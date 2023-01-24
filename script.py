def generateAdjacencyList():
    vertices = 100
    
    #Creation of adjecency list required for graph representation
    adjacencyList = [[] for _ in range(vertices + 1)]

    #Populating the adjacency list with edges represeting
    #all possible moves from each vertex
    for i in range(1, vertices):
        for j in range(i + 1, min(i + 7, vertices + 1)):
            adjacencyList[i].append(j)
    
    return adjacencyList

def replaceEdgeForVertices(adjacencyList, startVertex, oldEdge, newEdge):
    for i in range(startVertex - 1, max(startVertex - 6, 0) -1, -1):
        adjacencyList[i] = [newEdge if x == oldEdge else x for x in adjacencyList[i]]
    adjacencyList[startVertex].clear()

def printPathFromSourceToDestination(parent, destination):
    if parent[destination] == -1:
        # We have reached the source vertex
        print(destination, end=" -> ")
    else:
        printPathFromSourceToDestination(parent, parent[destination])
        if destination == 100:
            print(destination)
        else:
            print(destination, end=" -> ")

def breadthFirstSearch(adjacencyList, parent, level, start):
    #Initial level of the starting vertex, level of adjacent vertices will be 1
    #level of their adjacent vertices is 2, giving the idea of breadth
    level[start] = 0

    #Queue for processing vertices
    queue = []

    #The initial vertex is added to the queue
    queue.append(start)

    #Looping until all vertices are visited
    while not len(queue) == 0:
        #Vertex is automatically removed
        newVertex = queue.pop(0)

        #The following loop checks unvisited vertices, and appends them
        #It also updates the parent level
        for i, vertex in enumerate(adjacencyList[newVertex]):
            if level[vertex] == -1:
                level[vertex] = level[newVertex] + 1
                parent[vertex] = newVertex
                queue.append(vertex)

    return parent, level

def initBfs(parent, level, vertices):
    parent = [-1 for i in range(vertices + 1)]
    level = [-1 for i in range(vertices + 1)]

    return parent, level