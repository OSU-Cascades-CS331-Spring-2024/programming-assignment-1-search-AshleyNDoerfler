from mapping import Mapping
import math

class Actions:

    def __init__(self, mapping, start, end, search_type = 'bfs'):
        self.search_type = search_type
        self.mapping = mapping
        self.start = start
        self.end = end

    def search(self):
        if self.search_type == 'bfs':
            return self.bfs()
        elif self.search_type == 'dls':
            return self.iterative_deepening_search()
        elif self.search_type == 'ucs':
            return self.ucs()
        elif self.search_type == 'astar':
            return self.astar()
        else:
            return "Invalid search type"

    ############################
    #    Searching Algorithms  #
    ############################
    
    def bfs(self):
        reached = []
        frontier = [self.start]
        reached.append(self.start)

        # node = self.mapping.get_city_object(self.start)

        
        
        # print(self.mapping.city_map)

        while(frontier):
            node = self.mapping.get_city_object(frontier.pop(0))
            # node = self.get_next_city(mapping, node)

            # Base case
            if node == self.end:
                return node
        
            print("Node: ", node)

            # connections = self.mapping.get_citys_connections(node)

            if node == self.end:
                return reached

            # {city_obj: {city_connection: cost}}, so given the node object, get the connection key value pairs
            for child in self.mapping.city_map[node]:
                print("Child: ", child)
                print("Reached: ", reached)
                if child not in reached:
                    reached.append(child)
                    if child == self.end:
                        return reached
                    frontier.append(list(self.mapping.get_citys_connections(child).keys())[0])
        return None

    def dls(self, depth):
        result = "failure"

        if depth == 0:
            if self.start == self.end:
                return self.start
            else:
                return "cutoff"

        if depth > 0:
            for child in self.mapping.get_citys_connections(self.start):
                result = self.dls(self.mapping, child, self.end, depth - 1)
                if (result != "failure"):
                    return result
        
        return "failure"

    def iterative_deepening_search(self):
        depth = 0
        while True:
            result = self.dls(self.mapping, self.start, self.end, depth)
            if result != "cutoff":
                return result
            depth += 1

    def ucs(self):
        explored = []
        frontier = [self.start]
        connections = self.mapping.get_citys_connections(self.start)
        node = self.start
        path = {self.start: self.start}
        cost = {self.start: 0}

        while frontier:
            node = frontier.pop(0)
            if(node == self.end):
                return path[node]
            explored.append(node)
            for city, city_cost in connections.items():
                new_cost = cost[node] + city_cost
                if city not in cost or new_cost < cost[city]:
                    cost[city] = new_cost
                    frontier.append(city)
                    path[city] = path[node] + [city]

        return "failure"

    def astar(self):
        explored = []
        frontier = [(self.start, 0)]
        path = {self.start: [self.start]}
        cost = {self.start: 0}

        while frontier:
            node, node_cost = frontier.pop(0)
            if node == self.end:
                return path[node]
            explored.append(node)
            for city, city_cost in self.mapping.get_citys_connections(node):
                new_cost = node_cost + city_cost
                if city not in cost or new_cost < cost[city]:
                    cost[city] = new_cost
                    h_cost = self.euclidean_distance(self.mapping.get_city(node), self.mapping.get_city(self.end))
                    f_cost = new_cost + h_cost
                    frontier.append((city, f_cost))
                    path[city] = path[node] + [city]
        

    ############################
    #      Helper Functions    #
    ############################

    def euclidean_distance(self, city_1, city_2):
        lat1, lon1 = city_1.get_lat(), city_1.get_lon()
        lat2, lon2 = city_2.get_lat(), city_2.get_lon()
        return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
    
    