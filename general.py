def harvest_reset():
	harvest_all()
	clear()

def harvest_all():
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			harvest()
			move(East)
		move(North)
			

def go_to(x,y):
	x_diff = x - get_pos_x()
	y_diff = y - get_pos_y()
	x_dir = East
	y_dir = North
	
	if x_diff < 0 :
		x_dir = East
 
	if y_diff < 0:
		y_dir = South

	for i in range(abs(x_diff)):
		move(x_dir)
	for j in range(abs(y_diff)):
		move(y_dir)
		