def walk(x,y):
	if x+1 == get_world_size():
		move(North)
	move(East)

def plant_it(crop):
	plant(crop)

def harvest_it(crop):
	if can_harvest():
		harvest()
		plant_it(crop)

def farm_it(crop):
	x,y = get_pos_x(), get_pos_y()
	harvest_it(crop)
	walk(x,y)

if __name__ == '__main__':
	clear()
	while True:
		farm_it(Entities.Bush)
		