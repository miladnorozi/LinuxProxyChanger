#!/bin/bash

state=$(gsettings get org.gnome.system.proxy mode)

#set proxy setting to manual in gnome
if [ $state == "'none'" ]; then
	gsettings set org.gnome.system.proxy mode 'manual'
fi



getOkProxyFromFile () {
	filename="okProxy.txt"
  test=0
	while [ $test -lt 100 ]
	do
    filename="okProxy.txt"
    line=$(head -n 1 $filename)
    result=$(python proxyChecker.py $line)
    if [ $result -eq 1 ]; then
			sed -i '1d' okProxy.txt
      return 1
		else
			sed -i '1d' okProxy.txt
    fi
done
}
okProxyFile="okProxy.txt"
if [ -f "$okProxyFile" ]
then
	echo "file exists "
	getOkProxyFromFile
else
	python proxyGrabber.py
	sleep 30
	getOkProxyFromFile
fi

counter=0
proxy=$(echo $line | tr ":" "\n")
proxy_host=""
proxy_port=""
for addr in $proxy
do
	if [ $counter == 0 ]
	then
		proxy_host=$addr
		let "counter++"
	else
		proxy_port=$addr
	fi
done

proxy_string="$proxy_host:$proxy_port"
export HTTP_PROXY=$proxy_string
export http_proxy=$proxy_string

gsettings set org.gnome.system.proxy.http host "'$proxy_host'";
gsettings set org.gnome.system.proxy.http port "'$proxy_port'";

apt_conf_proxy="Acquire::http::Proxy \"$proxy_string\""

echo "$apt_conf_proxy" | sudo tee /etc/apt/apt.conf.d/proxy > /dev/null
