/* dfam.p4 - Dynamic Flow Analysis Module (DFAM)
   Detects flooding & ARP spoofing using LCST structure
*/

#include <core.p4>

const bit<16> TYPE_IPV4 = 0x0800;
const bit<16> TYPE_ARP  = 0x0806;

header ethernet_t {
    mac_addr dst_addr;
    mac_addr src_addr;
    bit<16>  eth_type;
}

header arp_t {
    bit<16> htype;
    bit<16> ptype;
    bit<8>  hlen;
    bit<8>  plen;
    bit<16> oper;
    mac_addr sha;
    ip4_addr spa;
    mac_addr tha;
    ip4_addr tpa;
}

struct headers {
    ethernet_t ethernet;
    arp_t arp;
}

parser MyParser(packet_in pkt,
                out headers hdr) {
    state start {
        pkt.extract(hdr.ethernet);
        transition select(hdr.ethernet.eth_type) {
            TYPE_ARP: parse_arp;
            default: accept;
        }
    }

    state parse_arp {
        pkt.extract(hdr.arp);
        transition accept;
    }
}

control MyIngress(...) {
    /* Match-action table placeholders */
    action drop() {
        mark_to_drop();
    }

    table detect_arp_spoof {
        key = {
            hdr.arp.sha: exact;
            hdr.arp.spa: exact;
        }
        actions = {
            drop;
            NoAction;
        }
        size = 1024;
    }

    apply {
        if (hdr.ethernet.eth_type == TYPE_ARP) {
            detect_arp_spoof.apply();
        }
    }
}
