def checkRow(grid,num):
    ans=0
    pos=()
    for i in range(n):
        if grid[num][i]=='O':
            return False
        elif grid[num][i]=='.':
            pos=(num,i)
            ans+=1
    
    return [ans,pos]

def checkCol(grid,num):
    ans=0
    pos=()
    for i in range (len(grid)):
        if grid[i][num]=='O':
            return False
        elif grid[i][num]=='.':
            pos=(i,num)
            ans+=1
    return [ans,pos]

t=int(input())
file=open("xs_and_os_output.txt","w")
for ii in range (1,t+1):
    n=int(input())
    grid=[]
    for i in range (n):
        grid.append(list(input()))
    ans=n+1
    allPos={}
    oneset=set()
    for i in range (n):
        tempx=checkRow(grid,i)
        if tempx:
            temp=tempx[0]
            if temp!=1 or tempx[1] not in oneset:
                if temp==1:
                    oneset.add(tempx[1])
                if temp in allPos:
                    allPos[temp]+=1
                else:
                    allPos[temp]=1
                ans=min(ans,temp)
        tempx=checkCol(grid,i)
        if tempx:
            temp=tempx[0]
            if temp!=1 or tempx[1] not in oneset:
                if temp==1:
                    oneset.add(tempx[1])
                if temp in allPos:
                    allPos[temp]+=1
                else:
                    allPos[temp]=1
                ans=min(ans,temp)
    if ans==n+1:
        ans="Impossible"
    else:
        ans=str(ans)+" "+str(allPos[ans])
    
    ansStr="Case #"+str(ii)+": "+ans+"\n"
    file.writelines(ansStr)
    print(ansStr,end="")
file.close()
