import math
from mesa import Agent

class Car(Agent):
  def __init__(self, pos, model, moore = False, length = 0, can_move = True, waiting_time = 0, orientation = 0):
    super().__init__(pos,model)
    self.pos = pos
    self.moore = moore
    self.length = length
    self.can_move = can_move
    self.waiting_time = waiting_time
    self.orientation = orientation

  def move(self):
    print("¿Me puedo mover?", self.can_move)
    if self.can_move == True and self.length < 1:
      
      if self.orientation == 0:
        next_move = (self.pos[0] + 1, self.pos[1])
        self.model.grid.move_agent(self, next_move)

      if self.orientation == 1:
        next_move = (self.pos[0], self.pos[1] - 1)
        self.model.grid.move_agent(self, next_move)
 

  def check_next_cell(self):
    
    if self.orientation == 0:
      print("")
      print("Infomracion Calle Este:")
      next_cell_position_este = (self.pos[0] + 1, self.pos[1])
      next_cell_contents_este = self.model.grid.get_cell_list_contents([next_cell_position_este])
      
      this_cell = self.model.grid.get_cell_list_contents([next_cell_position_este])
      
      if len(this_cell) < 1:
        self.can_move = True
        self.length = 0
        


      for agent in next_cell_contents_este:
        #print("checando que hay en la celda de enfrete")
        if type(agent) is Car:
          print("Hay un carro calle Este")
          self.length = 1
          self.waiting_time += 1
          self.can_move = False

        if type(agent) is Traffic_light:
          if next_cell_contents_este[0].light == 0:
            print("Semaforo Este Rojo")
            self.can_move = False
            self.waiting_time += 1
            print("Tiempo espera Este: ", self.waiting_time)

          elif next_cell_contents_este[0].light == 1:
            print("Semaforo Este Verde")
            self.model.grid.move_agent(self, next_cell_position_este)
    
      
      #self.move()
      
        
    if self.orientation == 1:
      print("")
      print("Informacion Calle Norte:")
      next_cell_position_norte = (self.pos[0] , self.pos[1] - 1)
      next_cell_contents_norte = self.model.grid.get_cell_list_contents([next_cell_position_norte])
      
      this_cell = self.model.grid.get_cell_list_contents([next_cell_position_norte])
      
      if len(this_cell) < 1:
        self.can_move = True
        self.length = 0

      for agent in next_cell_contents_norte:
        if type(agent) is Car:
          print("Hay un Carro calle Norte")
          self.length = 1
          self.waiting_time += 1
          self.can_move = False
            
        if type(agent) is Traffic_light:
          if next_cell_contents_norte[0].light == 0:
            print("Semaforo Norte Rojo")
            self.can_move = False
            self.waiting_time += 1
            print("Tiempo  Espera Norte:", self.waiting_time)
            
          elif next_cell_contents_norte[0].light == 1:
            print("Semaforo Norte Verde")
            self.model.grid.move_agent(self, next_cell_position_norte)
            
      
    
    self.move()
      
  def step(self):
    self.check_next_cell()
   

class Traffic_light(Agent):
  def __init__(self,pos, model, moore = False, light = 0, working_time = 0, orientation = 0):
    super().__init__(pos,model)
    self.pos = pos
    self.light = 0  # 0 Red, 1 Green
    self.working_time = working_time
    self.orientation = orientation

  def green_light(self):
    self.light = 1
  
  def red_ligth(self):
    self.light = 0
    

  def density(self):
    time_este = 0
    time_norte = 0
  

    if self.orientation == 0:
      print("Semaforo Este esta en" ,self.light)
      times = []
      total_time = 0
      list = [(0,5), (1,5), (2, 5), (3, 5), (4, 5)]
      trafic_list = self.model.grid.get_cell_list_contents(list)
      count = len(trafic_list)
      for car in trafic_list:
        
        car_time = car.waiting_time
        print("Car waiting Time Este: ",car.waiting_time)
        times.append(car_time)
        total_time += car_time
        
  
      
      print("Carros en la calle Este:", count)
      print("Tiempo total en espera Este: ", total_time)
      print("")
      time_este = total_time

      if time_este > time_norte:
        self.green_light()
      if time_este < time_norte:
        self.red_ligth()
      if time_este == time_norte:
        self.red_ligth()

    
    if self.orientation == 1:
      print("Semaforo Norte esta en" ,self.light)
      times = []
      total_time = 0
      list = [(6, 12), (6,11), (6,10), (6,9), (6, 8), (6,7)]
      trafic_list = self.model.grid.get_cell_list_contents(list)
      count = len(trafic_list)
      
      for car in trafic_list:
        self.working_time = car.waiting_time
        print("Car waitig time Norte:", car.waiting_time)
        times.append(self.working_time)
        total_time += self.working_time

      print("Carros en la calle Norte:", count)
      print("Tiempo total en espera Norte:", total_time)
      print("")
      time_norte = total_time

      if time_norte > time_este:
        self.green_light()
      if time_norte < time_este:
        self.red_ligth()
      if time_norte == time_este:
        self.red_ligth()
        
      
    
          


  def step(self):
    self.density()
    


class Sidewalk(Agent):
  
  def __init__(self,pos,model, moore = False, orientation = 0):
    super().__init__(pos,model)
    self.pos = pos
    self.orientation = orientation
  
  #def step(self):
    
  