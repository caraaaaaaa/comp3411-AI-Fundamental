import numpy as np
from fractions import Fraction
def laplace_error(l,i):
    k,n,N=len(l),max(l),sum(l)
    E=Fraction(f'{N-n+k-1}/{N+k}')
    print(f'Laplace error{i}: 1-({n}+1)/({N}+{k})={E}')
    return E
p,nodes,weights=np.array(input('parent node: ').split()).astype(np.int64),[],[]
s,N,Ep=sum(p),sum(p),laplace_error(p,0)
while s>0:
    node=np.array(input(f'child node{len(nodes)+1}: ').split()).astype(np.int64)
    weight=Fraction(f'{sum(node)}/{N}')
    weights.append(weight)
    nodes.append(laplace_error(node,len(nodes)+1))
    s-=sum(node)
Ec,string=sum([weights[i]*nodes[i] for i in range(len(nodes))]),'+'.join([f'{weights[i]}*{nodes[i]}' for i in range(len(nodes))])
if s<0:print('incorrect input, please check')
else:
    print(f'Ec: {string}={Ec}')
    if Ec<Ep:print(f'{Ec}(Ec)<{Ep}(Ep), do not prune off')
    else:print(f'{Ec}(Ec)>={Ep}(Ep), prune off')