import requests, json
from urllib.parse import urlparse, parse_qs
from tenacity import retry, stop_after_attempt, wait_fixed
import time


@retry(wait=wait_fixed(60), stop=stop_after_attempt(5))
def get_bing_img_info():
    info = json.loads(requests.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-cn').content)['images'][0]
    print(info)
    return info


@retry(wait=wait_fixed(60), stop=stop_after_attempt(5))
def post_tg_channel(data):
    with open('tg_config.json', 'r') as f:
        config = json.load(f)
    url = f"https://api.telegram.org/bot{config['token']}/sendPhoto"
    payload = {
        "chat_id": config['chat_id'],
        "photo": f"https://cn.bing.com{data['url']}",
        "parse_mode": 'markdown',
        "caption": ''
    }
    caption = ''
    date = data['startdate']
    caption += f"图片信息: {data['copyright']}\n"
    caption += f"发布时间: {date[:4]}年{date[4:6]}月{date[-2:]}日\n"
    caption += f"内容详情: [点击访问]({data['copyrightlink']})\n"
    caption += f"原图下载: [点击下载](https://cn.bing.com{data['url']})"

    payload['caption'] = caption
    resp = requests.post(url, data=payload)


def dump_all():
    with open('tg_pub.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        data = eval(line)
        post_tg_channel(data)
        time.sleep(5)

if __name__ == '__main__':
    post_tg_channel(get_bing_img_info())
#    dump_all()     

      


