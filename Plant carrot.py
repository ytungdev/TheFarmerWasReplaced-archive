def walk(x,y):
	if x+1 == get_world_size():
		move(North)
	move(East)

x1,y1,x2,y2 = 0,0,5,5
def in_carrot_field(x,y):
	return (x>=x1) and (x<=x2) and (y>=y1) and (y<=y2)

def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)

def harvest_carrot():
	if can_harvest():
		harvest()
		plant_carrot()


def main():
	x,y = get_pos_x(), get_pos_y()
	harvest_carrot()
	walk(x,y)
	
if __name__ == '__main__':
	clear()
	while True:
		main()
	