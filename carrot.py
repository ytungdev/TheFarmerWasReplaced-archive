import movement
import general

def plant_here():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)
	
def plant_in(x1,y1,x2,y2):
	movement.walk_region(x1,y1,x2,y2,plant_here)

def field(x1,y1,x2,y2):
	plant_in(x1,y1,x2,y2)
	while True:
		if can_harvest():
			harvest()
		plant_here()
		movement.follow_path(x1,y1,x2,y2)

def fill():
	n = get_world_size()-1
	field(0,0,n,n)
	
if __name__ == '__main__':
	general.harvest_reset()
	fill()