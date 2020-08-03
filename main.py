import threading
from conexoes import rabbit
from conexoes import socket_obj
import tornado.ioloop



threading.Thread(target=rabbit.procurar, args=()).start()
application = tornado.web.Application([(r"/", socket_obj.WebSocketHandler), ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

