import requests
import json
from multiprocessing import Pool
import settings as s
import time
import telegram
import asyncio

bot = telegram.Bot(token=s.TELEGRAM_TOKEN)
# wrapper for messaging function
async def send_message(message, chat_id):
    async with bot:
        await bot.send_message(text=message, chat_id=chat_id)

# worker function
def deviceHandler(deviceName: str):
    while True:
        url = 'http://'+s.SERVER+':'+s.PORT+s.PATH+'/'+deviceName+'?limit=1'
        print(f'sending request to {url}')
        response =requests.get(url)
        if response.status_code == 200:
            response = response.json()
            print(response)
            for  event in response["events"]:
                for reading in event["readings"]:
                    if int(reading["value"]) < 1000:
                        print(f'device {deviceName} is rebooting')

                        asyncio.run(send_message(f'device {deviceName} is rebooting',s.TELEGRAM_CHANNEL_ID))

        time.sleep(5)

# MAIN
print(s.TELEGRAM_TOKEN)
print(s.TELEGRAM_CHANNEL_ID)
asyncio.run(send_message(f'monitor application started',s.TELEGRAM_CHANNEL_ID))

with Pool(s.POOL_SIZE) as p:
    print(p.map(deviceHandler, s.DEVICES))
