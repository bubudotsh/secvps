# Sec-vps

Secure your server and create security audits on linux

This script secures your Linux server:
- configuration of a firewall
- manage port connections with fail2ban
- create audits with Lynis

It also sends you a security audit report via email on a recurring basis

## Requirement

This script use python3, so you need to install python

## Installation and configuration

```
git clone https://github.com/bubudotsh/secvps.git
cd secvps
chmod +x setup.sh
sudo ./setup.sh
```

## Usage

Start normal

```
cd src/
sudo python3 secvps.py
```

Start with pm2

```
cd src/
sudo pm2 start pm2secvps.py --interpreter python3
```


## Support

For support, email bunelierpro@gmail.com or on discord : bubudotsh#2601


## Authors

- [@bubudotsh](https://www.github.com/bubudotsh)