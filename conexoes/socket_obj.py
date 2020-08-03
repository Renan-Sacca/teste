import tornado.web
import tornado.websocket
import tornado.ioloop
import json
from conexoes import funcoes
objConnectedUsers = {}
objIdSocket = {}
class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def initialize(self):
        global objConnectedUsers
        global objIdSocket


    def open(self):
        print("Novo cliente conectado")



    def on_close(self):
        del objConnectedUsers[objIdSocket[self]]
        del objIdSocket[self]

        print("Cliente desconectado")
        for i in objConnectedUsers:
            print(i)

        for i in objIdSocket:
            print(i)


    def on_message(self, message):
        self.write_message(u"You said: " + message)
        existente = funcoes.verificar_novo(self, objIdSocket)
        if existente == 0:
            idCliente = ''
            idsVeiculos = []
            idsVeiculosProibidos = []
            dados = json.loads(message)

            if "cliente" in dados and dados["cliente"] != "" :
                idCliente = dados["cliente"]

            if "veiculos" in dados  and type(dados["veiculos"]) is list:
                idsVeiculos = dados["veiculos"]

            if "pveiculos" in dados  and type(dados["pveiculos"]) is list:
                idsVeiculosProibidos = dados["pveiculos"]

            objConnectedUsers[dados["indice"]] = funcoes.montarObjetoControle(dados["indice"],idCliente,idsVeiculos, idsVeiculosProibidos,self)
            objIdSocket[self] = dados["indice"]
            for i in objConnectedUsers:
                print(i)

            print(objConnectedUsers)
            print()

    def check_origin(self, origin):
        return True

    @staticmethod
    def get_objConnectedUsers():
        return objConnectedUsers


    """
    "objSocket":{
      "indice":502117,
      "hospedes":[
         "502208",
         "502282",
         "502346",
         "502117"
      ]
   }    
    """
