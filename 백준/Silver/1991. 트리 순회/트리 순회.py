import sys
n  = int(sys.stdin.readline().strip())
lc = ['.']*n
rc = ['.']*n
for _ in range(n):
    node, ln, rn = map(str, sys.stdin.readline().split())
    i = ord(node)-65
    lc[i] = ln
    rc[i] = rn

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    idx = ord(node)-65
    preorder(lc[idx])
    preorder(rc[idx])
    
def inorder(node):
    if node == '.':
        return
    idx = ord(node)-65
    inorder(lc[idx])
    print(node, end='')
    inorder(rc[idx])
    
def postorder(node):
    if node == '.':
        return
    idx = ord(node)-65
    postorder(lc[idx])
    postorder(rc[idx])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')