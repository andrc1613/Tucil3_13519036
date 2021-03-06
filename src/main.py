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

# Main Function
if __name__ == "__main__":
    print("Input \"#\" untuk keluar.")
    
    # file input handler
    filename = input("Enter file name: ")
    while (filename != "#"):
        try:
            txtMap = createGraphFromFile(filename)
            txtMap.visualizeGraph()
            txtMap.showGraph()
            print("\n")
            
            # node input handler
            print("Silakan masukkan lokasi asal dan tujuan (Format: <lokasi_asal><spasi><lokasi_tujuan>, contoh: ITB Sabuga) : ")
            start, end = input().split()
            
            # validate node input
            while not txtMap.getNodeByName(start) or not txtMap.getNodeByName(end):
                if not txtMap.getNodeByName(start):
                    print("Tidak ada lokasi dengan nama {0}".format(start))
                if not txtMap.getNodeByName(end):
                    print("Tidak ada lokasi dengan nama {0}".format(end))
                start, end = input("Silakan masukkan lokasi asal dan tujuan (Format: <lokasi_asal><spasi><lokasi_tujuan>, contoh: ITB Sabuga) : ").split()

            txtMap.aStar(start,end)
            txtMap.visualizePath()
            filename = input("Enter file name: ")
        
        except Exception:
            print("File tidak ditemukan")
            filename = input("Enter file name: ")
