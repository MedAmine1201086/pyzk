from zk import ZK, const

conn = None
zk = ZK('192.168.1.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
conn = zk.connect()

users = conn.get_users()
for user in users:
    privilege = 'User'
    if user.privilege == const.USER_ADMIN:
        privilege = 'Admin'
    print ('+ UID #{}'.format(user.uid))
    print ('  Name       : {}'.format(user.name))
    print ('  Privilege  : {}'.format(privilege))
    print ('  Password   : {}'.format(user.password))
    print ('  Group ID   : {}'.format(user.group_id))
    print ('  User  ID   : {}'.format(user.user_id))

