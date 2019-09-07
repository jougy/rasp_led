# rasp_led

Projeto para estudo de uso de sensores no Raspberry Pi  
  

## Instruções
### ver os ip's
```shell
ifconfig
netstat -nr
```
### fixar um ip
Edite o arquivo: `sudo nano /etc/dhcpcd.conf`  
Insira no início do arquivo:
```
interface wlan0
static ip_address=
static routers=
static domain_name_servers=$ROUTER_IP 8.8.8.8 8.8.4.4
```
Reinicie a máquina:
`sudo reboot`

### instalar dependências
```shell
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install mosquitto -y
sudo apt-get install mosquitto-clients -y
sudo apt install git-all
sudo python3 -m pip install paho-mqtt
sudo python3 -m pip install Flask
```
### configurar o mqtt  
Edite o arquivo:
`sudo nano /etc/mosquitto/mosquitto.conf`  
Apague a ultima linha e substitua por:
```
allow_anonymous false
password_file /etc/mosquitto/pwfile
listener 1883
```
Após editar o arquivo, configure o mosquitto:
```
sudo mosquitto_password -c /etc/mosquitto/pwfile [nome de usuario]
cat /etc/mosquitto/pwfile
```

