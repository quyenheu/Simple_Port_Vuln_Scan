#!/bin/bash
echo "your target name(eg: example.com ):"
read domain

echo '' > ./result/template.txt

nslookup "$domain" > ./result/nslookup.txt
python3 template.py

if grep -q "1" "./result/template.txt"; then
   python3 cat_ip.py "1"
else
   python3 cat_ip.py "2"
fi

while IFS= read -r line; do
   if [ -n "$line" ]; then
      echo "$line   $domain" >> "/etc/hosts"
   fi
done < "./result/range_ip.txt"

echo '' > ./result/check_vuln.txt
echo '' > ./result/ip_port.txt
echo '' > ./result/live_ip.txt
echo '' > ./result/nmap.txt
echo '' > ./result/nslookup.txt
echo '' > ./result/range_ip.txt
chmod +x cat_ip.py
chmod +x clean.py
chmod +x template.py
chmod +x hackerga2101.sh

./hackerga2101.sh
