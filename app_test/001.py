import threading
from queue import Queue
import requests
import json
import time
import pdfkit




class LaGou_spider():
    def __init__(self):
        self.url = 'https://gate.lagou.com/v1/neirong/kaiwu/getCourseLessons?courseId=17'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Cookie': '1a7c64d4612ce999b30d28e05ca05123eb8d7fdf80442d9e6343ea6a7d3593af',
            'Referer': 'https://kaiwu.lagou.com/course/courseInfo.htm?courseId=17',
            'Origin': 'https://kaiwu.lagou.com',
            'Sec-fetch-dest': 'empty',
            'Sec-fetch-mode': 'cors',
            'Sec-fetch-site': 'same-site',
            'x-l-req-header': '{deviceType:1}'}
        self.textUrl='https://gate.lagou.com/v1/neirong/kaiwu/getCourseLessons?courseId=102 '  #发现课程文章html的请求url前面都是一样的最后的id不同而已
        self.queue = Queue()  # 初始化一个队列
        self.error_queue = Queue()

    def parse_one(self):
        """

        :return:获取文章html的url
        """
        # id_list=[]
        html = requests.get(url=self.url, headers=self.headers).text
        dit_message = json.loads(html)
        message_list = dit_message['content']['courseSectionList']
        # print(message_list)
        for message in message_list:
            for i in message['courseLessons']:
                true_url=self.textUrl+str(i['id'])
                self.queue.put(true_url)#文章的请求url


        return self.queue

    def get_html(self,true_url):
        """

        :return:返回一个Str 类型的html
        """
        html=requests.get(url=true_url,timeout=10,headers=self.headers).text
        dit_message = json.loads(html)
        str_html=str(dit_message['content']['textContent'])
        article_name=dit_message['content']['theme']
        self.htmltopdf(str_html,article_name)

    def htmltopdf(self,str_html,article_name):
        path_wk = r'D:\wkhtmltox-0.12.6-1.mxe-cross-win64\wkhtmltox\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wk)
        options = {
            'page-size': 'Letter',
            'encoding': 'UTF-8',
            'custom-header': [('Accept-Encoding', 'gzip')]
        }
        pdfkit.from_string(str_html,"{}.pdf".format(article_name),configuration=config,options=options)



    def thread_method(self, method, value):  # 创建线程方法
        thread = threading.Thread(target=method, args=value)
        return thread

    def main(self):

        thread_list = []
        true_url= self.parse_one()
        while not  true_url.empty():
            for i in range(10):  # 创建线程并启动
                if not true_url.empty():
                    m3u8 = true_url.get()
                    print(m3u8)
                    thread = self.thread_method(self.get_html, (m3u8,))
                    thread.start()
                    print(thread.getName() + '启动成功,{}'.format(m3u8))
                    thread_list.append(thread)
                else:
                    break
            while len(thread_list)!=0:
                for k in thread_list:
                    k.join()  # 回收线程
                    print('{}线程回收完毕'.format(k))
                    thread_list.remove(k)



run = LaGou_spider()
run.main()

