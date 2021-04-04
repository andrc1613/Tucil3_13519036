from pyvis.network import Network
from classes import Graph, Node


# File Handling
def createGraphFromFile(filename):
    
    # open input file
    f = open("test/"+filename, "r")
    tempGraph = Graph()
    filelines = [line.strip() for line in f]

    # initialize vertex count
    num = int(filelines[0])
    filelines.pop(0)

    # initialize list of nodes
    nodesList = []
    for _ in range(num):
        nodesList.append(filelines[0].split())
        filelines.pop(0)

    # initialize adjacency matrix
    adjacencyMatrix = []
    for _ in range(num):
        adjacencyMatrix.append(''.join(filelines[0].split()))
        filelines.pop(0)

    # initialize graph
    for i in range(num):
        tempName = nodesList[i][2]
        tempX = int(nodesList[i][0])
        tempY = int(nodesList[i][1])
        tempAdj = []
        for j in range(num):
            if adjacencyMatrix[i][j] == "1":
                tempAdj.append(nodesList[j][2])

        tempNode = Node(tempName, tempX, tempY, tempAdj)
        tempGraph.addNode(tempNode)

    return tempGraph


# Graph Visualization
def visualizeGraph(graph):
    net = Network(height = 1000,width = 1000)
    listName = []
    listX = []
    listY = []
    listsize = [10 for i in range (graph.nodesCount)]
    listEdges = []
    for node in graph.nodes:
        listName.append(node.name)
        listX.append(node.x)
        listY.append(node.y)
        for adjNodes in node.adjacentNodes:
            listEdges.append((node.name,adjNodes))
    net.add_nodes(listName,size = listsize, x = listX, y = listY)
    net.add_edges(listEdges)
    net.show('test.html')
    net.show_buttons()
    return


# Main Function
if __name__ == "__main__":
    filename = "input1.txt"  # input("Enter file name: ")
    txtMap = createGraphFromFile(filename)
    txtMap.showGraph()
    # visualizeGraph(txtMap)
    # a = txtMap.getNodeByName("Sabuga")
    # b = txtMap.getNodeByName("Ciwalk")
    # path = txtMap.aStar(a,b)
    # if path != None:
    #     for e in path:
    #         print(e.name,e.g)
    # else:
    #     print("none")
