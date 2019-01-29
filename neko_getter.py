import sched
import datetime
import time
import threading
from neko_archiver import NekoArchiver


class NekoGetter:
    def __init__(self):
        pass

    def schedule(self, process):
        s = sched.scheduler(time.time, time.sleep)
        set_time = datetime.datetime.now()
        interval = datetime.timedelta(minutes=10)
        while True:
             # TODO: 良い感じにログ取りたい
            s.enterabs(time.mktime(set_time.timetuple()), 1, process)
            s.run()
            set_time += interval

    def control(self, process):
        thread_obj = threading.Thread(target=self.schedule, args=(process,), daemon=True)
        thread_obj.start()

    def run(self):
        neko = NekoArchiver()
        self.control(neko.get_toots)
