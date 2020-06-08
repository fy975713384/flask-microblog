import json
import requests
from flask import current_app
from flask_babel import _
from hashlib import md5


def translate(text, source_language, dest_language):
    if 'TRANSLATOR_APPID' not in current_app.config or not current_app.config['TRANSLATOR_APPID']:
        return _('Error: The translation service is not configured')
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    loads = {
        'q': text, 'from': source_language, 'to': dest_language,
        'appid': current_app.config['TRANSLATOR_APPID'], 'salt': 1,
        'sign': md5(f"{current_app.config['TRANSLATOR_APPID']}{text}1{current_app.config['TRANSLATOR_KEY']}".encode('utf-8')
                    ).hexdigest()
    }
    r = requests.post(url=url, headers=headers, data=loads)
    if r.status_code != 200:
        current_app.logger.debug(json.loads(r.content.decode('utf-8-sig')))
        return _('Error: The translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
