from sshtunnel import SSHTunnelForwarder
import pymongo

MONGO_HOST = "3.7.62.38"

server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_pkey='C:\\Users\\KEDAR\\PycharmProjects\\SudanConsultancy\\id_rsa',
    ssh_username='ubuntu',
    remote_bind_address=('127.0.0.1', 27017)
)
f = open('C:\\Users\\KEDAR\\PycharmProjects\\SudanConsultancy\\id_rsa')
server.ssh_pkeys.clear()
server.start()
client = pymongo.MongoClient('mongodb://prabjyot:PiPcJp8UTf6K@localhost:27017/siddhiart')
db = client['siddhiart']
col=db.get_collection('items')
