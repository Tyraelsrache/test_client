import requests
import base64

# Tutorial https://jdhao.github.io/2020/04/12/build_webapi_with_flask_s2/

url= 'http://192.168.178.79:8080/post_pic'

with open('test.jpg', 'rb') as f:
    im_b64 = base64.b64encode(f.read())

payload = {'id': '123', 'type': 'jpg', 'box': [0, 0, 100, 100], 'image': im_b64}

r = requests.post(url, data=payload)
print(r.json())