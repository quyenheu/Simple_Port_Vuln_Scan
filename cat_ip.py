#!/usr/bin/env python3

import sys

template = int(sys.argv[1])

with open('./result/nslookup.txt', 'r') as read, open('./result/range_ip.txt','a') as write:
   array = []
   for line in read:
      #hãy thử nslookup
      # mẫu 1 nghĩa là dòng ip sẽ trùng với lại address thứ 2
      if template == 1:
         if 'Address:' in line:
               array.append(line.strip())
      #mẫu 2 nghĩa là dòng ip sẽ ở dưới dòng address thứ 2
      elif template == 2:
         if 'Addresses:' in line:
               next_line = next(read, None)
               if next_line is not None:
                   array.append(next_line)

   if template == 1:
     for ip in range(1,len(array)):
       start_ip = array[ip].find('Address: ') + len('Address: ')
       ip_number = array[ip][start_ip:]
       ip_number = ip_number.strip()
       write.write(ip_number+'\n')
   elif template == 2:
     for ip in range(1, len(array)):
       write.write(array[ip].strip()+'\n')
