import socket


def get_ip_addresses(domain):
    try:
        ips = socket.getaddrinfo(domain, None)
        ip_addresses = set()
        for ip in ips:
            ip_addresses.add(ip[4][0])
        
        return ip_addresses
    
    except socket.gaierror as e:
        return f'Erro ao buscar informações sobre {domain}: {e}'



def main():
    domain = input('Enter a domain name: ')
    ips = get_ip_addresses(domain)

    if isinstance(ips, set):
        print(f"IP addresses for {domain}: {', '.join(ips)}")
    else:
        print(domain)


if __name__ == '__main__':
    main()