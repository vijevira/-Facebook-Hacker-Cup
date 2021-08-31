t=int(input())
file=open("consistency_chapter_1.txt","w")
for ii in range (1,t+1):
    s=input()
    vol="AEIOU"
    cons="BCDFGHJKLMNPQRSTVWXYZ"
    c={i:0 for i in cons}
    v={i:0 for i in vol}
    vc=0
    cc=0
    for i in s:
        if i in vol:
            v[i]+=1
            vc+=1
        else:
            c[i]+=1
            cc+=1
    mc=max(c.values())
    mv=max(v.values())
    fc=(cc-mc)*2+vc
    fv=(vc-mv)*2+cc
    ans=min(fc,fv)
    
    ansStr="Case #"+str(ii)+": "+str(ans)+"\n"
    file.writelines(ansStr)
    print(ansStr,end="")
file.close()
    
