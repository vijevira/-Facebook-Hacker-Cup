def isAllIncluded(set1,set2):
    for i in set1:
        if i not in set2:
            return False
    return True

def bfs(graph, node,setS):
    visited=[]
    queue=[(node,0)]
    visited.append(node)
    ans=dict()
    setNode=set()
    while queue:
        s = queue.pop(0) 
        ans[s[0]]=s[1]
        setNode.add(s[0])
        for neighbour in graph[s[0]]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append((neighbour,s[1]+1))
    possible=isAllIncluded(setS,setNode)
    return [ans,possible]

def numbersMove(s,tset):
    ans=0
    for i in s:
        ans+=tset[i]
    return ans
    

t=int(input())
file=open("consistency_chapter_2.txt","w")
for ii in range (1,t+1):
    s=input()
    setS=set(s)
    dictAB={i:[] for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    for _ in range (int(input())):
        ab=input()
        dictAB[ab[1]].append(ab[0])
    ansList=[]
    for key in dictAB:
        '''if len(dictAB)>1:
            x=bfs(dictAB,key,setS)
            if len(x[0])>1:
                print(x)
                pass
    print("______",ii)    
'''
        tset=bfs(dictAB,key,setS)
        if tset[1]: 
            ansList.append(numbersMove(s,tset[0]))
    ans=-1
    if len(ansList)>0:
        ans=min(ansList)
    ansStr="Case #"+str(ii)+": "+str(ans)+"\n"
    file.writelines(ansStr)
    print(ansStr,end="")
file.close()

