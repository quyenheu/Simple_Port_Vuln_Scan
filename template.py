#!/usr/bin/env python3

found = False
with open('./result/nslookup.txt', 'r') as read, open('./result/template.txt', 'w') as write:
    for line in read:
        if 'Addresses' in line:
             write.write('2')
             found = True
with open('./result/template.txt', 'w') as write:
    if found == False:
       write.write('1')
