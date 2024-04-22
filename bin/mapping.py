class Mapping:
    
    def __init__(self):
        self.city_map = {}

    def add_city(self, city, lat, lon):
        self.city_map[city] = (lat, lon)