import re

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
		print(f"File Extension (File Type By Extension): {ext[-1::-1]}")
		return f"{ext[-1::-1]}"
	else:
		print(f"Couldn't Detect File Extension.")

name=input("Enter file name: ")
hl = 10
ext=extmatch(name)


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
	print(f"Header Bytes: {hex_bytes}")
	with open("magic.txt", "r") as f:
		lines = f.readlines()
	for i in lines:
		spl = i.split("|")
		reg = str(f"^{spl[0].lower()}")
		t = re.findall(reg, hex_str)
		if t:
			break
	if t:
		print(f"Magic Header Type: {spl[1]}")
		print(f"Description (Magic Header [{spl[1]}]): {spl[2].strip()}")
	else:
		print(f"Couldn't detect file type with magic headers.")
else:
	print("Failed to retrieve header bytes.")

