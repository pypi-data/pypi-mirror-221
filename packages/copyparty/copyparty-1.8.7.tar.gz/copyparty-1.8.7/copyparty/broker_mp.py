# coding: utf-8
from __future__ import print_function, unicode_literals

import threading
import time
import traceback

import queue

from .__init__ import CORES, TYPE_CHECKING
from .broker_mpw import MpWorker
from .broker_util import ExceptionalQueue, try_exec
from .util import Daemon, mp

if TYPE_CHECKING:
    from .svchub import SvcHub

class MProcess(mp.Process):
    def __init__(
        self,
        q_pend   ,
        q_yield   ,
        target ,
        args ,
    )  :
        super(MProcess, self).__init__(target=target, args=args)
        self.q_pend = q_pend
        self.q_yield = q_yield


class BrokerMp(object):
    """external api; manages MpWorkers"""

    def __init__(self, hub )  :
        self.hub = hub
        self.log = hub.log
        self.args = hub.args

        self.procs = []
        self.mutex = threading.Lock()

        self.num_workers = self.args.j or CORES
        self.log("broker", "booting {} subprocesses".format(self.num_workers))
        for n in range(1, self.num_workers + 1):
            q_pend    = mp.Queue(1)
            q_yield    = mp.Queue(64)

            proc = MProcess(q_pend, q_yield, MpWorker, (q_pend, q_yield, self.args, n))
            Daemon(self.collector, "mp-sink-{}".format(n), (proc,))
            self.procs.append(proc)
            proc.start()

    def shutdown(self)  :
        self.log("broker", "shutting down")
        for n, proc in enumerate(self.procs):
            thr = threading.Thread(
                target=proc.q_pend.put((0, "shutdown", [])),
                name="mp-shutdown-{}-{}".format(n, len(self.procs)),
            )
            thr.start()

        with self.mutex:
            procs = self.procs
            self.procs = []

        while procs:
            if procs[-1].is_alive():
                time.sleep(0.1)
                continue

            procs.pop()

    def reload(self)  :
        self.log("broker", "reloading")
        for _, proc in enumerate(self.procs):
            proc.q_pend.put((0, "reload", []))

    def collector(self, proc )  :
        """receive message from hub in other process"""
        while True:
            msg = proc.q_yield.get()
            retq_id, dest, args = msg

            if dest == "log":
                self.log(*args)

            elif dest == "retq":
                # response from previous ipc call
                raise Exception("invalid broker_mp usage")

            else:
                # new ipc invoking managed service in hub
                try:
                    obj = self.hub
                    for node in dest.split("."):
                        obj = getattr(obj, node)

                    # TODO will deadlock if dest performs another ipc
                    rv = try_exec(retq_id, obj, *args)
                except:
                    rv = ["exception", "stack", traceback.format_exc()]

                if retq_id:
                    proc.q_pend.put((retq_id, "retq", rv))

    def ask(self, dest , *args )  :

        # new non-ipc invoking managed service in hub
        obj = self.hub
        for node in dest.split("."):
            obj = getattr(obj, node)

        rv = try_exec(True, obj, *args)

        retq = ExceptionalQueue(1)
        retq.put(rv)
        return retq

    def say(self, dest , *args )  :
        """
        send message to non-hub component in other process,
        returns a Queue object which eventually contains the response if want_retval
        (not-impl here since nothing uses it yet)
        """
        if dest == "listen":
            for p in self.procs:
                p.q_pend.put((0, dest, [args[0], len(self.procs)]))

        elif dest == "set_netdevs":
            for p in self.procs:
                p.q_pend.put((0, dest, list(args)))

        elif dest == "cb_httpsrv_up":
            self.hub.cb_httpsrv_up()

        else:
            raise Exception("what is " + str(dest))
