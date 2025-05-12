import socket
import threading

# Shared list for open ports
open_ports = []
lock = threading.Lock()

def scan_port(ip, port, timeout=1):
    """
    Scan a single port on a target IP address using a TCP connection.

    Args:
        ip (str): Target IP address.
        port (int): Port number to scan.
        timeout (int): Socket timeout in seconds.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                with lock:
                    print(f"[+] Port {port} is OPEN")
                    open_ports.append(port)
    except Exception as e:
        pass  # You can optionally log or print errors

def scan_ports(ip, ports, timeout=1):
    """
    Scan multiple ports using threading.

    Args:
        ip (str): Target IP address.
        ports (list): List of ports to scan.
        timeout (int): Socket timeout in seconds.

    Returns:
        list: Open ports detected on the target IP.
    """
    global open_ports
    open_ports = []

    print(f"\n[*] Scanning {ip} on ports: {ports}")

    threads = []

    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port, timeout))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return open_ports