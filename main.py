from os import system
import netifaces
def clearScreen():
	system("clear")

def mainMinu():
	print ("""[*] Network management program

[1] Network info
[2] Check ip address if available 
[3] Check connected devices
[4] Help
[5] Exit
	""")
clearScreen()
mainMinu()
ch=input(">> ")
while ( ch !="1" and ch !="2" and ch !="3" and ch!="4" and ch !="5"):
	clearScreen()
	mainMinu()
	print ("[!] chose 1 to 3 only !\n")
	ch=input(">> ")
while (True) :
	if (ch=="1"):
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
		input("\n[*] press enter to back to main minu")
		clearScreen()
		mainMinu()
		ch=input(">> ")

	elif (ch =="2"):

		hostname=input("enter IP address: ")
		response = system(f"ping -c 1 {hostname} > /dev/null")
		if response == 0:
			print ("\n" + hostname, 'is NOT available !')
		else:
			print ("\n" +  hostname, 'is available')
		input("\n[*] press enter to back to main minu")
		clearScreen()
		mainMinu()
		ch=input(">> ")

	elif (ch == "3"):
		ipaddr=input("Network ip address: ")
		submask=input("submask : ")

	elif (ch =="4"):
		print ("help coming soon ...")
		input("\n[*] press enter to back to main minu")
		clearScreen()
		mainMinu()
		ch=input(">> ")

	elif (ch == "5"):
		print("\nBYE\n")
		break


