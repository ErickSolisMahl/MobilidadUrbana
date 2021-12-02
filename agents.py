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

  def move(self):
  
    if self.orientation == 0:
      next_move = (self.pos[0] + 1, self.pos[1])
      self.model.grid.move_agent(self, next_move)

    if self.orientation == 1:
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
  
  def check_next_cell(self):
    print("Estoy checando que hay enfrente")

    if self.orientation == 0:
      print("Este")
      next_cell_position_este = (self.pos[0] + 1, self.pos[1])
      next_cell_contents_este = self.model.grid.get_cell_list_contents([next_cell_position_este])   

      for agent in next_cell_contents_este:
        print("checando que hay en la celda de enfrete")
        if type(agent) is Car:
          print("Hay un carro")

        if type(agent) is Traffic_light:
          if next_cell_contents_este[0].light == 0:
            print("Semaforo Este Rojo")
            self.stop()

          elif next_cell_contents_este[0].light == 1:
            print("Semaforo Este Verde")
            self.move()

    else:
      print("No hay nada lado Este")
      self.move()
        
    if self.orientation == 1:
      print("Oeste")
      next_cell_position_norte = (self.pos[0] , self.pos[1] - 1)
      next_cell_contents_norte = self.model.grid.get_cell_list_contents([next_cell_position_norte])
          
      for agent in next_cell_contents_norte:
        if type(agent) is Car:
          print("Hay un Carro calle Norte")
            
        if type(agent) is Traffic_light:
          if next_cell_contents_norte[0].light == 0:
            print("Semaforo Norte Rojo")
            self.stop()
            
          elif next_cell_contents_norte[0].light == 1:
            print("Semaforo Norte Verde")
            self.move()
            
    else:
      print("No hay nada lado Norte")
      self.move()
                    
        
  

  def stop(self):
    print(" En espera")
    self.waiting_time += 1
    print("Tiempo en espera", self.waiting_time)

  def step(self):
    #self.move()
    self.check_next_cell()
  


class Traffic_light(Agent):
  def __init__(self,pos, model, moore = False, light = 0, working_time = 0, orientation = 0):
    super().__init__(pos,model)
    self.pos = pos
    self.light = 0  # 0 Red, 1 Green
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
    
  