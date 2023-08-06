import asyncio
import ctypes
import fcntl
import os.path
import platform
import queue
import sysconfig
import threading
import time

_AIX = platform.system() == 'AIX'
_DARWIN = platform.system() == 'Darwin'
_LINUX = platform.system() == 'Linux'
_WINDOWS = platform.system() == 'windows'

class sub_worker(object):
    def __init__(self, user, password, host, port, dbname, notify_name):
        self.user, self.password, self.host, self.port, self.dbname, self.notify_name = \
            user, password, host, port, dbname, notify_name
        self.r_pip, self.w_pip, self.loop, self.transport = None, None, None, None
        self.is_running = False
        self.events = queue.Queue()
        if _WINDOWS:
            self.lib = ctypes.cdll.LoadLibrary(os.path.dirname(os.path.realpath(__file__)) + '/sub.dll')
        elif _DARWIN:
            if 'arm64' in sysconfig.get_platform():
                self.lib = ctypes.cdll.LoadLibrary(os.path.dirname(os.path.realpath(__file__)) + '/sub-mac-m1.so')
            else:
                self.lib = ctypes.cdll.LoadLibrary(os.path.dirname(os.path.realpath(__file__)) + '/sub.so')
        else:
            self.lib = ctypes.cdll.LoadLibrary(os.path.dirname(os.path.realpath(__file__)) + '/sub-linux.so')
        r, w = os.pipe()
        self.r_pip, self.w_pip = r, w
        w_flags = fcntl.fcntl(w, fcntl.F_GETFL)
        w_flags = w_flags | os.O_NONBLOCK
        fcntl.fcntl(w, fcntl.F_SETFL, w_flags)

        r_flags = fcntl.fcntl(r, fcntl.F_GETFL)
        r_flags = r_flags | os.O_NONBLOCK
        fcntl.fcntl(r, fcntl.F_SETFL, r_flags)

        self.loop = asyncio.get_event_loop()

    def start(self):
        if self.is_running:
            return
        t = threading.Thread(target=self._call_go_sub_work)
        t.setDaemon(True)
        t.start()
        self.is_running = True
        # self.loop.create_task(self._read_pip())
        # self.loop.run_forever()
        self.loop.run_until_complete(self._read_pip())

    def _call_go_sub_work(self):
        self.lib.SubWorkStart(self.w_pip,
                              self.user.encode('UTF-8'),
                              self.password.encode('UTF-8'),
                              self.host.encode('UTF-8'),
                              self.port,
                              self.dbname.encode('UTF-8'),
                              self.notify_name.encode('UTF-8'))

    async def _read_pip(self):
        try:
            r = os.fdopen(self.r_pip)
            loop = self.loop
            reader = asyncio.StreamReader(loop=loop)
            protocol = asyncio.StreamReaderProtocol(reader)
            transport, _ = await loop.connect_read_pipe(lambda: protocol, r)
            while True:
                data = b''
                dumpLenBy = await reader.read(4)
                dumpLen = int.from_bytes(dumpLenBy, 'big', signed=True)
                if dumpLen < 0:
                    loop.stop()
                    break
                while True:
                    if len(data) >= dumpLen:
                        break
                    out = await reader.read(dumpLen)
                    if out is None:
                        break
                    else:
                        data += out
                fs = loop.run_in_executor(None, self.events.put, data)
                await asyncio.wait(fs={fs})
                # self.events.put(data)
        except Exception as e:
            print(e)

    def get_event(self):
        while True:
            yield self.events.get()

    def close(self):
        with os.fdopen(self.w_pip, 'wb') as w:
            w.write(int.to_bytes(-1, 4, 'big', signed=True))
        time.sleep(1)
        self.loop.close()
        return