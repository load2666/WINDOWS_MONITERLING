from cmath import pi
from PIL import ImageGrab
import cv2
import keyboard
import mouse
import numpy as np
import time
import discord,os,random,string


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    global ROI_SET, x1, y1, x2, y2
    ROI_SET = False
    print("Select your ROI using .")
    while(mouse.is_pressed() == False):
        x1, y1 = mouse.get_position()
        while(mouse.is_pressed() == True):
            x2, y2 = mouse.get_position()
            while(mouse.is_pressed() == False):
                print("마우스 좌표 : {0}, {1}, {2}, {3}".format(x1, y1, x2, y2))
                ROI_SET = True
                if ROI_SET == True:
                    img=ImageGrab.grab()
                    saveas='static/images/moniter.png'
                    img.save(saveas)
                    time.sleep(5)


# @client.event
# async def on_message(message):
        # if message.content.startswith(':Moniter'):
        #     global ROI_SET, x1, y1, x2, y2
        #     ROI_SET = False
        #     print("Select your ROI using .")
        #     while(mouse.is_pressed() == False):
        #         x1, y1 = mouse.get_position()
        #         while(mouse.is_pressed() == True):
        #             x2, y2 = mouse.get_position()
        #             while(mouse.is_pressed() == False):
        #                 print("마우스 좌표 : {0}, {1}, {2}, {3}".format(x1, y1, x2, y2))
        #                 ROI_SET = True
        #                 if ROI_SET == True:
        #                     img=ImageGrab.grab()
        #                     saveas='static/images/moniter.png'
        #                     img.save(saveas)
                            # with open('static/images/moniter.png', 'rb') as f:
                            #     picture = discord.File(f)
                            #     i = 1
                            #     i += 1
                            #     await message.channel.send("------------- 모니터링 ------------")
                            #     await message.channel.send(file=picture)
                            #     # break
                            #     # await message.edit(picture)
                            #     time.sleep(3)
                            #     # while True: 
                            #         # await message.channel.send(file=picture)
                            # 위에 주석처리된 구문은 디스코드에서 사용이 필요할시 주석을 해제해주세요




        



client.run("")