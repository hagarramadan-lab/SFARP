def detect_arp_spoofing(arp_table):
    duplicate_mac_ip = {}
    mac_to_ip = {}

    for entry in arp_table:
        mac = entry['MAC']
        ip = entry['IP']
        if mac in mac_to_ip and mac_to_ip[mac] != ip:
            duplicate_mac_ip[mac] = [mac_to_ip[mac], ip]
        mac_to_ip[mac] = ip

    return duplicate_mac_ip
