import requests
import webtech
import whois
def check_server_type(domain):
    try:
        response = requests.get(f"http://{domain}")
        if response.status_code == 200:
            server_type = response.headers.get('Server')
            if server_type:
                print(f"The server at {domain} is running {server_type}.")
            else:
                print(f"The server at {domain} is running HTTP, but the server type could not be determined.")
        else:
                w = whois.whois(domain)
                server_type = w.get('name_servers', None)
                if server_type:
                    print(f"The server at {domain} is running {server_type}.")
                else:
                    print(f"The server at {domain} is not running HTTP, but the server type could not be determined.")
    except requests.exceptions.RequestException:
        print(f"Could not connect to {domain}. Please check the domain name or your internet connection.")

domain_name = input("Enter a domain name: ")

check_server_type(domain_name)

def web_tech():
    wt = webtech.WebTech(options={'json': True})
    try:
        report = wt.start_from_url(f"https://{domain_name}")
        print(report)
    except webtech.utils.ConnectionException:
        print("Connection error")
        
web_tech()