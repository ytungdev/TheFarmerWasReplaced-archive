def walk(x,y):
	if x+1 == get_world_size():
		move(North)
	move(East)

x1,y1,x2,y2 = 0,0,5,5
def in_pumpkin_field(x,y):
	return (x>=x1) and (x<=x2) and (y>=y1) and (y<=y2)

def plant_pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)

pumpkin_count = 0
min_size = 9
def harvest_pumpkin():
	global pumpkin_count
	if can_harvest():
		if pumpkin_count >= min_size:
			harvest()
			pumpkin_count = 0
		else:
			pumpkin_count += 1
	crop = get_entity_type()
	if crop == None or crop == Entities.Grass:
		plant_pumpkin()

def main():
	x,y = get_pos_x(), get_pos_y()
	if in_pumpkin_field(x,y):
		harvest_pumpkin()
	walk(x,y)
		
while True:
	main()
	