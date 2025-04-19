import movement
import general




def plant_here():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)
	
def plant_in(x1,y1,x2,y2):
	movement.walk_region(x1,y1,x2,y2,plant_here)

def harvest_largest(x1,y1,x2,y2):
	w,h = x2-x1+1, y2-y1+1
	map = [[0 for i in range(w)] for j in range(h)]

	movement.go_to(x1,y1)
	1_max_petals = 0
	2_max_petals = 0
	n = (x2-x1+1)*(y2-y1+1)
	for i in range(n):
		petals = measure()
		quick_print(i,petals)
		if petals > max_petals:
			max_petals = petals
			loc_x,loc_y = get_pos_x(),get_pos_y()
		movement.follow_path(x1,y1,x2,y2)
	movement.go_to(loc_x,loc_y)
#	if not can_harvest():
#		use_item(Items.Fertilizer)
	while not can_harvest():
		do_a_flip()
	harvest()
	plant(Entities.Sunflower)


def field(x1,y1,x2,y2):
	plant_in(x1,y1,x2,y2)
	while True:
		harvest_largest(x1,y1,x2,y2)
		movement.follow_path(x1,y1,x2,y2)


def fill():
	n = get_world_size()-1
	field(0,0,n,n)
	
if __name__ == '__main__':
	general.harvest_reset()
	#field(0,0,4,1)
	fill()