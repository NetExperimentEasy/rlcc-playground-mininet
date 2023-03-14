from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.util import info

from .utils import generate_random_paths_num

import sys


class baseTopo(Topo):
    "Simple topology with multiple envs(links)"
    """
                                  
            |-> root-eth0
            |      /-> "switch.intfs[2].name" : [tc]
    c1 --- sw1-eth2 --- ser1
            |
    c2 --- sw2 --- ser2
            |
    c3 --- sw3 --- ser3

    """

    def build(self, n, **_kwargs):

        # while use root-eth0, 10.0.0.1 cant be used, so set a useless client
        self.addHost('c0')

        switchlist = []
        for i in range(n):
            si, ci = self.addHost(f'ser{i+1}'), self.addHost(f'c{i+1}')
            swi = self.addSwitch(f'sw{i+1}')
            self.addLink(ci, swi)
            self.addLink(swi, si)
            switchlist.append(swi)

        for item in switchlist[1:]:
            self.addLink(switchlist[0], item)

class multiPathTopo(Topo):
    "Simple topology with multiple envs(multiple path)"

    """
                                  
    |-> root-eth0
    |
    |   --- c1 ---  ---
    |  /    |     \     \  
    sw11   sw12   sw13  ...
    |  \    |     /     / -> sw.eth2 -> "switch.intfs[2].name" : [tc]
    |   ---ser1---  ---
    |
    |   --- c2 ---  ---
    |  /    |     \     \ 
    sw21   sw22   sw23  ...
    |  \    |     /     /
    |   ---ser2---  ---
    |
    |
    ...

    """

    def build(self, n, paths_num=None, max_paths_num=None, **_kwargs):
        """
        n : number of envs
        paths_num : number of paths in each env
        max_paths_num : max number of paths in each env

        if you set paths_num, each env will consist of [paths_num] paths,
        otherwise, you should set max_paths_num, each env will generate random
        nums paths. 
        """

        # while use root-eth0, 10.0.0.1 cant be used, so set a useless client
        self.addHost('c0')

        if not paths_num and not max_paths_num:
            info("you should set at least paths_num or max_paths_num")
            sys.exit(0)

        switch1list = [] # conect each swi1 to sw11, then attach sw1 with rootNS
        for i in range(n):
            if max_paths_num:
                paths_num = generate_random_paths_num(2, max_paths_num)
            si, ci = self.addHost(f'ser{i+1}'), self.addHost(f'c{i+1}')

            for j in range(paths_num):
                swi = self.addSwitch(f'sw{i+1}{j+1}')
                self.addLink(ci, swi)
                self.addLink(swi, si)
                if j == 1:
                    switch1list.append(swi)

        for item in switch1list[1:]:
            self.addLink(switch1list[0], item) # 将sw11与每一个sw[i]1相连

def build_topo(n, paths_num=None, max_paths_num=None, topo=baseTopo):
    """
    general args:
    n : number of envs

    multiPathTopo args:
    paths_num : number of path in each env
    max_paths_num : max number of paths in each env

    if you set paths_num, each env will consist of [paths_num] paths,
    otherwise, you should set max_paths_num, each env will generate random
    nums paths. 
    """

    if topo == baseTopo:
        t = topo(n)
    if topo == multiPathTopo:
        t = topo(n, paths_num, max_paths_num)
    return Mininet(t, waitConnected=True)


def runMultiLinkTopo():
    "Create and run multiple link network"
    topo = baseTopo(n=2)
    net = Mininet(topo=topo, link=TCLink, waitConnected=True)
    net.start()
    CLI(net)
    net.stop()

def runMultiPathLinkTopo():
    "Create and run multiple link network"
    topo = multiPathTopo(n=2, max_paths_num=3)
    net = Mininet(topo=topo, link=TCLink, waitConnected=True)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    # runMultiLinkTopo()
    runMultiPathLinkTopo()
