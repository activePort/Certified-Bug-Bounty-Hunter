import whois
from colorama import Fore, Style, Back 

# WHOIS
def consulte_whois(domain_name):
    try:
        whois_info = whois.whois(domain_name)
        print(whois_info.text)
    except whois.parser.PywhoisError as e:
        print(f"Error al consultar WHOIS: {e}")



print()
domain_name = input(Fore.RED + Back.GREEN + "Enter the domain name to query:" + Style.RESET_ALL + " ")
consulte_whois(domain_name)