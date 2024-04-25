from mapping import Mapping
import math
import heapq

class Actions:

    def __init__(self, mapping, start, end, search_type = 'bfs'):
        self.search_type = search_type
        self.mapping = mapping
        self.start = start
        self.end = end
        self.frontier_count = 0
        self.maintained = 0

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
            self.frontier_count += 1
            # node = self.get_next_city(mapping, node)
        
            # print("Node: ", node)

            # connections = self.mapping.get_citys_connections(node)

            if node == self.end:
                self.maintained = len(frontier)
                return reached, self.frontier_count, len(reached - 1), self.maintained

            # {city_obj: {city_connection: cost}}, so given the node object, get the connection key value pairs
            for child in self.mapping.city_map[node]:
                # print("node: ", node.name, ', Connections ', self.mapping.city_map[node])
                # print("Child: ", child)
                # print("Reached: ", reached)
                if child not in reached:
                    reached.append(child)
                    if child == self.end:
                        return reached, self.frontier_count, len(reached - 1), self.maintained
                    frontier.append(list(self.mapping.get_citys_connections(node.name).keys())[0])
        return None

    def dls(self, depth):
        frontier = [self.start]
        path = []
        count = 0
        visited = []

        while frontier:
            node = self.mapping.get_city_object(frontier.pop(0))
            self.frontier_count += 1
            visited.append(node.name)

            print("Depth: ", depth, "Node: ", node.name, ", Frontier: ", frontier)

            path.append(node.name)
            count += 1

            # Success
            if node.name == self.end:
                self.maintained = len(frontier)
                return path, len(frontier)

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
                return result, self.frontier_count, len(result - 1), self.maintained

    def ucs(self):
        explored = set()
        frontier = [(0, self.start)]
        path = {self.start: [self.start]}
        cost = {self.start: 0}

        while frontier:
            current_cost, node = heapq.heappop(frontier)
            self.frontier_count += 1

            if node == self.end:
                return path[node], self.frontier_count, len(path[node] - 1), len(frontier)

            explored.add(node)

            for child, child_cost in self.mapping.get_citys_connections(node).items():
                total_cost = current_cost + int(child_cost)

                if child not in cost or total_cost < cost[child]:
                    cost[child] = total_cost
                    path[child] = path[node] + [child]
                    heapq.heappush(frontier, (total_cost, child))

        return "failure"

    def astar(self):
        explored = set()
        frontier = [(0, self.start)]
        path = {self.start: [self.start]}
        cost = {self.start: 0}

        while frontier:
            current_cost, node = heapq.heappop(frontier)
            self.frontier_count += 1

            if node == self.end:
                return path[node], self.frontier_count, len(path[node] - 1), self.maintained, len(frontier)

            explored.add(node)

            for child, _ in self.mapping.get_citys_connections(node).items():
                
                print("Node: ", node, ", Child: ", child)
                
                distance_to_goal = self.euclidean_distance(self.mapping.get_city_object(node), self.mapping.get_city_object(self.end)), len(frontier)
                heuristic_cost = distance_to_goal  # Replace this with your own heuristic function

                distance = self.euclidean_distance(node, child)
                total_cost = current_cost + distance + heuristic_cost  # Total cost includes both actual cost and heuristic

                if child not in cost or total_cost < cost[child]:
                    cost[child] = total_cost
                    path[child] = path[node] + [child]
                    heapq.heappush(frontier, (total_cost, child))

        return "failure"
        

    ############################
    #      Helper Functions    #
    ############################

    def euclidean_distance(self, city_1, city_2):
        if type(city_1) == str:
            city_1 = self.mapping.get_city_object(city_1)
        if type(city_2) == str:
            city_2 = self.mapping.get_city_object(city_2)
        
        # Get lat point one and two
        lat_coord_1 = city_1.get_lat().split(' ')
        lat_coord_2 = city_2.get_lat().split(' ')
        
        lat_1 = int(lat_coord_1[0])
        lat_2 = int(lat_coord_2[0])
        
        # Get lon point one and two
        lon_coord_1 = city_1.get_lon().split(' ')
        lon_coord_2 = city_2.get_lon().split(' ')
        
        lon_1 = int(lon_coord_1[1])
        lon_2 = int(lon_coord_2[1])

        return math.sqrt((lat_2 - lat_1) ** 2 + (lon_2 - lon_1) ** 2)
    
    