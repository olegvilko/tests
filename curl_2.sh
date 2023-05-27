#!/bin/bash
#source text.txt
token=$1

curl 'https://admin-api-qa-1.horeker.dev/admin/tariffs' -X POST \
-H 'Content-Type: application/json;' \
-H 'Authorization: Bearer '$token \
--data-raw $'{"price_month":0,"price_year":0,"ru":{"description":"\u0431\u0435\u0437 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439","name":"\u043a\u043b\u0430\u0441\u0442\u0435\u0440","subtitle":"\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0432 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0435"},"uk":{"description":"\u0431\u0435\u0437 \u043e\u0431\u043c\u0435\u0436\u0435\u043d\u044c","name":"\u043a\u043b\u0430\u0441\u0442\u0435\u0440","subtitle":"\u0432\u0438\u043a\u043e\u0440\u0438\u0441\u0442\u043e\u0432\u0443\u0454\u0442\u044c\u0441\u044f \u0432 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0456"},"en":{"description":"without restrictions","name":"cluster","subtitle":"is used in a cluster"}}'
