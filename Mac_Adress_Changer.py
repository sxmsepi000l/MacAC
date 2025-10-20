#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i" , "--interface", dest="interface" , help="Interface to change its MAC adress")
parser.add_option("-m" , "--mac", dest="new_mac" , help="New MAC adress")

(options, arguments) = parser.parse_args()

print("HALLO SCRIPT MADE BY ALSHABO0001")
print("------------------------------------")
print("YOUR CURRENT MAC ADRESS")
print("------------------------------------")

subprocess.call("ifconfig -a | grep -ioE '([a-z0-9]{2}:){5}..'", shell=True)
print("------------------------------------")

print("Enter The Interface ID")
subprocess.call("ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'", shell=True)
print("------------------------------------")

# interface = options.interface
# new_mac = options.new_mac
interface = input("[+] interface >")
new_mac = input("[+] Enter The New MAC Address >")
current_mac = subprocess.call("ifconfig -a | grep -ioE '([a-z0-9]{2}:){5}..'", shell=True)
# ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'
print("[+] Changing Mac Adress for " + interface  )
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
print("YOUR NEW MAC IS ")
subprocess.call("ifconfig -a | grep -ioE '([a-z0-9]{2}:){5}..'", shell=True)
print("THANK YOU PAPI SHABI")

