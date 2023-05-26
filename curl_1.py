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

c.setopt(c.URL, 'https://admin-api-qa-1.horeker.dev/admin/tariffs')
post_body = {"price_month":0,"price_year":0,"permissions":[{"id":6,"active":true},{"id":7,"active":true},{"id":8,"active":true},{"id":9,"active":true},{"id":10,"active":true},{"id":11,"active":true},{"id":12,"active":true},{"id":13,"active":true},{"id":14,"active":true},{"id":15,"active":true},{"id":16,"active":true},{"id":17,"active":true},{"id":18,"active":true},{"id":19,"active":true},{"id":20,"active":true},{"id":21,"active":true},{"id":22,"active":true},{"id":23,"active":true},{"id":24,"active":true},{"id":25,"active":true},{"id":26,"active":true},{"id":27,"active":true},{"id":28,"active":true},{"id":29,"active":true},{"id":30,"active":true},{"id":130,"active":true},{"id":31,"active":true},{"id":32,"active":true},{"id":33,"active":true},{"id":36,"active":true},{"id":37,"active":true},{"id":38,"active":true},{"id":39,"active":true},{"id":40,"active":true},{"id":41,"active":true},{"id":45,"active":true},{"id":46,"active":true},{"id":47,"active":true},{"id":42,"active":true},{"id":43,"active":true},{"id":44,"active":true},{"id":48,"active":true},{"id":49,"active":true},{"id":50,"active":true},{"id":51,"active":true},{"id":52,"active":true},{"id":34,"active":true},{"id":35,"active":true},{"id":131,"active":true},{"id":132,"active":true},{"id":133,"active":true},{"id":134,"active":true},{"id":135,"active":true},{"id":136,"active":true},{"id":137,"active":true},{"id":53,"active":true},{"id":54,"active":true},{"id":55,"active":true},{"id":56,"active":true},{"id":57,"active":true},{"id":58,"active":true},{"id":59,"active":true},{"id":60,"active":true},{"id":61,"active":true},{"id":62,"active":true},{"id":63,"active":true},{"id":64,"active":true},{"id":65,"active":true},{"id":66,"active":true},{"id":67,"active":true},{"id":68,"active":true},{"id":69,"active":true},{"id":70,"active":true},{"id":71,"active":true},{"id":72,"active":true},{"id":73,"active":true},{"id":74,"active":true},{"id":75,"active":true},{"id":76,"active":true},{"id":77,"active":true},{"id":78,"active":true},{"id":79,"active":true},{"id":80,"active":true},{"id":81,"active":true},{"id":82,"active":true},{"id":83,"active":true},{"id":84,"active":true},{"id":85,"active":true},{"id":86,"active":true},{"id":87,"active":true},{"id":88,"active":true},{"id":89,"active":true},{"id":90,"active":true},{"id":91,"active":true},{"id":92,"active":true},{"id":93,"active":true},{"id":94,"active":true},{"id":95,"active":true},{"id":96,"active":true},{"id":97,"active":true},{"id":98,"active":true},{"id":99,"active":true},{"id":100,"active":true},{"id":101,"active":true},{"id":102,"active":true},{"id":103,"active":true},{"id":104,"active":true},{"id":105,"active":true},{"id":106,"active":true},{"id":107,"active":true},{"id":108,"active":true},{"id":109,"active":true},{"id":110,"active":true},{"id":111,"active":true},{"id":112,"active":true},{"id":113,"active":true},{"id":114,"active":true},{"id":115,"active":true},{"id":116,"active":true},{"id":117,"active":true},{"id":118,"active":true},{"id":119,"active":true},{"id":123,"active":true},{"id":120,"active":true},{"id":121,"active":true},{"id":122,"active":true},{"id":124,"active":true},{"id":125,"active":true},{"id":126,"active":true},{"id":127,"active":true},{"id":128,"active":true},{"id":129,"active":true}],"active":true,"ru":{"description":"\u0431\u0435\u0437 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439","name":"\u043a\u043b\u0430\u0441\u0442\u0435\u0440","subtitle":"\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0432 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0435"},"uk":{"description":"\u0431\u0435\u0437 \u043e\u0431\u043c\u0435\u0436\u0435\u043d\u044c","name":"\u043a\u043b\u0430\u0441\u0442\u0435\u0440","subtitle":"\u0432\u0438\u043a\u043e\u0440\u0438\u0441\u0442\u043e\u0432\u0443\u0454\u0442\u044c\u0441\u044f \u0432 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0456"},"en":{"description":"without restrictions","name":"cluster","subtitle":"is used in a cluster"}}
c.setopt(pycurl.HTTPHEADER, ['Authorization: Bearer 26lhbngfsybdayabz6afrc6dcd', 'Content-Type: application/json'])
c.perform()