import socket

def grab_banner(ip, port, timeout=2):
    """
    Attempt to grab the banner from a service running on a given IP and port.

    Args:
        ip (str): The IP address of the target.
        port (int): The port number to connect to.
        timeout (int): Timeout in seconds for the socket.

    Returns:
        str: The banner returned by the service, or an error message if failed. 
    """
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            
            # Connecct to the target service
            s.connect((ip, port))

            # Send a basic HTTP HEAD request (works on many services)
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")

            # Receive response banner (up to 1024 bytes)
            banner = s.recv(1024)
            
            # Decode bytes to string, ignoring decoding issues
            return banner.decode(errors="ignore").strip()
        
    except Exception as e:
        return f"Could not grad banner {e}"
        