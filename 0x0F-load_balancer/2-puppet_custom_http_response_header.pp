#!/usr/bin/env bash
# Install and configure HAproxy on your lb-01 server.
# Requirements:
#   - Configure HAproxy so that it send traffic to web-01 and web-02
#   - Distribute requests using a roundrobin algorithm
#   - Make sure that HAproxy can be managed via an init script
#   - Make sure that your servers are configured with the right
#     hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.
#     If not, follow this tutorial.
#   - For your answer file, write a Bash script that configures a
#     new Ubuntu machine to respect above requirements

apt-get -y update
apt-get install -y haproxy

printf %s "
frontend husham35.tech
	bind *:80
	mode http
	defautl_backend techgist-backend

backend techgist-backend
	balance roundrobin
	option forwardfor
	server 414519-web-01 54.83.170.40 check
	server 414519-web-02 18.209.179.183 check
" >> /etc/haproxy/haproxy.cfg

printf %s "
ENABLED=1
" >> /etc/default/haproxy

service haproxy restart
