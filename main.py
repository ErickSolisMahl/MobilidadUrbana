
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule

from agents import Car, Traffic_light, Sidewalk
from model import Street


def agent_portrayal(agent):
  
  if agent is None:
    return
  
  portrayal = {}

  if type(agent) is Car:

    if agent.orientation == 0:
      
      portrayal["Shape"] = "resources/car.png"
      portrayal["scale"] = 2
      portrayal["Layer"] = "Car"

    if agent.orientation == 1:
      portrayal["Shape"] = "resources/car_n.png"
      portrayal["scale"] = 3
      portrayal["Layer"] = "Car"
  
  if type(agent) is Traffic_light:

      portrayal["Shape"] = "resources/red_light.png"
      portrayal["scale"] = 1
      portrayal["Layer"] = "Light"
  

  
  if type(agent) is Sidewalk:

    if agent.orientation == 0:
      portrayal["Shape"] = "resources/sidewalk_A.png"
      portrayal["scale"] = 2.5
      portrayal["Layer"] = "Sidewalk"
    
    elif agent.orientation == 1:
      portrayal["Shape"] = "resources/sidewalk_B.png"
      portrayal["scale"] = 1.5
      portrayal["Layer"] = "Sidewalk"



  return portrayal


canvas_element = CanvasGrid(agent_portrayal, 13, 13, 500, 500)
chart_element = ChartModule([{"Label": "Car", "Color": "#AA0000"}])

server = ModularServer(
    Street, [canvas_element, chart_element], " Test"
)

server.port = 8521 # 
server.launch()