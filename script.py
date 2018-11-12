import json
import pymongo
from mitmproxy import ctx


def response(flow):
    print(flow.request.url)
    client = pymongo.MongoClient('mongodb://Bridi:anNBU7MD@localhost:27017/')
    db = client['taobao']
    collection = db['live']
    url = 'https://guide-acs.m.taobao.com/gw/mtop.taobao.iliad.comment.query.latest/1.0/'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        danmakus = data.get('data').get('comments')
        for danmaku in danmakus:
            name = danmaku.get('publisherNick')
            content = danmaku.get('content')
            data = {
                '昵称': name,
                '弹幕内容': content,
            }
            ctx.log.info(str(data))
            collection.update({'昵称': name, '弹幕内容': content}, {'$set': data}, True)