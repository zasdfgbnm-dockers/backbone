#!/bin/bash

mkdir -p /run/dbus
dbus-daemon --config-file=/usr/share/dbus-1/system.conf

radvd
NetworkManager --no-daemon