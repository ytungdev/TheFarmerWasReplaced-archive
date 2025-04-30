import movement
import general

def plant_here():
	if get_ground_type() != Grounds.Soil:
		till()
	use_item(Items.Fertilizer)
	plant(Entities.Pumpkin)
	
def plant_in(x1,y1,x2,y2):
	movement.walk_region(x1,y1,x2,y2,plant_here)

def field(x1,y1,x2,y2):
	plant_in(x1,y1,x2,y2)
	steps = (x2-x1+1)*(y2-y1+1)
	count = 0
	walk = 0
	while count < steps:
		walk += 1
		if can_harvest():
			count += 1
		else:
			plant_here()
		if walk == steps:
			if count == steps:
				harvest()
			count = 0
			walk = 0
		movement.follow_path(x1,y1,x2,y2)

def fill():
	n = get_world_size()-1
	field(0,0,n,n)
	
if __name__ == '__main__':
	general.harvest_reset()
	fill()