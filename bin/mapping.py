class Mapping:
    
    def __init__(self):
        self.city_map = {}
        self.lat_pos = 0
        self.lon_pos = 1
        self.connections_pos = 2

    def add_city(self, city, lat, lon, connections):
        self.city_map[city] = (lat, lon, connections)

    def get_citys_lat(self, city):
        return self.city_map[city][self.lat_pos]
    
    def get_citys_lon(self, city):
        return self.city_map[city][self.lon_pos]
    
    def get_citys_connections(self, city):
        return self.city_map[city][self.connections_pos]