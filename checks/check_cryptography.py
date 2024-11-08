import ssl
import socket
from utils.logger import log

def check_ssl_certificate(host):
    """Check SSL/TLS configuration of a host."""
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
    conn.settimeout(3.0)
    
    try:
        conn.connect((host, 443))
        ssl_info = conn.getpeercert()
        return ssl_info
    except Exception as e:
        log(f"SSL check failed for {host}: {e}", "error")
        return None

def run_check():
    log("Running cryptographic health check...")
    print("Enter a domain to check for SSL/TLS health:")
    domain = input("Domain: ")
    ssl_info = check_ssl_certificate(domain)
    
    if ssl_info:
        print(f"SSL Certificate Info for {domain}: {ssl_info}")
        log(f"SSL Certificate for {domain}: {ssl_info}")
    else:
        print(f"SSL check failed for {domain}.")
        log(f"SSL check failed for {domain}.", "error")
