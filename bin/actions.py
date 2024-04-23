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

    def dls(self, mapping, start, end):
        pass

    def ucs(self, mapping, start, end):
        # explored = []
        # cost = 0
        # connections = mapping.get_citys_connections(start)
        # node = start

        # while True:
        #     if(connections.empty()):
        #         return None
        #     if(node == end):
        #         return #solution
        #     explored.append(node)
        #     for city in mapping.get_citys_connections(node):
        #         if city not in explored:
        #             connections.append(city)
        pass

    def astar(self, mapping, start, end):
        pass

    ############################
    #      Helper Functions    #
    ############################