import numpy as np

def entropy(L,i):
    l=[_ for _ in L/sum(L) if _]
    E=np.sum(-np.log2(l)*l)
    print(f'Entropy{i}: {E:0.3F}')
    return E
p,nodes,weights=np.array(input('parent node: ').split()).astype(np.int64),[],[]
s,N,Ep=sum(p),sum(p),entropy(p,0)
while s>0:
    node=np.array(input(f'child node{len(nodes)+1}: ').split()).astype(np.int64)
    weight=sum(node)/N
    weights.append(weight)
    nodes.append(entropy(node,len(nodes)+1))
    s-=sum(node)
Ec=sum([weights[i]*nodes[i] for i in range(len(nodes))])
if s<0:print('incorrect input, please check')
else:print(f'Ec: {Ec:0.3f}, Information gain: {Ep:0.3f}-{Ec:0.3f}={Ep-Ec:0.3f}')