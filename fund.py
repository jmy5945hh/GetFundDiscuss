# -*- coding: utf-8 -*-     
import re
import requests
import json
import collections

print 'Go!'

def get_jijinba_review(page_url, time_after, target_id = ''):

    print 'Handling page: {}'.format(page_url)
    
    r = requests.get(page_url)
    text = r.text.encode('utf-8')
    #print text
    id_pattern = re.compile(r'(?<=<div class="zwli clearfix" id=")(\w+)(?:" data-huifuid=")(\d+)(?:" data-huifuuid=")(\d{0,20})')
    name_pattern = re.compile(r'(?<=<div class="zwlianame"><strong>).+(?=</\w+></strong>：</div>)')
    content_pattern = re.compile(r'(?<=<div class="zwlitext">).+(?=</div>)')
    time_pattern = re.compile(r'(?<=<div class="zwlitxb">).+(?=</div>)')

    all_name = name_pattern.findall(text)
    all_content = content_pattern.findall(text)
    all_time = time_pattern.findall(text)

    for i in range(len(all_time)):

        if target_id != '':
            if target_id not in all_name[i]:
                continue

        time = all_time[i].replace(' ','')
        time = time.replace('-', '')
        time = time.replace(':', '')

        if int(time) < time_after:
            continue
        
        if all_name[i].find('回复') != -1:
            name1_pattern = re.compile(r'(?<=>).+(?=</\w+></strong>)')
            
            names = all_name[i].split('回复')
            name1 = name1_pattern.search(names[0])
            name2 = names[1].split('>')[-1]
            print name1.group(), ' 回复 ', \
                  name2.decode('utf-8', 'ignore'),
        else:
            name0 = all_name[i].split('>')[-1]
            print name0.decode('utf-8', 'ignore'),

        
        print all_time[i]

        contents = all_content[i].split('<br>')
        for j in range(len(contents)):
            print ' ', contents[j].decode('utf-8', 'ignore')

        print '*************************************************'


for i in range(10):
    time = 20150317000000
    page_url_wang = r'http://jijinba.eastmoney.com/news,110026,107355269,d_{}.html'.format(10-i)
    get_jijinba_review(page_url_wang, time, '创业板专业户1600')
    page_url_shan = r'http://jijinba.eastmoney.com/news,740001,115878344,d_{}.html'.format(10-i)
    get_jijinba_review(page_url_shan, time, '山人I')
    page_url_don = r'http://jijinba.eastmoney.com/news,519189,115972832,d_{}.html'.format(10-i)
    get_jijinba_review(page_url_don, time)
        
