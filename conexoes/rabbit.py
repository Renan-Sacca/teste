import pika
import json
from conexoes import socket_obj
import threading
from conexoes import funcoes


def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    threading.Lock()
    objConnectedUsers = socket_obj.WebSocketHandler.get_objConnectedUsers()

    if mensagem["ras_eve_id_indice"] in objConnectedUsers:
        funcoes.enviar(objConnectedUsers[mensagem["ras_eve_id_indice"]],body)
    if mensagem["ras_mon_hospedeiro"] in objConnectedUsers:
        funcoes.enviar(objConnectedUsers[mensagem["ras_mon_hospedeiro"]],body)
    threading.RLock()

def procurar():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.basic_consume(queue='testerenan', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
