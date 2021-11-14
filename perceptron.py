num_examples,examples,Actions=int(input('How many examples: ')),[],{'Subtract':-1,'Add':1,'None':0}
for i in range(num_examples):
    example=[float(x) for x in input(f'input example {chr(97+i)}: ').split()]
    examples.append(example)
W,lr,start,Iteration,num_none=[float(w) for w in input('input initial weights: ').split()],float(input('input learning rate: ')),ord(input('start point: '))-97,0,0
while num_none-num_examples:
    Training_Example,X=chr(97+(Iteration+start)%num_examples),examples[(Iteration+start)%num_examples]
    Iteration+=1
    s=W[0]+sum([wi*xi for (wi,xi) in zip(W[1:],X[:-1])])
    if X[-1]<0 and s>=0: Action='Subtract'
    elif X[-1]>0 and s<0: Action='Add'
    else: Action='None'
    num_none=num_none+1 if Action=='None' else 0
    print(f"Iteration: {Iteration:>2}, Weights: {W}, Training Example: {Training_Example}, Xs: {X[:-1]}, Class: {'+' if X[-1]>0 else '-'}, s: {s:>+.1f}, Action: {Action:^8}")
    W=[W[0]+lr*Actions[Action]]+[wi+lr*Actions[Action]*xi for (wi,xi) in zip(W[1:],X[:-1])]