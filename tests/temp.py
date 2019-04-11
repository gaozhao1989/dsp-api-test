import pymongo
from sshtunnel import SSHTunnelForwarder


MONGO_HOST = '182.140.144.180'
MONGO_DB = 'sndo'
MONGO_USER = 'staff'
MONGO_PASS = 'zxt@56$%998*'
BIND_HOST = '127.0.0.1'
BIND_PORT = 27018
server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=(BIND_HOST, BIND_PORT)
)
server.start()
client = pymongo.MongoClient(BIND_HOST, server.local_bind_port)
print(client[MONGO_DB].list_collection_names())
server.stop()