#!/usr/bin/env python
import subprocess
import optparse

def change_mac(interface, new_mac):
    if not interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")

    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change MAC address")
parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")
(options, args) = parser.parse_args()
interface = options.interface
new_mac = options.new_mac

change_mac(interface, new_mac)
