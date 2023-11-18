import whois
import subprocess
from colorama import Fore, Style, Back 

# WHOIS
def consulte_whois(domain_name):
    try:
        whois_info = whois.whois(domain_name)
        print(whois_info.text)
    except whois.parser.PywhoisError as e:
        print(f"Error al consultar WHOIS: {e}")

# DNS
def dig_all_records(domain_name):
    try:
        result = subprocess.check_output(["dig", domain_name, "ANY"], universal_newlines=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar dig: {e}")

print()
domain_name = input(Fore.RED + Back.GREEN + "Enter the domain name to query:" + Style.RESET_ALL + " ")
print()
print(Fore.RED + Back.GREEN + "### WHOIS ###" + Style.RESET_ALL)
consulte_whois(domain_name)
print(Fore.RED + Back.GREEN + "### DNS ###" + Style.RESET_ALL)
dig_all_records(domain_name)