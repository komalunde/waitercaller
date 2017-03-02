import urllib2
import json

TOKEN = 'R_9498582d74fe45928d50912f6a8c6da2'
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:

    def shorten_url(self,longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = urllib2.urlopen(url).read()
            jr = json.load(response)
            return jr['data']['url']
        except Exception as e:
            print e