def generate_report(target, open_ports, vulnerabilities):
    report = f'"""\
# BugHunt-cli Scan Report

**Target:** {target}

## Open Ports

'

    if open_ports:
        for port in open_ports:
            report += f'- Port {port}\n'
    else:
        report += 'No open ports found.\n'

    report += ''
## Vulnerabilities

'

    if vulnerabilities:
        for vulnerability in vulnerabilities:
            report += f'- {vulnerability}\n'
    else:
        report += 'No vulnerabilities found.\n'

    report += '"""'
    return report
