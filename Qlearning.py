s1a1,s1a2,s2a1,s2a2,r=[float(x) for x in input('input R(S1,a2),R(S1,a2),R(S2,a1),R(S2,a2),discount factor: ').split()]
cases={(s1a1/(1-r),s2a2+s1a1*r/(1-r)):'a1 a2',(s1a1/(1-r),s2a1/(1-r)):'a1 a1',((s1a2+s2a2*r)/(1-r*r),(s2a2+s1a2*r)/(1-r*r)):'a2 a2',(s1a2+s2a1*r/(1-r),s2a1/(1-r)):'a2 a1'}
case=max(cases.keys())
pi=cases[case]
if pi=='a1 a2':
    qs1a1=case[0]
    qs1a2=s1a2+case[1]*r
    qs2a1=s2a1+case[1]*r
    qs2a2=case[1]

elif pi=='a1 a1':
    qs1a1=case[0]
    qs1a2=s1a2+case[1]*r
    qs2a1=case[1]
    qs2a2=s2a2+case[0]*r
    
elif pi=='a2 a2':
    qs1a1=s1a1+case[0]*r
    qs1a2=case[0]
    qs2a1=s2a1+case[1]*r
    qs2a2=case[1]
    
elif pi=='a2 a1':
    qs1a1=s1a1+case[0]*r
    qs1a2=case[0]
    qs2a1=case[1]
    qs2a2=s2a2+case[0]*r

print(f'pi = {pi}\nQ(S1,a1)={qs1a1:0.2f}\nQ(S1,a2)={qs1a2:0.2f}\nQ(S2,a1)={qs2a1:0.2f}\nQ(S2,a2)={qs2a2:0.2f}')