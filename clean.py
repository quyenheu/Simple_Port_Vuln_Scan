#!/usr/bin/env python3

with open('./result/nmap.txt', 'r') as read, open('./result/ip_port.txt', 'w') as write:
   for line in read:
     if 'Discovered open' in line:
        port_start_index = line.find('port ') + len('port ')
        port_end_index = line.find('/')
        ip_index = line.find('on ') + len('on ')
        if port_start_index != -1 and port_end_index != -1 and ip_index != -1:
           port_number = line[port_start_index:port_end_index]
           ip_number = line[ip_index:]
           write.write('http://' + ip_number.strip() + ':' + port_number.strip() + '\n')
           write.write('https://'+ ip_number.strip() + ':' + port_number.strip() + '\n')
