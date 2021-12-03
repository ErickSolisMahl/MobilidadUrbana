from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from schedule import RandomActivationByBreed

from agents import Car, Traffic_light, Sidewalk



# BaseScheduler has a self.time of int, while
# StagedActivation has a self.time of floa

class Street(Model):
  def __init__(self, height = 13, width = 13, initial_population = 2):

    # Set parameters
    self.height = height
    self.width = width
    self.initial_population = initial_population
    self.schedule = RandomActivationByBreed(self)
    self.grid = MultiGrid(self.height, self.width, torus = True)
    self.running = True

    self.datacollector = DataCollector(
      model_reporters = {"Street" : Street},
      
    )


  # Create car
    for i in range (self.initial_population):
      x = self.random.randrange(0,5)
      y = 5
      length = 0
      can_move = False
      waiting_time = 0
      orientation = 0
      #is_the_cell_empty = self.grid.is_cell_empty([x,y])
      
      car = Car((x,y), self, False, length, can_move, waiting_time, orientation)
      self.grid.place_agent(car, (x,y))
      self.schedule.add(car)
        
        
      

      #self.running = True
      #self.datacollector.collect(self)

  # Create car
    for i in range (0,1):
      x = 6
      y = self.random.randrange(6, 12)
      length = 0
      can_move = False
      waiting_time = 0
      orientation = 1
      
      car = Car((x,y), self, False, length, can_move, waiting_time, orientation)
      self.grid.place_agent(car, (x,y))
      self.schedule.add(car)


  # Create Trafic_light
    for i in range(0,1):
      x = 5
      y = 5
      light = 0
      working_time = 0
      orientation = 0

      light =  Traffic_light((x,y), self, False, light, working_time, orientation)
      self.grid.place_agent(light, (x,y))
      self.schedule.add(light)

    for i in range(0,1):
      x = 6
      y = 6
      light = 0
      working_time = 0
      orientation = 1

      light =  Traffic_light((x,y), self, False, light, working_time, orientation)
      self.grid.place_agent(light, (x,y))
      self.schedule.add(light)
      
      #self.running = True
      #self.datacollector.collect(self)
  
  # Create sidewalk
    for i in range(0, 5):
      x = 0 + i
      y = 6

      orientation = 0
      sidewalk = Sidewalk((x,y), self, False, orientation)
      self.grid.place_agent(sidewalk, (x,y))
      self.schedule.add(sidewalk)

    for i in range(8, 12):
      x = 0 + i
      y = 6

      orientation = 0
      sidewalk = Sidewalk((x,y), self, False, orientation)
      self.grid.place_agent(sidewalk, (x,y))
      self.schedule.add(sidewalk)
  
    for i in range(0, 5):
      x = 0 + i
      y = 4
      orientation = 0
      sidewalk = Sidewalk((x,y), self, False, orientation)
      self.grid.place_agent(sidewalk, (x,y))
      self.schedule.add(sidewalk)

    for i in range(8, 12):
      x = 0 + i
      y = 4
      orientation = 0
      sidewalk = Sidewalk((x,y), self, False, orientation)
      self.grid.place_agent(sidewalk, (x,y))
      self.schedule.add(sidewalk)

    for i in range(0, 4):
      x = 5 
      y = 0 + i
      orientation = 1
      sidewalk = Sidewalk((x,y), self, False, orientation)
      self.grid.place_agent(sidewalk, (x,y))
      self.schedule.add(sidewalk)

    for i in range(0, 4):
      x = 7 
      y = 0 + i
      orientation = 1
      sidewalk = Sidewalk((x,y), self, False, orientation)
      self.grid.place_agent(sidewalk, (x,y))
      self.schedule.add(sidewalk)

    for i in range(7, 13):
      x = 7 
      y = 0 + i
      orientation = 1
      sidewalk = Sidewalk((x,y), self, False, orientation)
      self.grid.place_agent(sidewalk, (x,y))
      self.schedule.add(sidewalk)

    for i in range(7, 13):
      x = 5 
      y = 0 + i
      orientation = 1
      sidewalk = Sidewalk((x,y), self, False, orientation)
      self.grid.place_agent(sidewalk, (x,y))
      self.schedule.add(sidewalk)
    

  def step(self):
    
    self.schedule.step()
    self.datacollector.collect(self)
    
    