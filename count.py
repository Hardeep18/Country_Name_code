#!/usr/bin/python

import requests

uip= raw_input("User input: ")

resp1=requests.get('http://country.io/names.json')
a=resp1.json()

resp2=requests.get('http://country.io/capital.json')
b=resp2.json()

print uip + ' - ' + a[uip] + ' - ' + b[uip]
