# network_tool

* Network info
* Check ip address if available 
* Check connected devices

# app info
* python version : 3.9.2
* creator : ahmad Nueirat
* github : @ahmadner
* email: ahmadmnueirat@gmail.com
* instagram : ahmad.ner_

# python libraries

1. os `from os import system`
2. netifaces `import netifaces`

# parts of code

1. get network informations
```python
count = 1
interfacesList = netifaces.interfaces()
clearScreen()
print("[*] chose interface number\n")
for interface in interfacesList:
	print(f"[{count}] {interface}")
	count+=1
subCh=input("\n>> ")
if (subCh <"1" or subCh>str(count-1)):
	input(f"\n[!] out of range, number from 1 to {count-1}")
	continue
else:
	netifaces.ifaddresses(f"{interfacesList[int(subCh)-1]}")
try:
	ip = netifaces.ifaddresses(f'{interfacesList[int(subCh)-1]}')[netifaces.AF_INET][0]["addr"]
except:
	ip = "No ip address for this interface"
print (f"ip address: {ip}")
``` 


2. Check ip address if available  
```python
hostname=input("enter IP address: ")
response = system(f"ping -c 1 {hostname} > /dev/null")
if response == 0:
	print ("\n" + hostname, 'is NOT available !')
else:
	print ("\n" +  hostname, 'is available')
```

3. Check connected devices
```python
#soon ...
```
