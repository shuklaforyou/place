from platform import node


def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present in the graph!")
    else:
        node_count=node_count+1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge1(v1,v2):#undirected and unweight graph
    if v1 not in nodes:
        print(v1,"is not present in the graph!")
    elif v2 not in nodes:
        print(v2,"is not present in the graph!")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1

def add_edge2(v1,v2,cost):#undirected and weight graph
    if v1 not in nodes:
        print(v1,"is not present in the graph!")
    elif v2 not in nodes:
        print(v2,"is not present in the graph!")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost

def add_edge3(v1,v2):#directed and unweight graph
    if v1 not in nodes:
        print(v1,"is not present in the graph!")
    elif v2 not in nodes:
        print(v2,"is not present in the graph!")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1

def delete_node(v):
    global node_count
    if v not in nodes:
        print("v is not present in the graph!")
    else:
        index1=nodes.index(v)
        node_count=node_count-1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_ege1(v1,v2):#unweighted and undirectional
    if v1 not in nodes:
        print(v1,"is not present in the graph!")
    elif v2 not in nodes:
        print(v2,"is not present in the graph!")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0
        
def delete_ege2(v1,v2):#unweighted and undirectional
    if v1 not in nodes:
        print(v1,"is not present in the graph!")
    elif v2 not in nodes:
        print(v2,"is not present in the graph!")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        #graph[index2][index1]=0


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()

nodes=[]
graph=[]
node_count=0
print("before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_edge3("A","B")
add_edge3("A","C")
add_edge3("B","C")
delete_ege2("B","C")
print("aftre adding nodes")
print(nodes)
print(graph)
print_graph() 