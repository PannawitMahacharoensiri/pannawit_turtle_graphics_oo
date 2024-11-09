? How to run my program
  ->   run "polygon_art.py" in IDE or etc. inside it will ask for user input after insert in will do the task itself

-----------------------------
MY WORKFLOW
User & outside class : only pick choice from PolygonArt
class PolygonArt : manager receive the choice from user then use that to build all data by itself inside the class after that  sent data to Polygon and EmbeddedPolygon(Polygon) to perform , also determind how many times to draw
class Polygon : artist only draw(perform) only ,wait to get call from PolygonArt
class EmbeddedPolygon(Polygon) : side kick only work with Polygon also wait to get call from PolygonArt

-----------------------------
Conclusion : Correctly implemented all the code and doesn't found any bugs yet (assume that user will only pick 1-9)

