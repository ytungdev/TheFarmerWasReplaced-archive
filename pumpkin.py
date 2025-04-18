import movement

def plant_pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)
	
def plant_pumpkin_in(x1,y1,x2,y2):
	movement.walk_region(x1,y1,x2,y2,plant_pumpkin)
	
	
def pumpkin_field(x1,y1,x2,y2):
	plant_pumpkin_in(0,0,5,5)
	
if __name__ == '__main__':
	plant_pumpkin_in(0,0,5,5)
	steps = 25
	count = 0
	walk = 0
	while count < steps:
		walk += 1
		if can_harvest():
			count += 1
		else:
			plant_pumpkin()
		if walk == steps:
			if count == steps:
				harvest()
			count = 0
			walk = 0
		movement.move_in_range(0,0,5,5)