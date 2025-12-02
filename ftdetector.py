import re
import hashlib
import requests
import json
import random

def main(file,num_bytes):
	with open(file,'rb') as f:
		lines = f.read(num_bytes)
		return lines

def extmatch(file):
	name = file[-1::-1]
	for i,t in enumerate(name):
		if t=='.':
			ext = name[0:i]
			break
	if t:
		print(f"[+] File Extension: {ext[-1::-1]}")
		return f"{ext[-1::-1]}"
	else:
		print(f"[-] File Extension: Unable to Detect File Extension")

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

name=input("Enter file name: ")
hl = 40
ext=extmatch(name)

sha256hash = sha256_file(name)
md5hash = md5_file(name)

header = main(name, hl)

if header:
	header_encoded = header
	to_hex = header_encoded.hex()
	hex_bytes = ""
	hex_str = str(to_hex)
	for i,x in enumerate(to_hex):
		if i!=0 and i!= 1 and i%2==0:
			hex_bytes += " "+ hex_str[i]
		else:
			hex_bytes += hex_str[i]
	print(f"[+] Header Bytes: {hex_bytes}")
	with open("magic.txt", "r") as f:
		lines = f.readlines()
	for i in lines:
		spl = i.split("|")
		reg = str(f"^{spl[0].lower()}")
		regex=''
		for m in reg:
			if m=='?':
				regex+='.'
			else:
				regex+=m
		t = re.findall(regex, hex_str)
		if t:
			break
	if sha256hash:
        	print("[+] SHA256 hash: ", sha256hash)
	if md5hash:
        	print("[+] MD5 hash: ", md5hash)
	if t:
		print(f"[+] Magic Header Type: {spl[1]}")
		print(f"[+] Description (Magic Header [{spl[1]}]): {spl[2].strip()}")
	else:
		print(f"[-] Couldn't detect file type with magic headers.")
else:
	print("[-] Failed to retrieve header bytes.")

def virustotal_check():
	url = f"https://www.virustotal.com/api/v3/files/{sha256hash}"
	api=""
	with open('virustotalapi.txt','r') as f:
		api = f.read().strip()
	if api=="":
		print(f"[-] You have not provided virustotal api key in virustotalapi.txt.")
		exit()
	headers = {"accept": "application/json", "X-Apikey": api}
	response = requests.get(url, headers=headers)
	data = response.json()
	print("[+] VirusTotal Information\n")
	print(json.dumps(data, indent=4))
	print("")
	vcheck = input("Do you want to save virustotal response in a file? (Y/n): ")
	if vcheck.lower()=='y' or vcheck == "1" or vcheck == "yes":
		print()
		fname = f"{name}-{random.randint(000000000000,999999999999)}.json"
		with open(fname, 'w') as f:
			w = f.write(json.dumps(data, indent=4))
			f.close()
		print(f"[+] Saved as {fname}")
print()
vcheck = input("Do you want to run a virustotal check? (Y/n): ")
if vcheck.lower()=='y' or vcheck == "1" or vcheck == "yes":
	print()
	virustotal_check()
