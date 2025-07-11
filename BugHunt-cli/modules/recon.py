
import whois
import dns.resolver
from modules.subdomain_scanner import enumerate_subdomains

def get_whois_info(domain):
    try:
        return whois.whois(domain)
    except whois.parser.PywhoisError:
        return None

def get_dns_records(domain):
    records = {}
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [str(rdata) for rdata in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            pass
    return records

def perform_reconnaissance(target):
    print('\n--- WHOIS Information ---')
    whois_info = get_whois_info(target)
    if whois_info:
        print(whois_info)
    else:
        print('No WHOIS information found.')

    print('\n--- DNS Records ---')
    dns_records = get_dns_records(target)
    if dns_records:
        for record_type, records in dns_records.items():
            print(f'  {record_type}:')
            for record in records:
                print(f'    {record}')
    else:
        print('No DNS records found.')

    print('\n--- Subdomain Enumeration ---')
    subdomains = enumerate_subdomains(target)
    if subdomains:
        for subdomain in subdomains:
            print(f'  - {subdomain}')
    else:
        print('No subdomains found.')
