from mapping import Mapping
import math

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
        frontier = [start]
        connections = mapping.get_citys_connections(start)
        node = start
        path = {start: start}
        cost = {start: 0}

        while frontier:
            node = frontier.pop(0)
            if(node == end):
                return path[node]
            explored.append(node)
            for city, city_cost in connections.items():
                new_cost = cost[node] + city_cost
                if city not in cost or new_cost < cost[city]:
                    cost[city] = new_cost
                    frontier.append(city)
                    path[city] = path[node] + [city]

        return "failure"

    def astar(self, mapping, start, end):
        explored = []
        frontier = [(start, 0)]
        path = {start: [start]}
        cost = {start: 0}

        while frontier:
            node, node_cost = frontier.pop(0)
            if node == end:
                return path[node]
            explored.append(node)
            for city, city_cost in mapping.get_citys_connections(node):
                new_cost = node_cost + city_cost
                if city not in cost or new_cost < cost[city]:
                    cost[city] = new_cost
                    h_cost = self.euclidean_distance(mapping.get_city(node), mapping.get_city(end))
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