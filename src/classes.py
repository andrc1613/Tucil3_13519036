class Graph:
    def __init__(self):
        self.nodes = []
        self.nodesCount = 0

    def addNode(self, nodes):
        self.nodes.append(nodes)
        self.nodesCount += 1

    def getNodeByName(self, name):
        for n in self.nodes:
            if n.name == name:
                return n

    def showGraph(self):
        for e in self.nodes:
            e.showNode()
        return

    def euclideanDistance(self, node1, node2):
        return ((node1.x - node2.x)**2 + (node1.y - node2.y)**2)**(1/2)

    def aStar(self, start, end):

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
        openNodes.append(start)

        while any(openNodes):
            current = getNodeByF(openNodes)

            # case 1 : path found
            if current == end:
                path = []
                while current.previous != None:
                    path.append(current)
                    current = current.previous
                path.append(current)
                return path[::-1]

            # case 2 : path not yet found
            openNodes.remove(current)
            closedNodes.append(current)
            for adjacentNode in current.adjacentNodes:
                node = self.getNodeByName(adjacentNode)
                if node in closedNodes:
                    continue
                
                tempG = self.euclideanDistance(current,node) + current.g
                tempH = self.euclideanDistance(node,end)
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
        return None


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

    def showNode(self):
        print("{0} ({1},{2}) {3}".format(
            self.name, self.x, self.y, self.adjacentNodes))
