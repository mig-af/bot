import requests, asyncio
import logging, time, json, io

#logging.basicConfig(level=logging.INFO, format='%(levelname)s :::::::::::: %(message)s')

class Bot:

    __token = ""
    
    def __init__(self, token):
        self.__token = token
        self.url = f"https://api.telegram.org/bot{self.__token}" 


    async def sendAudio(self, chat_id, audio):
    
        data = {
            "chat_id":chat_id,

        }
        files = {
        #"audio":open(descarga("https://youtu.be/0f8Uz-UHSuw?si=TJfRy0nnRS4FKCGO"), "rb")
        "audio":audio
        }
        resp = requests.post(f"{self.url}/sendAudio", data=data, files=files)

        #logging.info(F"{self.sendAudio.__name__} ejecutada con la info:  {resp.text}")



    def inlineButton(self, listaObjetos: list):
        """
        listaObjetos -> [{
            "text":"texto",
            "callback_data":"mensaje callback" > si se usa web-app no debe haber el callback_data
            "web_app":{"ur":"url.com"}
        }], 

        """
        return {
            "inline_keyboard":[
                listaObjetos
            ]
            }


    async def messageSend(self, chat_id, message, reply_markp=None):
 
        data = {
        "chat_id":chat_id,
        "text": message,
        "reply_markup":"" if reply_markp == None else reply_markp,
        }

        resp = requests.post(f"{self.url}/sendMessage", json=data)
        #logging.info(f"funcion {self.messageSend.__name__} ejecutada con la informacion : {resp.text}")
        return



    async def sendChatAction(self, chat_id:int, action:str):

        """
        id: <int>
        action: "typing", "upload_photo", "upload_document"
        """

        data = {
        "chat_id":chat_id,
        "action":action
        }
        resp = requests.post(f"{self.url}/sendChatAction", json=data)
        #logging.info(f"funcion {self.sendChatAction.__name__} ejecutada con la informacion : {resp.text}")


