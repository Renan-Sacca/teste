import pika
import random

#criando conexao
conexao = pika.BlockingConnection (pika.ConnectionParameters ( host ='localhost' ))
channel = conexao.channel ()

#criando fila
#channel.queue_declare (queue = 'testerenan')

#exchange é o nome da troca
#routing key nome da fila
i=0

while i <2:
    a = random.randrange(0,2)
    if a == 1:
        a='{"ras_eve_id_indice":"930","mensagem":"ola mundo","ras_mon_hospedeiro":55}'
        channel.basic_publish (exchange = 'renan',
                              routing_key = 'testerenan',
                              body = a)

    else:
        a ='{"ras_eve_id_indice":"3333","mensagem":"ola world","ras_mon_hospedeiro":55}'
        channel.basic_publish(exchange='renan',
                              routing_key='testerenan',
                              body=a)
    print ( "[x] Enviado ",a )
    i += 1

conexao.close ()

