import json
import logging
from urllib import request, parse

# -*- coding:UTF-8 -*-
from urllib.error import URLError

from bs4 import BeautifulSoup


# from utils.utils import need_data, write_to_excel


def from_baidu_epidemic_data():
    global target_html
    url = 'http://wax.alcor.exchange/trade/fww-farmerstoken_wax-eosio.token'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.`0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    dict = {
        'name': 'Germey'
    }
    data = bytes(parse.urlencode(dict), encoding='utf8')
    logging.info('获取网站响应')
    response = request.Request(url=url, data=data, headers=headers, method='POST')
    target_response = request.urlopen(response)
    # try:
    #     response = request.Request(url=url, data=data, headers=headers, method='POST')
    #     target_response = request.urlopen(response)
    # except URLError:
    #     logging.error('获取连接失败')
    # else:
    #     # 获取到网页源代码
    target_html = target_response.read().decode('utf-8', 'ignore')

    print(target_html)
    # 网页源代码转换成lxml格式
    listmain_soup = BeautifulSoup(target_html, 'lxml')

    print(listmain_soup)
    # 获取到关于疫情的数据
    result_string = listmain_soup.find('script', id="captain-config").get_text()

    # result_string转换成json对象
    result_json = json.loads(result_string)
    print(result_json)

    case_list = result_json['component'][0]['caseList']
