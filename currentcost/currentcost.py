import collectd
import threading


class CollectCostReader(threading.Thread):
    def __init__(self):
        self.s = serial.Serial('/dev/ttyUSB0', baudrate=57600)
        self.watts = {}

    def run(self):
        while True:
            l = self.s.readline()
            d = dom.parseString(l)
            msg = d.getElementsByTagName('msg')[0]
            chans = [msg.getElementsByTagName('ch%d' % i) for i in range(1, 4)]
            new_watts = {}
            for ch in chans:
                new_watts['ch%d' % ch] = int(ch[0].childNodes[0].childNodes[0].nodeValue)
            self.watts = new_watts

    def latest_watts(self):
        return self.watts

reader_thread = CollectCostReader()

def collectcost_init():
    reader_thread.start()

def collectcost_read():
    watts = reader_thread.latest_watts()

    for ch, w in watts.items():
        val = collectd.Values(plugin='currentcost')
        val.type = 'gauge'
        val.type_instance = ch
        val.values = [w]
        val.dispatch()

def collectcost_shutdown():
    reader_thread.stop()


collectd.register_init(collectcost_init)
collectd.register_read(collectcost_read)
collectd.register_shutdown(collectcost_shutdown)
