import pika
import json
from conexoes import socket_obj
from conexoes import funcoes


class rabbit:
    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()


    def callback(self, ch, method, properties, body):
        mensagem = json.loads(body)
        print("hh")
        if socket_obj.objConnectedUsers[mensagem["ras_eve_id_indice"]]:
            funcoes.enviar(socket_obj.objConnectedUsers[mensagem["ras_eve_id_indice"]])
        if  socket_obj.objConnectedUsers[mensagem["ras_mon_hospedeiro"]]:
            funcoes.enviar(socket_obj.objConnectedUsers[mensagem["ras_mon_hospedeiro"]])






    def procurar(self):
        self.channel.basic_consume(queue='testerenan', on_message_callback=self.callback(), auto_ack=True)
        self.channel.start_consuming()


"""
    def callback(ch, method, properties, body):
        menssagem_rabbit = json.loads(body)
        for i in range(0, len(conexao_lista)):
            if (conexao_lista[i]["configuracao"]["ras_eve_id_indice"]) == (menssagem_rabbit["ras_eve_id_indice"]):
                conexao_lista[i]["endereco"].write_message(menssagem_rabbit)
                break

                """

