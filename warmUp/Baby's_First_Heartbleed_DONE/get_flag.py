#!/usr/bin/python3
from pwn import *
from sys import argv
from re import findall

context.log_level = "critical"

try:
	c = connect(argv[1], int(argv[2]))
except:
	c = connect("challenge.nahamcon.com", 30700)
else:
	print("[!]Opps can't connect")

print("[*]Connected!....")
print("[*]Getting the flag....")

c.recvuntil(b":")
c.sendline(b"abcd")
c.recvuntil(b":")
c.sendline(b"1337")

data = c.recvuntil(b"TO")

flag = findall(b"flag{.*}", data)[0].decode()
print(flag)


