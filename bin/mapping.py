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

    def __str__(self):
        return str(self.city_map)