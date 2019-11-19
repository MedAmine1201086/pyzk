from zk import ZK, const
from datetime import datetime

conn = None
zk = ZK('192.168.1.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
conn = zk.connect()

# get current machine's time
zktime = conn.get_time()
print(zktime)
# update new time to machine
newtime = datetime.today()
conn.set_time(newtime)