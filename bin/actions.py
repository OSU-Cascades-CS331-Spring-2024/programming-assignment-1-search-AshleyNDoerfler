from mapping import Mapping
import math
import heapq

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
        
            # print("Node: ", node)

            # connections = self.mapping.get_citys_connections(node)

            if node == self.end:
                return reached

            # {city_obj: {city_connection: cost}}, so given the node object, get the connection key value pairs
            for child in self.mapping.city_map[node]:
                # print("node: ", node.name, ', Connections ', self.mapping.city_map[node])
                # print("Child: ", child)
                # print("Reached: ", reached)
                if child not in reached:
                    reached.append(child)
                    if child == self.end:
                        return reached
                    frontier.append(list(self.mapping.get_citys_connections(node.name).keys())[0])
        return None

    def dls(self, depth):
        frontier = [self.start]
        path = []
        count = 0
        visited = []

        while frontier:
            node = self.mapping.get_city_object(frontier.pop(0))
            visited.append(node.name)

            print("Depth: ", depth, "Node: ", node.name, ", Frontier: ", frontier)

            path.append(node.name)
            count += 1

            # Success
            if node.name == self.end:
                return path

            if depth > count:
                for child_name, _ in self.mapping.get_citys_connections(node.name).items():
                    if child_name not in visited:
                        frontier.append(child_name)
                    # print("Node: ", node.name, ",Frontier: ", frontier)

        return "cutoff"

    def iterative_deepening_search(self):
        for depth in range(0, 100):
            result = self.dls(depth)
            if result != "cutoff":
                print("Result: ", result)
                return result

    def ucs(self):
        explored = set()
        frontier = [(0, self.start)]
        path = {self.start: [self.start]}
        cost = {self.start: 0}

        while frontier:
            current_cost, node = heapq.heappop(frontier)

            if node == self.end:
                return path[node]

            explored.add(node)

            for child, child_cost in self.mapping.get_citys_connections(node).items():
                total_cost = current_cost + int(child_cost)

                if child not in cost or total_cost < cost[child]:
                    cost[child] = total_cost
                    path[child] = path[node] + [child]
                    heapq.heappush(frontier, (total_cost, child))

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
    
    