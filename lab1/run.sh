#!/bin/bash

openrc
touch /run/openrc/softlevel
echo 'rc_provide="loopback net"' >> /etc/rc.conf
rc-service nginx start
sh