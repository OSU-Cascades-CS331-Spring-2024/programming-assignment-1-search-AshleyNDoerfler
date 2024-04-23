class Actions:

    def __init__(self, search_type = 'bfs'):
        self.search_type = search_type

    ############################
    #    Searching Algorithms  #
    ############################
    
    def bfs(self, mapping, start, end):
        reached = []
        connections = mapping.get_citys_connections(start)
        node = start
        # Base case
        if node == end:
            return node
        frontier = start
        reached.append(node)

        while(frontier.empty() == False):
            node = frontier.pop(0)

            for child in connections:
                s = child
                if child not in reached:
                    reached.append(child)
                    if child == end:
                        return reached
                    frontier.append(mapping.get_citys_connections(child))
        return None

    def dls(self, mapping, start, end, depth):
        frontier = start
        result = "failure"

        while(frontier.empty() == False):
            node = frontier.pop(0)
            if node == end:
                return node
            if len(depth > mapping.get_citys_connections(node)) :
                return "cutoff"
            elif(cycle_node(node) == False):
                for child in mapping.get_citys_connections(node):
                    frontier.append(child)
            return result

    def iterative_deepening_search(self, mapping, start, end):
        for depth in range(0, 1e-100):
            result = self.dls(mapping, start, end, depth)
            if result != "cutoff":
                return result

    def ucs(self, mapping, start, end):
        explored = []
        frontier = start
        connections = mapping.get_citys_connections(start)
        node = start
        path = node

        while True:
            if(frontier.empty()):
                return "failure"
            node = frontier.pop(0)
            if(node == end):
                return path
            explored.append(node)
            for city in connections:
                child = city
                if child not in explored:
                    frontier.append(city)
                elif child in frontier:
                    if path < child:
                        path = child


    def astar(self, mapping, start, end):
        pass

    ############################
    #      Helper Functions    #
    ############################