import script as bfsGame
import time

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

def test_6():
    adjacencyList = bfsGame.generateAdjacencyList()
    parent = []
    level = []
    vertices = 100

    bfsGame.replaceEdgeForVertices(adjacencyList, 4, 4, 40)
    bfsGame.replaceEdgeForVertices(adjacencyList, 7, 7, 70)
    bfsGame.replaceEdgeForVertices(adjacencyList, 45, 45, 85)
    bfsGame.replaceEdgeForVertices(adjacencyList, 20, 20, 40)
    bfsGame.replaceEdgeForVertices(adjacencyList, 10, 10, 80)
    bfsGame.replaceEdgeForVertices(adjacencyList, 13, 13, 55)
    bfsGame.replaceEdgeForVertices(adjacencyList, 23, 23, 88)
    bfsGame.replaceEdgeForVertices(adjacencyList, 44, 44, 99)
    bfsGame.replaceEdgeForVertices(adjacencyList, 60, 60, 70)
    bfsGame.replaceEdgeForVertices(adjacencyList, 70, 70, 80)

    bfsGame.replaceEdgeForVertices(adjacencyList, 95, 95, 2)
    bfsGame.replaceEdgeForVertices(adjacencyList, 40, 40, 25)
    bfsGame.replaceEdgeForVertices(adjacencyList, 79, 79, 45)
    bfsGame.replaceEdgeForVertices(adjacencyList, 91, 91, 22)
    bfsGame.replaceEdgeForVertices(adjacencyList, 90, 90, 30)
    bfsGame.replaceEdgeForVertices(adjacencyList, 97, 97, 12)
    bfsGame.replaceEdgeForVertices(adjacencyList, 77, 77, 25)
    bfsGame.replaceEdgeForVertices(adjacencyList, 87, 87, 15)
    bfsGame.replaceEdgeForVertices(adjacencyList, 19, 19, 2)
    bfsGame.replaceEdgeForVertices(adjacencyList, 65, 65, 6)

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
    start_time = time.time()
    test_5()
    end_time = time.time()
    print("Elapsed time:", end_time - start_time, "seconds")
    print("----------------------------------------------------------------------------------------------------------------")
    print("Test with 10 ladders and 10 snakes")
    print("----------------------------------------------------------------------------------------------------------------")
    start_time = time.time()
    test_6()
    end_time = time.time()
    print("Elapsed time:", end_time - start_time, "seconds")
    print("----------------------------------------------------------------------------------------------------------------")

checkAllTests()