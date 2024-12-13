import asyncio
from os import environ

global CLIENTS
CLIENTS = {}

CHAT_PORT = environ.get("CHAT_PORT")
MAX_USERS = environ.get("MAX_USERS")

print("coucou")

async def handle_client_msg(reader, writer):
    print("client connecté")
    addr = writer.get_extra_info('peername')
    firstmsg = False
    if addr not in CLIENTS :
        CLIENTS[addr] = {"r" : reader, "w" : writer}
        firstmsg = True
    while True:

        data = await reader.read(1024)

        if data == b'':
            CLIENTS.pop(addr)
            for client, infos in CLIENTS.items() :
                if client != addr :
                    infos["w"].write(f"Annonce : {pseudo} a quitté la chatroom".encode())
                    await infos["w"].drain()
            break

        message = data.decode()
        print(f"Message received from {addr[0]}:{addr[1]} : {message}")
        if firstmsg :
            if message[:6] != "Hello|" :
                print("le premier msg n'est pas le pseudo")
                CLIENTS.pop(addr)
                break
            CLIENTS[addr]["pseudo"] = str(message).split('|')[1]
            firstmsg = False
            pseudo = CLIENTS[addr]["pseudo"]
            for client, infos in CLIENTS.items() :
                if client != addr :
                    infos["w"].write(f"Annonce : {pseudo} a rejoint la chatroom".encode())
                    await infos["w"].drain()
       
        else :
            pseudo = CLIENTS[addr]["pseudo"]
            for client, infos in CLIENTS.items() :
                if client != addr :
                    infos["w"].write(f"{pseudo} a dit : {message}".encode())
                    await infos["w"].drain()

async def main():
    print("coucou")
    server = await asyncio.start_server(handle_client_msg, '0.0.0.0', CHAT_PORT)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
