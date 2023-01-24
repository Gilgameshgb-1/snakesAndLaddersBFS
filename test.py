import script as bfsGame

#Adjacency list test_1:
def test_1():
    adjacencyList = bfsGame.generateAdjacencyList()
    
    print(adjacencyList[2])
    print(adjacencyList[55])
    print(adjacencyList[98])
    print(adjacencyList[99])
    print(adjacencyList[100])

def test_2():
    adjacencyList = bfsGame.generateAdjacencyList()

    bfsGame.replaceEdgeForVertices(adjacencyList, 40, 40, 4)
    bfsGame.replaceEdgeForVertices(adjacencyList, 70, 70, 7)

    print(adjacencyList[38])
    print(adjacencyList[66])
    print(adjacencyList[70])
    print(adjacencyList[40])

def test_3():
    adjacencyList = bfsGame.generateAdjacencyList()
    parent = []
    level = []
    vertices = 100

    parent, level = bfsGame.initBfs(parent, level, vertices)
    parent, level = bfsGame.breadthFirstSearch(adjacencyList, parent, level, 1)

    print()
    print("Minimum number of moves required to finish the game: ",level[100])
    print()
    print("Shortest path to finish the game is: ")
    bfsGame.printPathFromSourceToDestination(parent, 100)

def test_4():
    adjacencyList = bfsGame.generateAdjacencyList()
    parent = []
    level = []
    vertices = 100

    bfsGame.replaceEdgeForVertices(adjacencyList, 4, 4, 40)
    bfsGame.replaceEdgeForVertices(adjacencyList, 7, 7, 70)
    bfsGame.replaceEdgeForVertices(adjacencyList, 45, 45, 85)

    parent, level = bfsGame.initBfs(parent, level, vertices)
    parent, level = bfsGame.breadthFirstSearch(adjacencyList, parent, level, 1)

    print()
    print("Minimum number of moves required to finish the game: ",level[100])
    print()
    print("Shortest path to finish the game is: ")
    bfsGame.printPathFromSourceToDestination(parent, 100)

def test_5():
    adjacencyList = bfsGame.generateAdjacencyList()
    parent = []
    level = []
    vertices = 100

    bfsGame.replaceEdgeForVertices(adjacencyList, 4, 4, 40)
    bfsGame.replaceEdgeForVertices(adjacencyList, 7, 7, 70)
    bfsGame.replaceEdgeForVertices(adjacencyList, 45, 45, 85)

    bfsGame.replaceEdgeForVertices(adjacencyList, 95, 95, 2)
    bfsGame.replaceEdgeForVertices(adjacencyList, 40, 40, 25)
    bfsGame.replaceEdgeForVertices(adjacencyList, 79, 79, 45)

    parent, level = bfsGame.initBfs(parent, level, vertices)
    parent, level = bfsGame.breadthFirstSearch(adjacencyList, parent, level, 1)

    print()
    print("Minimum number of moves required to finish the game: ",level[100])
    print()
    print("Shortest path to finish the game is: ")
    bfsGame.printPathFromSourceToDestination(parent, 100)


def checkAllTests():
    print("Test with no snakes or ladders")
    print("----------------------------------------------------------------------------------------------------------------")
    test_3()
    print("----------------------------------------------------------------------------------------------------------------")
    print("Test with 3 ladders (4, 40), (7, 70), (45, 85)")
    print("----------------------------------------------------------------------------------------------------------------")
    test_4()
    print("----------------------------------------------------------------------------------------------------------------")
    print("Test with 3 ladders and 3 snakes (95, 2), (40, 25), (79, 45)")
    print("----------------------------------------------------------------------------------------------------------------")
    test_4()
    print("----------------------------------------------------------------------------------------------------------------")

checkAllTests()