import requests
from bs4 import BeautifulSoup
class KBA:
    def __init__(self,User_Agent='Kelime Bulucu API Wrapper'):
        self.Url = 'https://kelimeler.net/makine/kelimebul'
        self.Session = requests.Session()
        self.Session.headers['User-Agent'] = User_Agent
    def KelimeBul(self,Kelime,Baglam='',h=53417):
        Data = {'Harfler':Kelime,'Baglam':Baglam,'h':h}
        Response = requests.post(self.Url,data=Data)
        Resp_Text = Response.text
        soup = BeautifulSoup(Resp_Text,'html.parser')
        return (match.contents[0] for match in soup.find_all('a'))
