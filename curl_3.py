import pycurl
import certifi
from io import BytesIO
from urllib.parse import urlencode
import json
import subprocess

## Create PycURL instance
c = pycurl.Curl()
c.setopt(c.URL, 'https://admin-api-qa-1.horeker.dev/admin/auth/login')
post_body = {"email":"admin@mail.test","password":"admin1"}
post_data = urlencode(post_body)
c.setopt(c.POSTFIELDS, post_data)
buffer = BytesIO()
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.perform()
c.close()
body = buffer.getvalue()
json_object = json.loads(body.decode('iso-8859-1'))
access_token = json_object['access_token']
#print(access_token)

subprocess.call(['./curl_2.sh_2', access_token])