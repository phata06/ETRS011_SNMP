# https://makina-corpus.com/python/initiation-snmp-avec-python-pysnmp-partie-2-utilisation-de-la-librairie

from pysnmp.hlapi import *

## Les commandes si elles étaient lancé sur un terminale :
# $ snmpget -v2c -c passprojet 192.168.176.2 sysLocation.0 sysDescr.0
# $ snmpget -v3 -l authPriv -u user1 -a SHA -A miracle2022 -x AES -X power2022 192.168.140.140 sysLocation.0 sysDescr.0

# partie data pour les OID sysLocation.0 sysDescr.0
data = (
  ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0)), 
  ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0)),
  ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
)

# SNMP v2c
gv2 = getCmd(SnmpEngine()
           , CommunityData('passprojet', mpModel=1)
           , UdpTransportTarget(('192.168.176.2', 161))
           , ContextData()
           , *data)

# SNMP v3
gv3 = getCmd(SnmpEngine()
           , UsmUserData("user1"
            , authProtocol=usmHMACSHAAuthProtocol
            , authKey="miracle2022"
            , privProtocol=usmAesCfb128Protocol
            , privKey="power2022" )
           , UdpTransportTarget(('192.168.140.140', 161))
           , ContextData()
           , *data)

errorIndication, errorStatus, errorIndex, varBinds = next(gv2)
#errorIndication, errorStatus, errorIndex, varBinds = next(gv3)

# code erreur
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (
                         errorStatus.prettyPrint(),
                         errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
                       )

          )
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
