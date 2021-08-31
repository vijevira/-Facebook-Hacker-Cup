def maxSumEdge(graph,edge,val,vis):
	if edge in vis:
		return 0
	vis.add(edge)
	if len(graph[edge])==0:
		return val[edge]
	temp=[]
	for i in graph[edge]:
		temp.append(maxSumEdge(graph,i,val,vis))
	return val[edge]+max(temp)

def maxValue(graph,val):
    root=1
    if len(graph[root])==0:
        return val[1]
    if len(graph[root])==1:
        return maxSumEdge(graph,root,val,set())
    child=[]
    for i in graph[root]:
        child.append(maxSumEdge(graph,i,val,{1}))

    child.sort()
    return val[root]+child[-1]+child[-2]
        
    
    
    
t=int(input())
file=open("gold_mine_chapter_1_output.txt","w")
for ii in range (1,t+1):
    n=int(input())
    caves=list(map(int,input().split()))
    val=[0]+caves
    graph={i:[] for i in range (1,n+1)}
    for i in range (n-1):
        x,y=map(int,input().split())
        graph[y].append(x)
        graph[x].append(y)
    ans=maxValue(graph,val)
    
    ansStr="Case #"+str(ii)+": "+str(ans)+"\n"
    file.writelines(ansStr)
    print(ansStr,end="")
file.close()

