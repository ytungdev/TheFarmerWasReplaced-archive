def here(type):
	if type == Items.Wood:
		x,y = get_pos_x(), get_pos_y()
		if (x+y)%2:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		return
	if type == Items.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		return
	if type == Items.Pumpkin:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		return
		
	