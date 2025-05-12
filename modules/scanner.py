import socket

def scan_ports(ip, ports, timeout=1):

    """ Scan a list of ports on a target IP address using TCP connection attempts.

    Args:
        ip (str): The target IP address to scan.
        ports (list): A list of integer port numbers to scan.
        timeout (int): Timeout in seconds for each connection attempt.

    Returns:
        list: A list of open ports that responded successfully. """
    
    open_ports = []
    print(f"\n[*] Scanning {ip} on ports: {ports}")

    for port in ports:
        try:

            # Create a TCP socket

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Set timeout so it doesn't hang too long per port
                s.settimeout(timeout)

                # Attempt to connect to the target port
                result = s.connect_ex((ip, port))
                
                # connect_ex returns 0 if the port is open
                if result == 0:
                    print (f"[+] Port {port} is OPEN")
                    open_ports.append(port)
        except Exception as e:
            # Catch any errors and print them (i.e., invalid IP)
            print(f"[!] Error scanning port {port}: {e}")
    return open_ports               