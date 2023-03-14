from core.rlccenv import RlccMininet, PcapAt
from core.topo import build_topo, baseTopo
from mininet.log import setLogLevel

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

topo = build_topo(len(map_c_2_rlcc_flag.keys()), topo=baseTopo)

Exp = RlccMininet(map_c_2_rlcc_flag, topo=topo, XQUIC_PATH=XQUIC_PATH)

# # Generate TLS key
# c1 = Exp.topo.get("c1")
# cmd_at(c1, generate_xquic_tls)

Exp.run_train("random")
