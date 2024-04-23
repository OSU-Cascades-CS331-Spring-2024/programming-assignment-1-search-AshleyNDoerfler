class Mapping:
    
    def __init__(self):
        self.city_map = {}

    def add_city(self, city, connections):
        self.city_map[city] = connections
    
    def get_citys_connections(self, city_name):
        for city_obj in self.city_map:
            if city_obj.get_name() == city_name:
                return self.city_map[city_obj]
        else:
            return 
        
    def get_city(self, city_name):
        for city_obj in self.city_map:
            if city_obj.get_name() == city_name:
                return city_obj
        else:
            return
        
    def set_cities_as_objects(self):
        new_connections = []

        # For each city in the city map
        for city, connections in self.city_map.items():
            print(connections) # For testing purposes, delete later
            # For each connection in the city's connections
            for connection in connections:
                print(connection) # For testing purposes, delete later
                connected_city_object = self.get_city(connection)
                
                if connected_city_object:
                    cost = connections[connection]
                    new_connections.append([connected_city_object, cost])
            # Set the city's connections to the new connections list
            self.city_map[city] = new_connections
            new_connections = []
        print(self.city_map) # For testing purposes, delete later

    def __str__(self):
        return str(self.city_map)