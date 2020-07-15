import protocols as prt

bgp_protocol = prt.Protocols(prt.Types.BGP, prt.Format.BIRD_1_x)
#bgp_protocol.create_protocol()
bgp_protocol.list_protocol()
