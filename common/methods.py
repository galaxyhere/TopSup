# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/9 10:39
# @desc    :

import requests
import webbrowser
import urllib.parse
from . import process

# # 颜色兼容Win 10
from colorama import init, Fore
init()


def open_webbrowser(question):
    webbrowser.open('https://baidu.com/s?wd=' + urllib.parse.quote(question))


def open_webbrowser_count(question, choices):
    print('\n-- 方法2： 题目+选项搜索结果计数法 --\n')
    print('Question: ' + question)
    if '不是' in question:
        print('**请注意此题为否定题,选计数最少的**')

    counts = []
    for i in range(len(choices)):
        # 请求
        req = requests.get(url='http://www.baidu.com/s',
                           params={'wd': question + choices[i]})
        content = req.text
        index = content.find('百度为您找到相关结果约') + 11
        content = content[index:]
        index = content.find('个')
        count = content[:index].replace(',', '')
        counts.append(count)
        #print(choices[i] + " : " + count)
    output(choices, counts)


def count_base(question, choices):
    print('\n-- 方法3： 题目搜索结果包含选项词频计数法 --\n')
    # 请求
    req = requests.get(url='http://www.baidu.com/s', params={'wd': question})
    content = req.text
    # print(content)

    print("====================\r\n")
    try:
        results = process.page(content) 
        #print (results)
        count = 0
        for result in results:
            result_str = ('{0}'.format(result.abstract))
            if "当前代码版本不予摘要" in result_str:
                continue
            else:
                try:
                    # print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
                    print(result_str.replace(u'\xa0', u' ') + "\r\n")  # 此处应有格式化输出
                    count = count + 1
                    if(count == 5):  # 这里限制了只显示5条结果，可以自己设置
                        break
                except:
                    continue
    except :
        pass
    print("====================\r\n")
    print('Question: ' + question)
    if '不是' in question:
        print('**请注意此题为否定题,选计数最少的**')
    counts = []

    for i in range(len(choices)):
        counts.append(content.count(choices[i]))
        #print(choices[i] + " : " + str(counts[i]))
    output(choices, counts)


def output(choices, counts):
    counts = list(map(int, counts))
    #print(choices, counts)

    # 计数最高
    index_max = counts.index(max(counts))

    # 计数最少
    index_min = counts.index(min(counts))

    for i in range(len(choices)):
        print()
        if i == index_max:
            # 绿色为计数最高的答案
            print(Fore.GREEN +
                  "{0} : {1} ".format(choices[i], counts[i]) + Fore.RESET)
        elif i == index_min:
            # 红色为计数最低的答案
            print(Fore.MAGENTA +
                  "{0} : {1}".format(choices[i], counts[i]) + Fore.RESET)
        else:
            print("{0} : {1}".format(choices[i], counts[i]))
            
    if index_max == index_min:
        print(Fore.RED + "高低计数相等此方法失效！" + Fore.RESET)
        return


def search_choices(choices):

    for choice in choices:
        req = requests.get(url='http://www.baidu.com/s', params={'wd': choice})
        content = req.text
        # print(content)
        #counts = []

        print("=======  "+choice+"  ====================\r\n")
        results = process.page(content)
        #print (results)
        count = 0
        for result in results:
            result_str = ('{0}'.format(result.abstract))
            if "当前代码版本不予摘要" in result_str:
                continue
            else:
                try:
                    # print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
                    print(result_str.replace(u'\xa0', u' ')  + "\r\n")  # 此处应有格式化输出
                    count = count + 1
                    if(count == 2):  # 这里限制了只显示2条结果，可以自己设置
                        break
                except:
                    continue


def run_algorithm(al_num, question, choices):
    if al_num == 0:
        open_webbrowser(question)
    elif al_num == 1:
        open_webbrowser_count(question, choices)
    elif al_num == 2:
        count_base(question, choices)


if __name__ == '__main__':
    question = '新装修的房子通常哪种化学物质含量会比较高?'
    choices = ['甲醛', '苯', '甲醇']
    run_algorithm(1, question, choices)