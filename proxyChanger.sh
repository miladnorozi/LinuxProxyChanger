#!/bin/bash

state=$(gsettings get org.gnome.system.proxy mode)
if [ $state == "'none'" ]; then
	gsettings set org.gnome.system.proxy mode 'manual'
fi
proxy_host="176.105.199.19"
proxy_port=":52024"
proxy_string="176.105.199.19:52024"
export HTTP_PROXY=$proxy_string
export http_proxy=$proxy_string

gsettings set org.gnome.system.proxy.http host "'$proxy_host'";
gsettings set org.gnome.system.proxy.http port "'$proxy_port'";

apt_conf_proxy="Acquire::http::Proxy \"$proxy_string\""

echo "$apt_conf_proxy" | sudo tee /etc/apt/apt.conf.d/proxy > /dev/null
