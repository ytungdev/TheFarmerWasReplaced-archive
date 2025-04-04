def walk(x,y):
	if x+1 == get_world_size():
		move(North)
	move(East)

def plant_it(x,y):
	if (x+y)%2:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

def harvested():
	if can_harvest():
		harvest()
		return True
	return False

def farm_it():
	x,y = get_pos_x(), get_pos_y()
	if harvested():
		plant_it(x,y)
	walk(x,y)
		
while True:
	farm_it()
	