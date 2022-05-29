import requests
import json
import time
import schedule
import random
import math
import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
from bs4 import BeautifulSoup
import urllib.request as req

def full_mor():
# 날짜 계산
    today = datetime.date.today()

    #서코
    seoulcomic = datetime.date(2022,5,15)
    seoulcomic_d = seoulcomic - today

    #한강 API
    han_url = 'https://api.hangang.msub.kr/'
    han_response = requests.get(han_url)
    han_contents = han_response.text
    han_json = json.loads(han_contents)
    temp = han_json['temp']
    time = han_json['time']

    # 비트코인 API
    bit_url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days/?code=CRIX.UPBIT.KRW-BTC'
    bit_response = requests.get(bit_url)
    bit_contents = bit_response.text
    bit_ljson = json.loads(bit_contents)

    # 거래 가격
    bit_tp = bit_ljson[0]['tradePrice']
    bit_tpc = format(math.trunc(bit_tp), ',')
    # 전일 종가
    bit_closing = bit_ljson[0]['prevClosingPrice']
    bit_closingc = format(math.trunc(bit_closing), ',')
    # 전일 대비
    bit_change = bit_ljson[0]['change']
    if bit_change == 'RISE':
        bit_change_emoji = ':chart_with_upwards_trend: 상승 '
    if bit_change == 'FALL':
        bit_change_emoji = ':chart_with_downwards_trend: 하락 '
    if bit_change == 'EVEN':
        bit_change_emoji = ':repeat:'
        
    # 전일 대비 rate
    bit_rate = bit_ljson[0]['changeRate']
    bit_ratec = round(bit_rate,4)

    # 전일 대비 price
    bit_lp = bit_ljson[0]['signedChangePrice']
    bit_lpc = format(math.trunc(bit_lp),',')


    # 이더리움 API
    eth_url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days/?code=CRIX.UPBIT.KRW-ETH'
    eth_response = requests.get(eth_url)
    eth_contents = eth_response.text
    eth_ljson = json.loads(eth_contents)

    # 거래 가격
    eth_tp = eth_ljson[0]['tradePrice']
    eth_tpc = format(math.trunc(eth_tp), ',')
    # 전일 종가
    eth_closing = eth_ljson[0]['prevClosingPrice']
    eth_closingc = format(math.trunc(eth_closing), ',')
    # 전일 대비
    eth_change = eth_ljson[0]['change']
    if eth_change == 'RISE':
        eth_change_emoji = ':chart_with_upwards_trend: 상승 '
    if eth_change == 'FALL':
        eth_change_emoji = ':chart_with_downwards_trend: 하락 '
    if eth_change == 'EVEN':
        eth_change_emoji = ':repeat:'

    # 전일 대비 rate
    eth_rate = eth_ljson[0]['changeRate']
    eth_ratec = round(eth_rate,4)

    # 전일 대비 price
    eth_lp = eth_ljson[0]['signedChangePrice']
    eth_lpc = format(math.trunc(eth_lp),',')


    # 환율정보 크롤링
    uk_url = "http://finance.naver.com/marketindex/"
    uk_res = req.urlopen(uk_url)
    uk_soup = BeautifulSoup(uk_res, "html.parser")
    uk_price = uk_soup.select_one("div.head_info > span.value").string

    # MSI RTX3060 크롤링
    p3060 = requests.get("https://search.shopping.naver.com/catalog/27313935527?cat_id=50003104&frm=NVSCPRO&query=rtx3060&NaPm=ct%3Dl1dusiww%7Cci%3D21d566b0ce9b4e658ffa0f717112e1f834988d69%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D3b1e941f67f0c226d1e6098cc393037aeca16e01")
    s3060 = BeautifulSoup(p3060.content, "html.parser")
    rtx3060 = s3060.select_one('.lowestPrice_num__3AlQ-').string
        
    # MSI RTX3070 크롤링
    p3070 = requests.get("https://search.shopping.naver.com/catalog/28168478522?cat_id=50003104&frm=NVSCPRO&query=rtx3070&NaPm=ct%3Dl1dvat3c%7Cci%3D7e2f533a73f461a8fc41fce1923578b8fc89e01d%7Ctr%3Dsls%7Csn%3D95694%7Chk%3Db15c9959feebc5fed948216a25de38b893f373a3")
    s3070 = BeautifulSoup(p3070.content, "html.parser")
    rtx3070 = s3070.select_one('.lowestPrice_num__3AlQ-').string

        
    pic_list = 'https://funzinnu.com/stream/cdn/dccon/%ED%95%91%ED%81%AC%EB%B9%88.gif', 'https://funzinnu.com/stream/cdn/dccon/y.jpg', 'https://puu.sh/Be2kM/454abf3902.png', 'https://funzinnu.com/stream/cdn/dccon/%EC%99%9C%EA%B3%A1%EC%95%B5%EB%AC%B4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EC%8A%A4%ED%95%80%EC%95%B5%EB%AC%B4.gif', 'https://puu.sh/BhRU3/11b721faee.png', 'https://puu.sh/BvBBz/a0656c7f94.png', 'https://funzinnu.com/stream/cdn/dccon/%EB%A7%88%EC%B0%B8%EB%82%B4.png', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EC%A4%80%EB%B9%84.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A42.gif'
    emoji_list = ':cat:', ':fox:', ':koala:', ':pig:', ':frog:', ':chicken:', ':wolf:', ':duck:'
    hello = '좋은 아침입니다.', '좋은 아침아침아침 입니다.', '.다니입침아 은좋','냐옹냐옹냐옹', '멍멍멍멍멍멍', '왈왈왈왈왈왈왈', '早上好', 'Good Morning', 'Bonjour', 'Guten Morgen'

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/958695648713113631/8FgFmdDVif_yAF-xuOu1FDmqXLQcR-HaODDMrLiKqZD59hWfBEXqLedZUy5jqUEdc984')

    embed = DiscordEmbed(title='{} {}'.format(random.choice(emoji_list), random.choice(hello)), description='', color='3838ff')
    embed.set_thumbnail(url=random.choice(pic_list))
    embed.add_embed_field(name=':ocean: 한강 수온', value='{}도'.format(temp))
    embed.add_embed_field(name=':person_doing_cartwheel: 서코까지', value='{}일'.format(seoulcomic_d.days))
    embed.add_embed_field(name=':dollar: 원달러', value='{}원'.format(uk_price), inline=False)
    embed.add_embed_field(name='ㅤ',value='ㅤ', inline=False)
    embed.add_embed_field(name=':coin: 비트코인', value='**{}원** | {} | {}% | {}원'.format(bit_tpc, bit_change_emoji, bit_ratec, bit_lpc), inline=False)
    embed.add_embed_field(name=':white_heart: 이더리움', value='**{}원** | {} | {}% | {}원'.format(eth_tpc, eth_change_emoji, eth_ratec, eth_lpc), inline=False)
    embed.add_embed_field(name='MSI RTX3060', value='{}원'.format(rtx3060))
    embed.add_embed_field(name='MSI RTX3070', value='{}원'.format(rtx3070))



    #embed.add_embed_field(name='대비, 비율', value='{} {}%'.format(bit_change_emoji,bit_ratec))

    webhook.add_embed(embed)

    print('--------------------------------------------')
    print('한강 온도 = ',temp,'도')
    print("원달러 = ",uk_price,'원')
    print('서코까지 {}일 남았습니다.'.format(seoulcomic_d.days))
    print('비트코인 거래가격 = ',bit_tpc,'원')
    print('전일 종가 = ',bit_closingc,'원')
    print('전일 대비 = ',bit_change, bit_change_emoji)
    print('전일 대비 rate = ',bit_ratec,'%')
    print('전일 대비 price = ', bit_lpc,'원')
    print('--------------------------------------------')
    print('이더리움 거래가격 = ',eth_tpc,'원')
    print('전일 종가 = ',eth_closingc,'원')
    print('전일 대비 = ',eth_change, eth_change_emoji)
    print('전일 대비 rate = ',eth_ratec,'%')
    print('전일 대비 price = ', eth_lpc,'원')
    print('RTX3060 최저가 = ',rtx3060,'원')
    print('RTX3070 최저가 = ',rtx3070,'원')

    # 웹훅 발사
    response = webhook.execute()
    
def full_end():
    # 날짜 계산
    today = datetime.date.today()

    #서코
    seoulcomic = datetime.date(2022,5,15)
    seoulcomic_d = seoulcomic - today

    #한강 API
    han_url = 'https://api.hangang.msub.kr/'
    han_response = requests.get(han_url)
    han_contents = han_response.text
    han_json = json.loads(han_contents)
    temp = han_json['temp']
    time = han_json['time']

    # 비트코인 API
    bit_url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days/?code=CRIX.UPBIT.KRW-BTC'
    bit_response = requests.get(bit_url)
    bit_contents = bit_response.text
    bit_ljson = json.loads(bit_contents)

    # 거래 가격
    bit_tp = bit_ljson[0]['tradePrice']
    bit_tpc = format(math.trunc(bit_tp), ',')
    # 전일 종가
    bit_closing = bit_ljson[0]['prevClosingPrice']
    bit_closingc = format(math.trunc(bit_closing), ',')
    # 전일 대비
    bit_change = bit_ljson[0]['change']
    if bit_change == 'RISE':
        bit_change_emoji = ':chart_with_upwards_trend: 상승 '
    if bit_change == 'FALL':
        bit_change_emoji = ':chart_with_downwards_trend: 하락 '
    if bit_change == 'EVEN':
        bit_change_emoji = ':repeat:'
        
    # 전일 대비 rate
    bit_rate = bit_ljson[0]['changeRate']
    bit_ratec = round(bit_rate,4)

    # 전일 대비 price
    bit_lp = bit_ljson[0]['signedChangePrice']
    bit_lpc = format(math.trunc(bit_lp),',')


    # 이더리움 API
    eth_url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days/?code=CRIX.UPBIT.KRW-ETH'
    eth_response = requests.get(eth_url)
    eth_contents = eth_response.text
    eth_ljson = json.loads(eth_contents)

    # 거래 가격
    eth_tp = eth_ljson[0]['tradePrice']
    eth_tpc = format(math.trunc(eth_tp), ',')
    # 전일 종가
    eth_closing = eth_ljson[0]['prevClosingPrice']
    eth_closingc = format(math.trunc(eth_closing), ',')
    # 전일 대비
    eth_change = eth_ljson[0]['change']
    if eth_change == 'RISE':
        eth_change_emoji = ':chart_with_upwards_trend: 상승 '
    if eth_change == 'FALL':
        eth_change_emoji = ':chart_with_downwards_trend: 하락 '
    if eth_change == 'EVEN':
        eth_change_emoji = ':repeat:'

    # 전일 대비 rate
    eth_rate = eth_ljson[0]['changeRate']
    eth_ratec = round(eth_rate,4)

    # 전일 대비 price
    eth_lp = eth_ljson[0]['signedChangePrice']
    eth_lpc = format(math.trunc(eth_lp),',')


    # 환율정보 크롤링
    uk_url = "http://finance.naver.com/marketindex/"
    uk_res = req.urlopen(uk_url)
    uk_soup = BeautifulSoup(uk_res, "html.parser")
    uk_price = uk_soup.select_one("div.head_info > span.value").string

    # MSI RTX3060 크롤링
    p3060 = requests.get("https://search.shopping.naver.com/catalog/27313935527?cat_id=50003104&frm=NVSCPRO&query=rtx3060&NaPm=ct%3Dl1dusiww%7Cci%3D21d566b0ce9b4e658ffa0f717112e1f834988d69%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D3b1e941f67f0c226d1e6098cc393037aeca16e01")
    s3060 = BeautifulSoup(p3060.content, "html.parser")
    rtx3060 = s3060.select_one('.lowestPrice_num__3AlQ-').string
        
    # MSI RTX3070 크롤링
    p3070 = requests.get("https://search.shopping.naver.com/catalog/28168478522?cat_id=50003104&frm=NVSCPRO&query=rtx3070&NaPm=ct%3Dl1dvat3c%7Cci%3D7e2f533a73f461a8fc41fce1923578b8fc89e01d%7Ctr%3Dsls%7Csn%3D95694%7Chk%3Db15c9959feebc5fed948216a25de38b893f373a3")
    s3070 = BeautifulSoup(p3070.content, "html.parser")
    rtx3070 = s3070.select_one('.lowestPrice_num__3AlQ-').string

        
    pic_list = 'https://funzinnu.com/stream/cdn/dccon/%ED%95%91%ED%81%AC%EB%B9%88.gif', 'https://funzinnu.com/stream/cdn/dccon/y.jpg', 'https://puu.sh/Be2kM/454abf3902.png', 'https://funzinnu.com/stream/cdn/dccon/%EC%99%9C%EA%B3%A1%EC%95%B5%EB%AC%B4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EC%8A%A4%ED%95%80%EC%95%B5%EB%AC%B4.gif', 'https://puu.sh/BhRU3/11b721faee.png', 'https://puu.sh/BvBBz/a0656c7f94.png', 'https://funzinnu.com/stream/cdn/dccon/%EB%A7%88%EC%B0%B8%EB%82%B4.png', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EC%A4%80%EB%B9%84.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A42.gif'
    emoji_list = ':cat:', ':fox:', ':koala:', ':pig:', ':frog:', ':chicken:', ':wolf:', ':duck:'
    hello = '저녁 결산', '안녕~', '!!!!!!!'

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/958695648713113631/8FgFmdDVif_yAF-xuOu1FDmqXLQcR-HaODDMrLiKqZD59hWfBEXqLedZUy5jqUEdc984')

    embed = DiscordEmbed(title='{} {}'.format(random.choice(emoji_list), random.choice(hello)), description='', color='3838ff')
    embed.set_thumbnail(url=random.choice(pic_list))
    embed.add_embed_field(name=':ocean: 한강 수온', value='{}도'.format(temp))
    embed.add_embed_field(name=':person_doing_cartwheel: 서코까지', value='{}일'.format(seoulcomic_d.days))
    embed.add_embed_field(name=':dollar: 원달러', value='{}원'.format(uk_price), inline=False)
    embed.add_embed_field(name='ㅤ',value='ㅤ', inline=False)
    embed.add_embed_field(name=':coin: 비트코인', value='**{}원** | {} | {}% | {}원'.format(bit_tpc, bit_change_emoji, bit_ratec, bit_lpc), inline=False)
    embed.add_embed_field(name=':white_heart: 이더리움', value='**{}원** | {} | {}% | {}원'.format(eth_tpc, eth_change_emoji, eth_ratec, eth_lpc), inline=False)
    embed.add_embed_field(name='MSI RTX3060', value='{}원'.format(rtx3060))
    embed.add_embed_field(name='MSI RTX3070', value='{}원'.format(rtx3070))



    #embed.add_embed_field(name='대비, 비율', value='{} {}%'.format(bit_change_emoji,bit_ratec))

    webhook.add_embed(embed)

    print('--------------------------------------------')
    print('한강 온도 = ',temp,'도')
    print("원달러 = ",uk_price,'원')
    print('서코까지 {}일 남았습니다.'.format(seoulcomic_d.days))
    print('비트코인 거래가격 = ',bit_tpc,'원')
    print('전일 종가 = ',bit_closingc,'원')
    print('전일 대비 = ',bit_change, bit_change_emoji)
    print('전일 대비 rate = ',bit_ratec,'%')
    print('전일 대비 price = ', bit_lpc,'원')
    print('--------------------------------------------')
    print('이더리움 거래가격 = ',eth_tpc,'원')
    print('전일 종가 = ',eth_closingc,'원')
    print('전일 대비 = ',eth_change, eth_change_emoji)
    print('전일 대비 rate = ',eth_ratec,'%')
    print('전일 대비 price = ', eth_lpc,'원')
    print('RTX3060 최저가 = ',rtx3060,'원')
    print('RTX3070 최저가 = ',rtx3070,'원')

    # 웹훅 발사
    response = webhook.execute()

def full_lunch():
    # 날짜 계산
    today = datetime.date.today()

    #서코
    seoulcomic = datetime.date(2022,5,14)
    seoulcomic_d = seoulcomic - today

    #한강 API
    han_url = 'https://api.hangang.msub.kr/'
    han_response = requests.get(han_url)
    han_contents = han_response.text
    han_json = json.loads(han_contents)
    temp = han_json['temp']
    time = han_json['time']

    # 비트코인 API
    bit_url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days/?code=CRIX.UPBIT.KRW-BTC'
    bit_response = requests.get(bit_url)
    bit_contents = bit_response.text
    bit_ljson = json.loads(bit_contents)

    # 거래 가격
    bit_tp = bit_ljson[0]['tradePrice']
    bit_tpc = format(math.trunc(bit_tp), ',')
    # 전일 종가
    bit_closing = bit_ljson[0]['prevClosingPrice']
    bit_closingc = format(math.trunc(bit_closing), ',')
    # 전일 대비
    bit_change = bit_ljson[0]['change']
    if bit_change == 'RISE':
        bit_change_emoji = ':chart_with_upwards_trend: 상승 '
    if bit_change == 'FALL':
        bit_change_emoji = ':chart_with_downwards_trend: 하락 '
    if bit_change == 'EVEN':
        bit_change_emoji = ':repeat:'
        
    # 전일 대비 rate
    bit_rate = bit_ljson[0]['changeRate']
    bit_ratec = round(bit_rate,4)

    # 전일 대비 price
    bit_lp = bit_ljson[0]['signedChangePrice']
    bit_lpc = format(math.trunc(bit_lp),',')


    # 이더리움 API
    eth_url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days/?code=CRIX.UPBIT.KRW-ETH'
    eth_response = requests.get(eth_url)
    eth_contents = eth_response.text
    eth_ljson = json.loads(eth_contents)

    # 거래 가격
    eth_tp = eth_ljson[0]['tradePrice']
    eth_tpc = format(math.trunc(eth_tp), ',')
    # 전일 종가
    eth_closing = eth_ljson[0]['prevClosingPrice']
    eth_closingc = format(math.trunc(eth_closing), ',')
    # 전일 대비
    eth_change = eth_ljson[0]['change']
    if eth_change == 'RISE':
        eth_change_emoji = ':chart_with_upwards_trend: 상승 '
    if eth_change == 'FALL':
        eth_change_emoji = ':chart_with_downwards_trend: 하락 '
    if eth_change == 'EVEN':
        eth_change_emoji = ':repeat:'

    # 전일 대비 rate
    eth_rate = eth_ljson[0]['changeRate']
    eth_ratec = round(eth_rate,4)

    # 전일 대비 price
    eth_lp = eth_ljson[0]['signedChangePrice']
    eth_lpc = format(math.trunc(eth_lp),',')


    # 환율정보 크롤링
    uk_url = "http://finance.naver.com/marketindex/"
    uk_res = req.urlopen(uk_url)
    uk_soup = BeautifulSoup(uk_res, "html.parser")
    uk_price = uk_soup.select_one("div.head_info > span.value").string

    # MSI RTX3060 크롤링
    p3060 = requests.get("https://search.shopping.naver.com/catalog/27313935527?cat_id=50003104&frm=NVSCPRO&query=rtx3060&NaPm=ct%3Dl1dusiww%7Cci%3D21d566b0ce9b4e658ffa0f717112e1f834988d69%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D3b1e941f67f0c226d1e6098cc393037aeca16e01")
    s3060 = BeautifulSoup(p3060.content, "html.parser")
    rtx3060 = s3060.select_one('.lowestPrice_num__3AlQ-').string
        
    # MSI RTX3070 크롤링
    p3070 = requests.get("https://search.shopping.naver.com/catalog/28168478522?cat_id=50003104&frm=NVSCPRO&query=rtx3070&NaPm=ct%3Dl1dvat3c%7Cci%3D7e2f533a73f461a8fc41fce1923578b8fc89e01d%7Ctr%3Dsls%7Csn%3D95694%7Chk%3Db15c9959feebc5fed948216a25de38b893f373a3")
    s3070 = BeautifulSoup(p3070.content, "html.parser")
    rtx3070 = s3070.select_one('.lowestPrice_num__3AlQ-').string

        
    pic_list = 'https://funzinnu.com/stream/cdn/dccon/%ED%95%91%ED%81%AC%EB%B9%88.gif', 'https://funzinnu.com/stream/cdn/dccon/y.jpg', 'https://puu.sh/Be2kM/454abf3902.png', 'https://funzinnu.com/stream/cdn/dccon/%EC%99%9C%EA%B3%A1%EC%95%B5%EB%AC%B4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EC%8A%A4%ED%95%80%EC%95%B5%EB%AC%B4.gif', 'https://puu.sh/BhRU3/11b721faee.png', 'https://puu.sh/BvBBz/a0656c7f94.png', 'https://funzinnu.com/stream/cdn/dccon/%EB%A7%88%EC%B0%B8%EB%82%B4.png', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EC%A4%80%EB%B9%84.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A42.gif'
    emoji_list = ':cat:', ':fox:', ':koala:', ':pig:', ':frog:', ':chicken:', ':wolf:', ':duck:'
    hello = '좋은 점심', '배고파', '밥줘', '점!심', '점?심'

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/958695648713113631/8FgFmdDVif_yAF-xuOu1FDmqXLQcR-HaODDMrLiKqZD59hWfBEXqLedZUy5jqUEdc984')

    embed = DiscordEmbed(title='{} {}'.format(random.choice(emoji_list), random.choice(hello)), description='', color='3838ff')
    embed.set_thumbnail(url=random.choice(pic_list))
    embed.add_embed_field(name=':ocean: 한강 수온', value='{}도'.format(temp))
    embed.add_embed_field(name=':person_doing_cartwheel: 서코까지', value='{}일'.format(seoulcomic_d.days))
    embed.add_embed_field(name=':dollar: 원달러', value='{}원'.format(uk_price), inline=False)
    embed.add_embed_field(name='ㅤ',value='ㅤ', inline=False)
    embed.add_embed_field(name=':coin: 비트코인', value='**{}원** | {} | {}% | {}원'.format(bit_tpc, bit_change_emoji, bit_ratec, bit_lpc), inline=False)
    embed.add_embed_field(name=':white_heart: 이더리움', value='**{}원** | {} | {}% | {}원'.format(eth_tpc, eth_change_emoji, eth_ratec, eth_lpc), inline=False)
    embed.add_embed_field(name='MSI RTX3060', value='{}원'.format(rtx3060))
    embed.add_embed_field(name='MSI RTX3070', value='{}원'.format(rtx3070))



    #embed.add_embed_field(name='대비, 비율', value='{} {}%'.format(bit_change_emoji,bit_ratec))

    webhook.add_embed(embed)

    print('--------------------------------------------')
    print('한강 온도 = ',temp,'도')
    print("원달러 = ",uk_price,'원')
    print('서코까지 {}일 남았습니다.'.format(seoulcomic_d.days))
    print('비트코인 거래가격 = ',bit_tpc,'원')
    print('전일 종가 = ',bit_closingc,'원')
    print('전일 대비 = ',bit_change, bit_change_emoji)
    print('전일 대비 rate = ',bit_ratec,'%')
    print('전일 대비 price = ', bit_lpc,'원')
    print('--------------------------------------------')
    print('이더리움 거래가격 = ',eth_tpc,'원')
    print('전일 종가 = ',eth_closingc,'원')
    print('전일 대비 = ',eth_change, eth_change_emoji)
    print('전일 대비 rate = ',eth_ratec,'%')
    print('전일 대비 price = ', eth_lpc,'원')
    print('RTX3060 최저가 = ',rtx3060,'원')
    print('RTX3070 최저가 = ',rtx3070,'원')

    # 웹훅 발사
    response = webhook.execute()

def short():
        # 날짜 계산
    today = datetime.date.today()

    #서코
    seoulcomic = datetime.date(2022,5,14)
    seoulcomic_d = seoulcomic - today

    #한강 API
    han_url = 'https://api.hangang.msub.kr/'
    han_response = requests.get(han_url)
    han_contents = han_response.text
    han_json = json.loads(han_contents)
    temp = han_json['temp']
    time = han_json['time']

    # 비트코인 API
    bit_url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days/?code=CRIX.UPBIT.KRW-BTC'
    bit_response = requests.get(bit_url)
    bit_contents = bit_response.text
    bit_ljson = json.loads(bit_contents)

    # 거래 가격
    bit_tp = bit_ljson[0]['tradePrice']
    bit_tpc = format(math.trunc(bit_tp), ',')
    # 전일 종가
    bit_closing = bit_ljson[0]['prevClosingPrice']
    bit_closingc = format(math.trunc(bit_closing), ',')
    # 전일 대비
    bit_change = bit_ljson[0]['change']
    if bit_change == 'RISE':
        bit_change_emoji = ':chart_with_upwards_trend: 상승 '
    if bit_change == 'FALL':
        bit_change_emoji = ':chart_with_downwards_trend: 하락 '
    if bit_change == 'EVEN':
        bit_change_emoji = ':repeat:'
        
    # 전일 대비 rate
    bit_rate = bit_ljson[0]['changeRate']
    bit_ratec = round(bit_rate,4)

    # 전일 대비 price
    bit_lp = bit_ljson[0]['signedChangePrice']
    bit_lpc = format(math.trunc(bit_lp),',')


    # 이더리움 API
    eth_url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/days/?code=CRIX.UPBIT.KRW-ETH'
    eth_response = requests.get(eth_url)
    eth_contents = eth_response.text
    eth_ljson = json.loads(eth_contents)

    # 거래 가격
    eth_tp = eth_ljson[0]['tradePrice']
    eth_tpc = format(math.trunc(eth_tp), ',')
    # 전일 종가
    eth_closing = eth_ljson[0]['prevClosingPrice']
    eth_closingc = format(math.trunc(eth_closing), ',')
    # 전일 대비
    eth_change = eth_ljson[0]['change']
    if eth_change == 'RISE':
        eth_change_emoji = ':chart_with_upwards_trend: 상승 '
    if eth_change == 'FALL':
        eth_change_emoji = ':chart_with_downwards_trend: 하락 '
    if eth_change == 'EVEN':
        eth_change_emoji = ':repeat:'

    # 전일 대비 rate
    eth_rate = eth_ljson[0]['changeRate']
    eth_ratec = round(eth_rate,4)

    # 전일 대비 price
    eth_lp = eth_ljson[0]['signedChangePrice']
    eth_lpc = format(math.trunc(eth_lp),',')


    # 환율정보 크롤링
    uk_url = "http://finance.naver.com/marketindex/"
    uk_res = req.urlopen(uk_url)
    uk_soup = BeautifulSoup(uk_res, "html.parser")
    uk_price = uk_soup.select_one("div.head_info > span.value").string

    # MSI RTX3060 크롤링
    p3060 = requests.get("https://search.shopping.naver.com/catalog/27313935527?cat_id=50003104&frm=NVSCPRO&query=rtx3060&NaPm=ct%3Dl1dusiww%7Cci%3D21d566b0ce9b4e658ffa0f717112e1f834988d69%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D3b1e941f67f0c226d1e6098cc393037aeca16e01")
    s3060 = BeautifulSoup(p3060.content, "html.parser")
    rtx3060 = s3060.select_one('.lowestPrice_num__3AlQ-').string
        
    # MSI RTX3070 크롤링
    p3070 = requests.get("https://search.shopping.naver.com/catalog/28168478522?cat_id=50003104&frm=NVSCPRO&query=rtx3070&NaPm=ct%3Dl1dvat3c%7Cci%3D7e2f533a73f461a8fc41fce1923578b8fc89e01d%7Ctr%3Dsls%7Csn%3D95694%7Chk%3Db15c9959feebc5fed948216a25de38b893f373a3")
    s3070 = BeautifulSoup(p3070.content, "html.parser")
    rtx3070 = s3070.select_one('.lowestPrice_num__3AlQ-').string

        
    pic_list = 'https://funzinnu.com/stream/cdn/dccon/%ED%95%91%ED%81%AC%EB%B9%88.gif', 'https://funzinnu.com/stream/cdn/dccon/y.jpg', 'https://puu.sh/Be2kM/454abf3902.png', 'https://funzinnu.com/stream/cdn/dccon/%EC%99%9C%EA%B3%A1%EC%95%B5%EB%AC%B4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EC%8A%A4%ED%95%80%EC%95%B5%EB%AC%B4.gif', 'https://puu.sh/BhRU3/11b721faee.png', 'https://puu.sh/BvBBz/a0656c7f94.png', 'https://funzinnu.com/stream/cdn/dccon/%EB%A7%88%EC%B0%B8%EB%82%B4.png', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EC%A4%80%EB%B9%84.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A4.gif', 'https://funzinnu.com/stream/cdn/dccon/%EA%B4%80%EC%A7%9D%EB%8C%84%EC%8A%A42.gif'
    emoji_list = ':cat:', ':fox:', ':koala:', ':pig:', ':frog:', ':chicken:', ':wolf:', ':duck:'

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/958695648713113631/8FgFmdDVif_yAF-xuOu1FDmqXLQcR-HaODDMrLiKqZD59hWfBEXqLedZUy5jqUEdc984')

    embed = DiscordEmbed(title='{}'.format(random.choice(emoji_list)), description='', color='3838ff')
    embed.set_thumbnail(url=random.choice(pic_list))
    embed.add_embed_field(name=':ocean: 한강 수온', value='{}도'.format(temp))
    embed.add_embed_field(name=':dollar: 원달러', value='{}원'.format(uk_price), inline=False)
    embed.add_embed_field(name=':coin: 비트코인', value='{} | {}% | {}원'.format(bit_change_emoji, bit_ratec, bit_lpc), inline=False)
    embed.add_embed_field(name=':white_heart: 이더리움', value='{} | {}% | {}원'.format(eth_change_emoji, eth_ratec, eth_lpc), inline=False)




    #embed.add_embed_field(name='대비, 비율', value='{} {}%'.format(bit_change_emoji,bit_ratec))

    webhook.add_embed(embed)

    print('--------------------------------------------')
    print('한강 온도 = ',temp,'도')
    print("원달러 = ",uk_price,'원')
    print('서코까지 {}일 남았습니다.'.format(seoulcomic_d.days))
    print('비트코인 거래가격 = ',bit_tpc,'원')
    print('전일 종가 = ',bit_closingc,'원')
    print('전일 대비 = ',bit_change, bit_change_emoji)
    print('전일 대비 rate = ',bit_ratec,'%')
    print('전일 대비 price = ', bit_lpc,'원')
    print('--------------------------------------------')
    print('이더리움 거래가격 = ',eth_tpc,'원')
    print('전일 종가 = ',eth_closingc,'원')
    print('전일 대비 = ',eth_change, eth_change_emoji)
    print('전일 대비 rate = ',eth_ratec,'%')
    print('전일 대비 price = ', eth_lpc,'원')
    print('RTX3060 최저가 = ',rtx3060,'원')
    print('RTX3070 최저가 = ',rtx3070,'원')

    # 웹훅 발사
    response = webhook.execute()
    

#########################################
schedule.every().day.at('07:00').do(full_mor)

schedule.every().day.at('12:30').do(full_lunch)

schedule.every().day.at('23:00').do(full_end)



while True:
    schedule.run_pending()
    time.sleep(1)
