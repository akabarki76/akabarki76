
import socket

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((target, port)) == 0:
                    open_ports.append(port)
        except socket.gaierror:
            print(f'Error: Hostname could not be resolved: {target}')
            return []
        except socket.error:
            print(f'Error: Could not connect to server.')
            return []
    return open_ports
