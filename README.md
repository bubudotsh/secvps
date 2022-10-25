# Sec-vps

Secure your server and create security audits on linux




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

Make audit

```
chmod +x secvps.sh
sudo ./secvps.sh -a
```

look mode : create an audit every x hour and send the report by email

```
chmod +x secvps.sh
sudo ./secvps.sh -l
```

look mode with pm2 (install pm2 first)

```
cd src/
sudo pm2 start pm2secvps.py --interpreter python3
```


## Support

For support, email bunelierpro@gmail.com or on discord : bubudotsh#2601


## Authors

- [@bubudotsh](https://www.github.com/bubudotsh)