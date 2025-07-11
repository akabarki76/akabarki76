
import argparse
from modules.port_scanner import scan_ports
from modules.vulnerability_scanner import check_sql_injection, check_xss
from modules.reporting import generate_report
from modules.recon import perform_reconnaissance
from modules.port_scanner import scan_ports
from modules.vulnerability_scanner import check_sql_injection, check_xss
from modules.reporting import generate_report

def main():
    parser = argparse.ArgumentParser(
        description='BugHunt-cli: AI-powered pentesting assistant.'
    )
    parser.add_argument(
        '--target',
        required=True,
        help='The target to scan (e.g., a domain or IP address).'
    )
    parser.add_argument(
        '--ports',
        nargs='+',
        type=int,
        default=range(1, 1025),
        help='A list of ports to scan (e.g., 80 443 8080). Defaults to 1-1024.'
    )
    parser.add_argument(
        '--scan-vulns',
        action='store_true',
        help='Run a basic vulnerability scan.'
    )
    parser.add_argument(
        '--recon',
        action='store_true',
        help='Run a reconnaissance scan.'
    )
    parser.add_argument(
        '--report',
        action='store_true',
        help='Generate a report of the findings.'
    )
    args = parser.parse_args()

    print('Welcome to BugHunt-cli!')
    print('=======================')
    print('Ethical Hacking Reminder: Always ensure you have explicit permission before scanning any target.')
    print('=======================')

    print(f'Scanning target: {args.target}')
    open_ports = scan_ports(args.target, args.ports)

    if open_ports:
        print('Open ports found:')
        for port in open_ports:
            print(f'  - Port {port} is open.')
    else:
        print('No open ports found or host is down.')

    vulnerabilities = []
    if args.scan_vulns:
        print('\nRunning vulnerability scan...')
        target_url = f'http://{args.target}'
        if check_sql_injection(target_url):
            vulnerabilities.append('Potential SQL Injection')
            print('  - Potential SQL Injection vulnerability found.')
        else:
            print('  - No SQL Injection vulnerability found.')

        if check_xss(target_url):
            vulnerabilities.append('Potential XSS')
            print('  - Potential XSS vulnerability found.')
        else:
            print('  - No XSS vulnerability found.')

    if args.recon:
        print('\nRunning reconnaissance scan...')
        perform_reconnaissance(args.target)

    if args.report:
        print('\nGenerating report...')
        report = generate_report(args.target, open_ports, vulnerabilities)
        print(report)

if __name__ == '__main__':
    main()
