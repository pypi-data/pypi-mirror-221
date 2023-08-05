# coding: utf-8
from __future__ import print_function, unicode_literals

import argparse
import os
import signal
import sys
import threading

import queue

from .__init__ import ANYWIN
from .authsrv import AuthSrv
from .broker_util import BrokerCli, ExceptionalQueue
from .httpsrv import HttpSrv
from .util import FAKE_MP, Daemon, HMaccas

class MpWorker(BrokerCli):
    """one single mp instance"""

    def __init__(
        self,
        q_pend   ,
        q_yield   ,
        args ,
        n ,
    )  :
        super(MpWorker, self).__init__()

        self.q_pend = q_pend
        self.q_yield = q_yield
        self.args = args
        self.n = n

        self.log = self._log_disabled if args.q and not args.lo else self._log_enabled

        self.retpend   = {}
        self.retpend_mutex = threading.Lock()
        self.mutex = threading.Lock()

        # we inherited signal_handler from parent,
        # replace it with something harmless
        if not FAKE_MP:
            sigs = [signal.SIGINT, signal.SIGTERM]
            if not ANYWIN:
                sigs.append(signal.SIGUSR1)

            for sig in sigs:
                signal.signal(sig, self.signal_handler)

        # starting to look like a good idea
        self.asrv = AuthSrv(args, None, False)

        # instantiate all services here (TODO: inheritance?)
        self.iphash = HMaccas(os.path.join(self.args.E.cfg, "iphash"), 8)
        self.httpsrv = HttpSrv(self, n)

        # on winxp and some other platforms,
        # use thr.join() to block all signals
        Daemon(self.main, "mpw-main").join()

    def signal_handler(self, sig , frame )  :
        # print('k')
        pass

    def _log_enabled(self, src , msg , c   = 0)  :
        self.q_yield.put((0, "log", [src, msg, c]))

    def _log_disabled(self, src , msg , c   = 0)  :
        pass

    def logw(self, msg , c   = 0)  :
        self.log("mp{}".format(self.n), msg, c)

    def main(self)  :
        while True:
            retq_id, dest, args = self.q_pend.get()

            # self.logw("work: [{}]".format(d[0]))
            if dest == "shutdown":
                self.httpsrv.shutdown()
                self.logw("ok bye")
                sys.exit(0)
                return

            elif dest == "reload":
                self.logw("mpw.asrv reloading")
                self.asrv.reload()
                self.logw("mpw.asrv reloaded")

            elif dest == "listen":
                self.httpsrv.listen(args[0], args[1])

            elif dest == "set_netdevs":
                self.httpsrv.set_netdevs(args[0])

            elif dest == "retq":
                # response from previous ipc call
                with self.retpend_mutex:
                    retq = self.retpend.pop(retq_id)

                retq.put(args)

            else:
                raise Exception("what is " + str(dest))

    def ask(self, dest , *args )  :
        retq = ExceptionalQueue(1)
        retq_id = id(retq)
        with self.retpend_mutex:
            self.retpend[retq_id] = retq

        self.q_yield.put((retq_id, dest, list(args)))
        return retq

    def say(self, dest , *args )  :
        self.q_yield.put((0, dest, list(args)))
