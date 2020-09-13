#!/usr/bin/python

import yaml
import uuid
import os

with open('args.yml') as f:
    args = yaml.load(f, yaml.CLoader)

# setup radvd
with open('radvd.conf') as f:
    text = f.read()
    text = text.format(**args)

with open('/etc/radvd.conf', 'w') as f:
    f.write(text)

os.umask(0o077)

# setup wireguard
with open('NetworkManager/system-connections/wg_backbone.nmconnection') as f:
    nmconnection = f.read()

with open('NetworkManager/system-connections/wg_template') as f:
    template = f.read()

wireguard_peers = ''
for peer in args['wireguard_peers']:
    wireguard_peers += template.format(**peer)
args['wireguard_peers'], wireguard_peers = wireguard_peers, args['wireguard_peers']

nmconnection = nmconnection.format(**args, uuid4=str(uuid.uuid4()))

with open('/etc/NetworkManager/system-connections/wg_backbone.nmconnection', 'w') as f:
    f.write(nmconnection)

# setup gre
with open('NetworkManager/system-connections/gretap_{name}.nmconnection') as f:
    nmconnection = f.read()

for peer in wireguard_peers:
    with open('/etc/NetworkManager/system-connections/gretap_{name}.nmconnection'.format(**peer), 'w') as f:
        f.write(nmconnection.format(**peer, uuid4=str(uuid.uuid4())))

# setup bridge
with open('NetworkManager/system-connections/bridge.nmconnection') as f:
    nmconnection = f.read()

with open('/etc/NetworkManager/system-connections/bridge.nmconnection', 'w') as f:
    f.write(nmconnection.format(uuid4=str(uuid.uuid4())))
