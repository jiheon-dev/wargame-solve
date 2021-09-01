from pwn import *
r = remote('host1.dreamhack.games', 16790)
r.interactive()