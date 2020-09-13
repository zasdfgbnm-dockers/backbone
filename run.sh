#!/bin/bash

mkdir -p /run/dbus
dbus-daemon --config-file=/usr/share/dbus-1/system.conf

sysctl -w net.ipv6.conf.all.forwarding=1

radvd -C /etc/radvd.conf
NetworkManager --no-daemon
