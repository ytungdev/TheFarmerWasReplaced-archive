def harvest_reset():
	harvest_all()
	clear()

def harvest_all():
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			harvest()
			move(East)
		move(North)
			

def fill_with(entity):
	def plant_here(entity):
			if not plant(entity):
				till()
				plant(entity)
	
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			plant_here(entity)
			move(East)
		move(North)

def get_loc():
	return get_pos_x(), get_pos_y()

def back(NESW):
	back = {North:South,East:West,
		South:North,West:East}
	move(back[NESW])
			
		