#!/bin/bash

template="1"

if grep -q "1" "./result/template.txt"; then
   template="1"
else
   template="2"
fi

if [ -e "./target.txt" ]; then
   while IFS= read -r domain; do
      echo "running nslookup..."
      if [ -n "$domain" ]; then
         nslookup "$domain" > ./result/nslookup.txt
         python3 cat_ip.py "$template"
      fi
   done < "./target.txt"

   while IFS= read -r line; do
      echo "running nmap..."
      if [ -n "$line" ]; then
         nmap -vvv -p- "$line" >> ./result/nmap.txt
      fi
   done < "./result/range_ip.txt"

   python3 clean.py
   cat ./result/ip_port.txt | httpx -mc 200,403 >> ./result/live_ip.txt

   while IFS= read -r ip; do
       nuclei -u "$ip" >> ./result/check_vuln.txt
   done < "./result/live_ip.txt"
else
   echo "file not found"
fi

