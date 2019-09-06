# rasp_led

Projeto para estudo de uso de sensores no Raspberry Pi


=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
------------Instruções-----------------------
# ver os ip's
ifconfig
netstats -nr
# fixar um ip
sudo nano /etc/dhcpcd.conf
	interface wlan0
	static ip_address=
	static routers=
	static domain_name_servers=[router ip] 8.8.8.8 8.8.4.4
sudo reboot
# requer as seguintes instalações
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install mosquitto -y
sudo apt-get install mosquitto-clients -y
sudo apt install git-all
sudo python3 -m pip install paho-mqtt
sudo python3 -m pip install Flask
# configurar o mqtt
sudo nano /etc/mosquitto.conf
	apagar a ultima linha
	allow_anonymous false
	password_file /etc/mosquitto/pwfile
	listener 1883
sudo mosquitto_password -c /etc/mosquitto/pwfile [nome de usuario]
cat /etc/mosquitto/pwfile


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

