# init original setting
n=41
k=3
ppl=range(n)

def josephus(n, k):
    # CORRECT
    person = []
    for i in range(0,n):
        person.append(i+1)
    ppl = n
    pos = 0
    
    while(ppl!=1):
        # Note: a%b=a when a<b, incredible line
        pos = (pos+k-1)%ppl

        person.pop(pos)
        ppl-=1
        
    pos = pos%ppl
    return person[pos]

ans = josephus(41,3)
print("safe position: ",ans)


