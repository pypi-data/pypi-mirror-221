#!/usr/bin/python3

import sys
from rsclib.trafficshape import IPTables_Mangle_Rule

f = None
if len (sys.argv) > 1 :
    f = open (sys.argv [1])
IPTables_Mangle_Rule.parse_prerouting_rules (f, use_ipt = True)
for r in IPTables_Mangle_Rule.rules :
    print (r.as_tc_filter ('eth0', 'root', prio = 1))
