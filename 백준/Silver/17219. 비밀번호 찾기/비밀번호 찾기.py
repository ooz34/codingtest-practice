import sys
n, m = map(int, sys.stdin.readline().split())
site_pwd = {}
for _ in range(n):
    site, pwd = sys.stdin.readline().split()
    site_pwd[site] = pwd
for _ in range(m):
    print(site_pwd[sys.stdin.readline().strip()])