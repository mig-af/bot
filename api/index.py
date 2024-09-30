from flask import Flask, request 
import asyncio, re
from myBot import Bot
from download import verificar_link, descarga
from control import Seguridad



obj = ""
app = Flask(__name__)   
bot = Bot("6607114505:AAFUnp9YWU-XMYUZ0NoPiYExC9akq3sIgpY")
sec = Seguridad()

def buttonResponse():
    pass



async def messageHandler(data):
    search = data["message"]["text"]

    
    #await messageSend(data["message"]["from"]["id"], "resultado:")
    if(verificar_link(search) == True):
        bufferAudio = descarga(search)
        if(bufferAudio[1] != "error"):
            title = bufferAudio[1]
            musica = bufferAudio[0]
            audio = (f"{title}.mp3", musica, "audio/mpeg")
            await bot.sendChatAction(data["message"]["from"]["id"], "upload_audio")
            await bot.sendAudio(data["message"]["from"]["id"], audio)
        else:
            await bot.sendChatAction(data["message"]["from"]["id"], "typing")
            await bot.messageSend(data["message"]["from"]["id"],bufferAudio[0])
    else:
        await bot.messageSend(data["message"]["from"]["id"], "Link incorrecto")
    
    #logging.info(f"funcion {messageHandler.__name__} ejecutada con exito")
    

async def startCommand(data):
    name = data["message"]["chat"]["first_name"]
    await bot.messageSend(data["message"]["from"]["id"], f"Hola {name}, copia el link de la cancion que quieres descargar" )
    #logging.info(f"funcion {startCommand.__name__} ejecutada con exito")


async def creditsCommand(data):
    creditos = "Creado por @pes528"
    await bot.messageSend(data["message"]["chat"]["id"], creditos)
    #logging.info(f"Funcion {creditsCommand.__name__} ejecutada")
    



async def remove_userCommand(data):
    id = re.search(r"/removeuser (\d+)", data["message"]["text"]).group(1)
    sec.borrar_usuario(id)
    await bot.messageSend(data["message"]["chat"]["id"], f"users: {sec.ver_usuarios()}")


async def add_userCommand(data):
    id = re.search(r"/adduser (\d+)", data["message"]["text"]).group(1)
    
    if data["message"]["chat"]["id"] != sec.ver_admin():
        pass
    else:
        sec.permitir_usuario(int(id))
        await bot.messageSend(data["message"]["chat"]["id"], f"users: {sec.ver_usuarios()}")



@app.route("/webhook", methods=["POST"])
async def main():
    

    data = request.json
    #print(data)
    try:
        #print(data)
        data["message"]

        if(sec.verificar_usuario(data["message"]["chat"]["id"])):

            if(data["message"]["text"] == "/start"):
                
                obj = data
                await startCommand(data)
            elif(data["message"]["text"] == "/creditos"):
                await creditsCommand(data)

            elif (re.match(r"/adduser (\d+)", data['message']['text'])):
                await add_userCommand(data)

            elif (re.match(r"/removeuser (\d+)", data['message']['text'])):
                await remove_userCommand(data)
            else:
                await messageHandler(data)
        else:
            await bot.messageSend(data["message"]["chat"]["id"], "No tienes acceso")
           
    except KeyError:
        pass


    return "", 200


if __name__ == "__main__":

    
    app.run(port=8443, debug=True)
