import math
from mesa import Agent

class Car(Agent):
  def __init__(self, pos, model, moore = False, length = 0, speed = 0, waiting_time = 0, orientation = 0):
    super().__init__(pos,model)
    self.pos = pos
    self.moore = moore
    self.length = length
    self.speed = speed
    self.waiting_time = waiting_time
    self.orientation = orientation

    
  def maximum_distance(pos_1, pos_2):
    x1, y1 = pos_1
    x2, y2 = pos_2
    dx = x1 - x2
    dy = y1 - y2

    print("")

  def minimum_distance(pos_1, pos_2):
    x1, y1 = pos_1
    x2, y2 = pos_2
    dx = x1 - x2
    dy = y1 - y2

  def move(self):
  
    #next_moves = self.model.grid.get_neighborhood(self.pos, self.moore, True)
    next_move = (self.pos[0] + 1, self.pos[1])
    this_cell = self.model.grid.get_cell_list_contents([self.pos])
    next_cell = self.model.grid.get_cell_list_contents([next_move])
    
  
    #check if there is a Light in the next move
    if self.orientation == 0:
      #print("Estoy en",self.pos)
      for agent in next_cell:
        if type(agent) is Car:
          print("Hay un Carro")
          
        if type(agent) is Traffic_light:
          #print("Posicion",self.pos)
          print("Hay un semaforo en ", agent.pos)
          self.check_light()
          return
        else:
          print("Puedo avanzar!")
      self.model.grid.move_agent(self, next_move)
        
         
          

    elif self.orientation == 1:
      #print(self.pos)
      next_move = (self.pos[0], self.pos[1] - 1)
      self.model.grid.move_agent(self, next_move)


  def check_light(self):
    this_cell = self.model.grid.get_cell_list_contents([self.pos])
    next_move = (self.pos[0] + 1, self.pos[1])
    next_cell = self.model.grid.get_cell_list_contents([next_move])
    print("Esperando cambio de luz")
    for agent in next_cell:
        if type(agent) is Traffic_light:
          if next_cell[0].red_light == True and self.waiting_time < 3:
            print("Luz roja: ", next_cell[0].red_light)
            self.stop()
            print("Tiempo en espera", self.waiting_time)

          else:
            print("Es verde")
            self.model.grid.move_agent(self, next_move)
  

  def stop(self):
    print(" En espera")
    self.waiting_time += 1
    print("Tiempo en espera", self.waiting_time)

  def step(self):
    self.move()
  


class Traffic_light(Agent):
  def __init__(self,pos, model, moore = False, red_light = True, yellow_light = False, green_light = False, working_time = 0, orientation = 0):
    super().__init__(pos,model)
    self.pos = pos
    self.red_light = red_light
    self.yellow_light = yellow_light
    self.green_light = green_light
    self.working_time = working_time
    self.orientation = orientation

  def change_light(self):
    print()

  def density(self):
    if self.orientation == 0:

      list = [(0,5), (1,5), (2, 5), (3, 5), (4, 5)]
      trafic_list = self.model.grid.get_cell_list_contents(list)
      count = len(trafic_list)
      #print(trafic_list)
      print("Carros en la calle Este", count)
    
    if self.orientation == 1:
      list = [(6, 12), (6,11), (6,10), (6,9), (6, 8), (6,7)]
      trafic_list = self.model.grid.get_cell_list_contents(list)
      count = len(trafic_list)
      #print(trafic_list)
      print("Carros en la calle Norte", count)


  def step(self):
    #print("Semaforo Rojo", self.pos)
    self.density()
    


class Sidewalk(Agent):
  
  def __init__(self,pos,model, moore = False, orientation = 0):
    super().__init__(pos,model)
    self.pos = pos
    self.orientation = orientation
  
  #def step(self):
    
  