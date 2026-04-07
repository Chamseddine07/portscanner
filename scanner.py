import socket

PORT_NAMES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

target = input("Enter IP or hostname to scan: ")
ip = socket.gethostbyname(target)  # hostname resolution
print(f"Scanning {target} ({ip})\n")

for port in PORT_NAMES:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    status = s.connect_ex((ip, port))

    if status == 0:
        print(f"{port} IS OPEN. SERVICE: {PORT_NAMES[port]}")
    else:
        print(f"{port} IS CLOSED. SERVICE: {PORT_NAMES[port]}")

    s.close()