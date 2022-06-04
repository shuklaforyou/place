

graph={}
def add_node(v):
    global graph
    if v in graph:
        print(v,"is already is present in the graph!")
    else:
        graph[v]=[]


def add_edge1(v1,v2):
    global graph
    if v1 not in graph:
        print(v1,"is not present  in the graph!")
    elif v2 not in graph:
        print(v2,"is not present  in the graph!")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
        

playerfrined=list(map(int,input().split(" ")))
player = playerfrined[0]
rel = playerfrined[1]
list_rate=list(map(int,input().split()))

if  player != len(list_rate):
    print("invald code")

for i in range(1,player+1):
    add_node(i)



for j in range(rel):
    yxrel=(list(map(int,input().split())))
    add_edge1(yxrel[0],yxrel[1])


for q in range(1,player):
    work=[]
    notwork=[]
    pre=i
    post=graph[i]
    work.append(pre)
    work.append(post)
    for w in range(player):
        if w not in work:
            notwork.append(w)
    count=0
    for j in range(player):
        for k in range(len(notwork)):
            if list_rate[j] > list_rate[k]:
                count+=1
    print(count,end=' ')
        




                
