import subprocess
import optparse
import re

def get_arquments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--inter", dest="interface", help="Interface to change a MAC adress")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC adress")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please watch --help to instruction = interface")
    elif not options.new_mac:
        parser.error("[-] Please watch --help to instruction = new_mac")
    return options


def changer_mac(interface, new_mac):
    print(f"MAC adress: {interface}  to  {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    result_test = subprocess.check_output(["ifconfig", interface])
    mac_adress_research = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result_test))
    if mac_adress_research:
        return mac_adress_research.group(0)
    else:
        print("[-] Dont search MAC adress")


options = get_arquments()
current_mac = get_current_mac(options.interface)
print("Current MAC adress = " + str(current_mac))

changer_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("MAC adress sucessesfully change to " + current_mac)
else:
    print("MAC adress didn't change.")