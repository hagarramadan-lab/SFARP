#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch, Host
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

def create_network():
    net = Mininet(controller=RemoteController, switch=OVSSwitch, link=TCLink)

    print("*** Adding controllers")
    central = net.addController('c0', ip='127.0.0.1', port=6653)
    backup = net.addController('c1', ip='127.0.0.1', port=6654)
    domain1 = net.addController('c2', ip='127.0.0.1', port=6655)
    domain2 = net.addController('c3', ip='127.0.0.1', port=6656)

    print("*** Adding switches")
    sw1 = net.addSwitch('s1')
    sw2 = net.addSwitch('s2')
    sw3 = net.addSwitch('s3')
    sw4 = net.addSwitch('s4')

    print("*** Adding hosts")
    hosts = []
    for i in range(1, 21):
        host = net.addHost(f'h{i}', ip=f'10.0.0.{i}/24')
        hosts.append(host)

    print("*** Creating links")
    switches = [sw1, sw2, sw3, sw4]
    for i, host in enumerate(hosts):
        net.addLink(host, switches[i // 5])

    for sw in switches:
        net.addLink(sw, central)

    print("*** Starting network")
    net.build()
    for c in [central, backup, domain1, domain2]:
        c.start()
    for sw in switches:
        sw.start([central])

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
