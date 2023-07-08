# WRITE YOUR SOLUTION HERE:
class WeatherStation:

    def __init__(self, name: str):
        self.__name = name
        self.__observations = []

    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def latest_observation(self):
        if(len(self.__observations) > 0):
            return self.__observations[-1]
        else:
            return "no observations"
    
    def number_of_observations(self):
        return len(self.__observations)
    
    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"
    
### Example solution
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observations = 0
        self.__latest_observation = ""
 
    def add_observation(self, observation: str):
        self.__latest_observation = observation
        self.__observations += 1
 
    def latest_observation(self):
        return self.__latest_observation
 
    def number_of_observations(self):
        return self.__observations 
 
    def __str__(self):
        return f"{self.__name}, {self.__observations} observations"