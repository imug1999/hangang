import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
import schedule
import random

def main():
    url = 'https://api.hangang.msub.kr/'
    response = requests.get(url)
    contents = response.text
    json_ob = json.loads(contents)

    temp = json_ob['temp']
    time = json_ob['time']
    
    pic_list = 'https://funzinnu.com/stream/cdn/dccon/%ED%95%91%ED%81%AC%EB%B9%88.gif', 'https://funzinnu.com/stream/cdn/dccon/y.jpg', 'https://puu.sh/Be2kM/454abf3902.png', 'https://funzinnu.com/stream/cdn/dccon/%EC%99%9C%EA%B3%A1%EC%95%B5%EB%AC%B4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EC%8A%A4%ED%95%80%EC%95%B5%EB%AC%B4.gif', 'https://puu.sh/BhRU3/11b721faee.png', 'https://puu.sh/BvBBz/a0656c7f94.png', 'https://funzinnu.com/stream/cdn/dccon/%EB%A7%88%EC%B0%B8%EB%82%B4.png', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EC%A4%80%EB%B9%84.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A42.gif'
    print(random.choice(pic_list))

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/950082233358745632/EvuYQRu21mHFpGomerbrR9kdJY-jlblr-77RyxRCxHZL7GRSmr7u6dd99EMPxLhKEmca')

    embed = DiscordEmbed(title=':ocean: 현재 한강수온', description='{}도\n{}'.format(temp, time), color='3838ff')
    embed.set_thumbnail(url=random.choice(pic_list))


    webhook.add_embed(embed)

    print(json_ob)
    print(temp)
    print(time)

    response = webhook.execute()

schedule.every(3).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)