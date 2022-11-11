graph = {
'A' : ['B','C','D'],
'B' : ['D', 'E'],
'C' : ['F'],
'D' : ['E'],
'E' : ['F'],
'F' : []
}
stack = []
visited = set()
ans = []
for s in list(graph.keys()):
    if s not in visited:
        stack.append(s)
        while(stack):
            s = stack.pop()
            if s in visited:
                continue
            visited.add(s)
            ans.append(s)
            for neighbours in graph[s]:
                if neighbours not in stack:
                    stack.append(neighbours)

for a in ans:
    print(a)