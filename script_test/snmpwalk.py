from pysnmp.hlapi import *

# Paramètres SNMPv3
user = UsmUserData(
    'user1', 
    authKey='miracle2022', authProtocol=usmHMACSHAAuthProtocol,
    privKey='power2022', privProtocol=usmAesCfb128Protocol
)

# Paramètres de la cible SNMP
target = UdpTransportTarget(('192.168.140.140', 161))

# Définir l'OID de départ pour le snmpwalk
start_oid = ObjectType(ObjectIdentity('SNMPv2-MIB', 'system'))

for (errorIndication, errorStatus, errorIndex, varBinds) in bulkCmd(
        SnmpEngine(),
        user,
        target,
        ContextData(),
        0, 25,  # NonRepeaters, MaxRepetitions
        start_oid
    ):
    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
            )
        )
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))

