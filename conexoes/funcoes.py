from conexoes import socket_obj

def verificar_novo(atual,obj):
    for i in obj:
        if i == atual:
            return 1
    return 0

def montarObjetoControle(ind, cli, idsVei, idsVeicPro,endereco):
    return {
        "indice": ind,
        "cliente": cli,
        "veiculos": idsVei,
        "pveiculos": idsVeicPro,
        "endereco" : endereco
    }

def enviar(socket_conectado,mensagem):
    if len(socket_conectado["cliente"]) == 0 and len(socket_conectado["veiculos"]) == 0 and len(socket_conectado["pveiculos"]) == 0:
        print(socket_conectado)
        objConnectedUsers = socket_obj.WebSocketHandler.get_objConnectedUsers()
        objConnectedUsers["3333"]["endereco"].write_message(mensagem)
        print("qm")



#vem mensagem para 2 clientes na msm mensagem ?
#