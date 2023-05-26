import pycurl
import certifi
from io import BytesIO
from urllib.parse import urlencode
import json

## Create PycURL instance
c = pycurl.Curl()

## Define Options - Set URL we want to request
c.setopt(c.URL, 'https://admin-api-qa-1.horeker.dev/admin/auth/login')

# Setting POST Data + Encoding Data
post_body = {"email":"admin@mail.test","password":"admin1"}
post_data = urlencode(post_body)
c.setopt(c.POSTFIELDS, post_data)

## Setup buffer to recieve response
buffer = BytesIO()
c.setopt(c.WRITEDATA, buffer)

## Setup SSL certificates
c.setopt(c.CAINFO, certifi.where())

## Make Request
c.perform()

## Close Connection
c.close()

## Retrieve the content BytesIO & Decode
body = buffer.getvalue()
#print(body.decode('iso-8859-1'))
#a=body.decode('iso-8859-1')
json_object = json.loads(body.decode('iso-8859-1'))
#print(json.dumps(json_object, indent=2))
access_token = json_object['access_token']
#print(access_token)

post_body = {"email":"admin@mail.test","password":"admin1"}
