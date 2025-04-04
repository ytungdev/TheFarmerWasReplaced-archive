def check_crop(x,y):
	if y <= 1:
		return Entities.Carrot
	else:
		return Entities.Tree
	return Entities.Grass
	
def plant_crop(x,y,crop):
	if crop == Entities.Carrot:
		if get_ground_type() != Grounds.soil:
			till()
		plant(Entities.Carrot)
	if crop == Entities.Tree:
		if (x+y)%2 == 0:
			plant(Entities.Tree)

def follow_route(x,y):
	if x+1 == get_world_size():
		move(North)
	move(East)

def farm():
	x,y = get_pos_x(),get_pos_y()
	if can_harvest():
		harvest()
		plant_crop(x,y,check_crop(x,y))
	follow_route(x,y)

def run():
	clear()
	init = 0
	while True:
		if init == 0:
			for i in range(get_world_size()**2):
				x,y = get_pos_x(), get_pos_y()
				crop = check_crop(x,y)
				plant_crop(x,y,crop)	
				follow_route(x,y)
			init = 1
		farm()
		
run()