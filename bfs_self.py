graph={'A':['B','C','E'],'B':['C','D'],'C':['D','E'],'D':[],'E':[]}
def bfs(graph,root):
    visited=[]
    queue=[]

    visited.append(root)
    queue.append(root)

    while queue:
        m=queue.pop(0)
        print(m)
        for neighbours in graph[m]:
            if neighbours not in visited:
                visited.append(neighbours)
                queue.append(neighbours)

bfs(graph,'A')
