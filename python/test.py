# -*- coding: utf-8 -*-
import datetime
import math
import User

name = '岩崎'
print('私の名前は' + name + 'です')

x = '私の名前は' + name + 'です'

x.format(name)

print(x)

num = 5 * 4
print(num)

num /= 2
print(num)

now = datetime.datetime.now()
print(now)

age = 20

if age >= 20:
    print('成人です')
else:
    print('未成年です')

device = 'windows'

if device == 'mac':
    print('使用OSはMACです')
else:
    if device == 'windows':
        print('使用OSはWINDOWSです')
    else:
        print('どちらでもありません')

kanto = {'東京' : '新宿区', '神奈川県' : '横浜市', '千葉県' : '千葉市', '栃木県' : '宇都宮市', '埼玉県' : 'さいたま市'}

print kanto['東京']

saitama = 'さいたま市'
for officelocation in kanto:
    if kanto[officelocation] == saitama:
        print(officelocation + 'の県庁所在地は' + kanto[officelocation] + 'です')

def tasizan(x, y):
    sum = x + y
    return sum

print(tasizan(1, 5))

def hello(name):
    greet = name + 'さんこんにちは'
    return greet

print(hello('岩崎'))

def calcTaxInPrice(price):
    return float(price * 1.1)

print(calcTaxInPrice(1000))

list = [1, 2, 3, 4, 5, 6, 7, 8]
list.pop(4)
print(list)

def is_price(price):
    amount = price * 1.1
    return int(amount)

print(is_price(1000))

a = 3.141592653589793

print(int(a))