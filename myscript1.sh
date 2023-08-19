#!/bin/bash

AUTH_LOG="/var/log/auth.log"
MAX_ATTEMPTS=3

while true; do
    failed_ips=$(grep 'Failed password' $AUTH_LOG | awk '{print $(NF-3)}' | sort | uniq -c | awk '$1 >= '$MAX_ATTEMPTS'>
    for ip in $failed_ips; do
        if ! iptables -C INPUT -s $ip -j DROP &>/dev/null; then
            iptables -A INPUT -s $ip -j DROP
            echo "Blocked IP address: $ip"
        fi
    done

    sleep 60
done
