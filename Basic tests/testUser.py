from zk import ZK, const

conn = None
zk = ZK('192.168.1.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
conn = zk.connect()

users = conn.get_users()
conn.set_user(uid=20, name='MOHAMED AMINE BEN AFIA', privilege=const.USER_ADMIN, password='12345678', group_id='', user_id='8', card=0)

print(users)