import requests
from bs4 import BeautifulSoup
from datetime import datetime


class NEWS:
    def __init__(self, url, tag, tag_class):
        self.url = url
        self.tag = tag
        self.tag_class = tag_class

    def requesting(self):
        res = requests.get(self.url, headers={"User-Agent": "INSERT HERE YOUR USER AGENT"})
        res.raise_for_status()
        return res

    def creating_bs_obj(self, res_obj):
        soup = BeautifulSoup(res_obj.content, features='html.parser')
        return soup

    def writing_data(self, soup_obj):
        file = open('INSERT HERE THE PATH', 'a')
        file.write(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + self.url + '\n')
        file.write('\n')
        for titles in soup_obj.find_all(self.tag, class_=self.tag_class):
            file.write(' '.join(titles.find_all(text=True)) + '\n')
        file.write('\n')
        file.close()
        print("News titles from " + self.url + " are now written on the file")
