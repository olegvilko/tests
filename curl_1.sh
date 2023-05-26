#!/bin/bash

ex_1(){
curl 'https://admin-api-qa-1.horeker.dev/admin/auth/login' -X POST \
-H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0' \
-H 'Accept: application/json' -H 'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3' \
-H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/json;' -H 'Content-Language: uk' \
-H 'Origin: https://billing-qa-1.horeker.dev' -H 'Connection: keep-alive' \
-H 'Referer: https://billing-qa-1.horeker.dev/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: same-site' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'TE: trailers' \
--data-raw '{"email":"admin@mail.test","password":"admin1"}'
}

ex_1
