from core.rlccenv import RlccMininet, PcapAt
from mininet.log import setLogLevel
from core.topo import build_topo, multiPathTopo

setLogLevel('info')

XQUIC_PATH = '/home/seclee/xquic/xquic_forrlcc/build'

map_c_2_rlcc_flag = {
    'c1': "1001",
    'c2': "1002",
    'c3': "1003",
    'c4': "1004",
    'c5': "1005",
    'c6': "1006",
    'c7': "1007",
    'c8': "1008",
    'c9': "1009",
    'c10': "1010",
}

network = build_topo(len(map_c_2_rlcc_flag.keys()), max_paths_num=4, topo=multiPathTopo)

Exp = RlccMininet(map_c_2_rlcc_flag, network=network, root_switch="sw11", XQUIC_PATH=XQUIC_PATH)

sw1 = Exp.network.get(f"sw21")
print("------", sw1.intfs)

Exp.cli()