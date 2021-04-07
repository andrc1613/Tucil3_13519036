import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = []
        self.nodesCount = 0
        self.aStarPath = []

    def addNode(self, nodes):
        self.nodes.append(nodes)
        self.nodesCount += 1

    def getNodeByName(self, name):
        for n in self.nodes:
            if n.name == name:
                return n
        return None

    def showGraph(self):
        print("Berikut list lokasi yang terdapat dalam peta:")
        for e in self.nodes:
            e.showNodeName()
        return

    def visualizeGraph(self):
        plt.axis([-10,10,-10,10])
        listName = []
        listX = []
        listY = []
        listEdges = []
        for node in self.nodes:
            listName.append(node.name)
            listX.append(node.x)
            listY.append(node.y)
            for adjNodes in node.adjacentNodes:
                listEdges.append((node.name,adjNodes))

        for i in range(self.nodesCount):
            plt.plot(listX[i],listY[i],"bo")
            plt.text(listX[i],listY[i],listName[i])
        
        for i in range(len(listEdges)):
            node1 = self.getNodeByName(listEdges[i][0])
            node2 = self.getNodeByName(listEdges[i][1])
            plt.plot([node1.x,node2.x],[node1.y,node2.y],color='b')
            plt.text((node1.x+node2.x)/2, (node1.y+node2.y)/2, str(round(self.euclideanDistance(node1,node2),2)))
        
        plt.show()
        return
    
    def visualizePath(self):
        if self.aStarPath == None:
            print("Tidak terdapat jalan yang menghubungkan kedua lokasi.\n")
            return
        plt.axis([-10,10,-10,10])
        listName = []
        listX = []
        listY = []
        listNameInPath = []
        listEdges = []
        for node in self.nodes:
            listName.append(node.name)
            listX.append(node.x)
            listY.append(node.y)
            if node in self.aStarPath:
                listNameInPath.append(node.name)
            for adjNodes in node.adjacentNodes:
                listEdges.append((node.name,adjNodes))

        for i in range(self.nodesCount):
            plt.text(listX[i],listY[i],listName[i])
            if listName[i] in listNameInPath:
                plt.plot(listX[i],listY[i],"ro")
                continue
            plt.plot(listX[i],listY[i],"bo")

        for i in range(len(listEdges)):
            node1 = self.getNodeByName(listEdges[i][0])
            node2 = self.getNodeByName(listEdges[i][1])
            if node1.name in listNameInPath and node2.name in listNameInPath:
                plt.plot([node1.x,node2.x],[node1.y,node2.y],color='r')
                plt.text((node1.x+node2.x)/2, (node1.y+node2.y)/2, str(round(self.euclideanDistance(node1,node2),2)))
                continue
            plt.plot([node1.x,node2.x],[node1.y,node2.y],color='b')
            plt.text((node1.x+node2.x)/2, (node1.y+node2.y)/2, str(round(self.euclideanDistance(node1,node2),2)))

        plt.show()
        print("Jarak dari {0} menuju {1} adalah {2}\n".format(self.aStarPath[0].name,self.aStarPath[-1].name,str(round(self.aStarPath[-1].g,2))))
        return

    def euclideanDistance(self, node1, node2):
        return ((node1.x - node2.x)**2 + (node1.y - node2.y)**2)**(1/2)

    def aStar(self, start, end):
        self.aStarPath = []

        # define get node with minimum f value function
        def getNodeByF(openNodes):
            minNode = openNodes[0]
            for n in openNodes:
                if minNode.f > n.f:
                    minNode = n
            return minNode
        
        # initialize variables
        openNodes = []
        closedNodes = []

        # algorithm
        openNodes.append(self.getNodeByName(start))
        endNode = self.getNodeByName(end)
        while any(openNodes):
            current = getNodeByF(openNodes)

            # case 1 : path found
            if current == endNode:
                while current.previous != None:
                    self.aStarPath.append(current)
                    current = current.previous
                self.aStarPath.append(current)
                self.aStarPath = self.aStarPath[::-1]
                return

            # case 2 : path not yet found
            openNodes.remove(current)
            closedNodes.append(current)
            for adjacentNode in current.adjacentNodes:
                node = self.getNodeByName(adjacentNode)
                if node in closedNodes:
                    continue
                
                tempG = self.euclideanDistance(current,node) + current.g
                tempH = self.euclideanDistance(node,endNode)
                tempF = tempG + tempH
                
                if node in openNodes:
                    if tempG >= node.g:    
                        continue
                
                node.f = tempF
                node.g = tempG
                node.h = tempH
                node.previous = current
                openNodes.append(node)
        
        # case 3 : path not found
        self.aStarPath = None
        return


class Node:
    def __init__(self, name, x, y, adjacentNodes):
        self.name = name
        self.x = x
        self.y = y
        self.adjacentNodes = adjacentNodes
        self.previous = None
        self.f = 0
        self.g = 0
        self.h = 0

    def showNodeName(self):
        print(self.name)
