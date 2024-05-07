import pandas as pd

class Airport:
    def __init__(self) -> None:
        self.__cod_airport = None
        self.__name = None
        self.__city = None
        self.__country = None
        self.__latitude = None
        self.__longitude = None
        self.__distance = None
    
    def get_cod_airport(self):
        return self.__cod_airport
    def set_cod_airport(self, cod_airport):
        self.__cod_airport = cod_airport
    
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_city(self):
        return self.__city
    def set_city(self, city):
        self.__city = city
    
    def get_country(self):
        return self.__country
    def set_country(self, country):
        self.__country = country
    
    def get_latitude(self):
        return self.__latitude
    def set_latitude(self, latitude):
        self.__latitude = latitude
    
    def get_longitude(self):
        return self.__longitude
    def set_longitude(self, longitude):
        self.__longitude = longitude
    
    
    def get_distance(self):
        return self.__distance
    def set_distance(self, distance):
        self.__distance = distance
    
    def create_airport_origin(self, airport_info:'pd.DataFrame', distance):
        self.set_cod_airport(airport_info['Source']) 
        self.set_name(airport_info['Source Airport Name'])
        self.set_city(airport_info['Source Airport City'])
        self.set_country(airport_info['Source Airport Country'])
        self.set_latitude(airport_info['Source Airport Latitude'])
        self.set_longitude(airport_info['Source Airport Longitude'])
        self.set_distance(distance)

    def create_airport_target(self, airport_info:'pd.DataFrame', distance):
        self.set_cod_airport(airport_info['Destination']) 
        self.set_name(airport_info['Destination Airport Name'])
        self.set_city(airport_info['Destination Airport City'])
        self.set_country(airport_info['Destination Airport Country'])
        self.set_latitude(airport_info['Destination Airport Latitude'])
        self.set_longitude(airport_info['Destination Airport Longitude'])
        self.set_distance(distance)
    