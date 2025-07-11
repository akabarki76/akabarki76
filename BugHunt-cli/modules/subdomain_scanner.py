
import requests

def enumerate_subdomains(domain):
    subdomains = []
    wordlist = ['www', 'mail', 'ftp', 'localhost', 'test']  # Simple wordlist
    for sub in wordlist:
        subdomain = f'http://{sub}.{domain}'
        try:
            requests.get(subdomain)
            subdomains.append(subdomain)
        except requests.ConnectionError:
            pass
    return subdomains
