import requests, json
from urllib.parse import urlparse, parse_qs
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(wait=wait_fixed(60), stop=stop_after_attempt(5))
def get_bing_img_info():
    info = json.loads(requests.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-cn').content)['images'][0]
    print(info)
    return info

def get_img_name(url):
    try:
        qs = parse_qs(urlparse(url).query)
        return qs['id'][0]
    except:
        return ''

if __name__ == '__main__':
    get_img_name(get_bing_img_info()['url'])

