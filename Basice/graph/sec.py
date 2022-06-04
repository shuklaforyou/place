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
        
def add_edge2(v1,v2,cost):#weigth and undirectional graph
    global graph
    if v1 not in graph:
        print(v1,"is not present  in the graph!")
    elif v2 not in graph:
        print(v2,"is not present  in the graph!")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

def add_edge3(v1,v2):
    global graph
    if v1 not in graph:
        print(v1,"is not present  in the graph!")
    elif v2 not in graph:
        print(v2,"is not present  in the graph!")
    else:
        graph[v1].append(v2)
    

def delete_node(v):
    if v not in graph:
        print("v is not present in the graph!")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)


def delete_node2(v):#weighted graph
    if v not in graph:
        print("v is not present in the graph!")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            for j in list1:
                if v ==j[0]:
                    list1.remove(j)
                    break

def delete_edge1(v1,v2):
    if v1 not in graph:
        print(v1,"is not present  in the graph!")
    elif v2 not in graph:
        print(v2,"is not present  in the graph!")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)    
            graph[v2].remove(v1)    

def delete_edge2(v1,v2,cost):
    if v1 not in graph:
        print(v1,"is not present  in the graph!")
    elif v2 not in graph:
        print(v2,"is not present  in the graph!")
    else:
        temp=[v1,cost]
        temp1=[v2,cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)    
            graph[v2].remove(temp)    

def delete_edge3(v1,v2):
    if v1 not in graph:
        print(v1,"is not present  in the graph!")
    elif v2 not in graph:
        print(v2,"is not present  in the graph!")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)    
            #graph[v2].remove(v1)    


def DFS(nodes,visited,graph):
    if nodes not in visited:
        print(nodes,end=" ")
        visited.add(nodes)
        for i in graph[nodes]:
            DFS(i,visited,graph)


def DFSiterative(nodes,graph):
    visited=set()
    if nodes not in graph:
        print("node is not present in the graph")
        return
    stack=[]
    stack.append(nodes)
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


visited=set()
graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge1("A","B")
add_edge1("A","C")
add_edge1("A","D")
add_edge1("B","D")
add_edge1("E","D")
add_edge1("B","E")
DFS("A",visited,graph)
print()
# delete_node2("B")
# delete_edge2("B","C",2)
print(graph)