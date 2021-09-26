#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

res = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
json = res.json()
usd = json[0]
eur = json[1]
rur = json[2]
print("Курсы валют Приват Банка")
print("===================")
print(f"Доллар США.       Курс покупки {usd['buy']}. Курс продажи {usd['sale']}.")
print("===================")
print(f"Евро.             Курс покупки {eur['buy']}. Курс продажи {eur['sale']}.")
print("===================")
print(f"Российский рубль. Курс покупки {rur['buy']}. Курс продажи {rur['sale']}.")

