import movement
import general
import util

def plant_here():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)
	return measure()
	
locs = {}
vals = []
count = 0
def plant_in(x1,y1,x2,y2):
	global count
	global locs
	global vals
	w,h = x2-x1+1, y2-y1+1
	movement.go_to(x1,y1)
	for i in range(h):
		for j in range(w):
			petals = plant_here()
			count += 1
			vals.append(petals)
			arr = util.get(locs,petals, [])
			arr.append((get_pos_x(), get_pos_y()))
			locs[petals] = arr
			movement.follow_path(x1,y1,x2,y2)
	vals = util.sort(vals)

def pick_max():
	global count
	if count < 1:
		return False
	val = vals.pop()
	loc = locs[val].pop()
	movement.go_to(loc[0],loc[1])
	while not can_harvest():
		do_a_flip()
	harvest()
	count -= 1
	return True
	
def farm():
	n = get_world_size()-1
	plant_in(0,0,n,n)
	cont = True
	while cont:
		cont = pick_max()
	clear()

if __name__ == '__main__':
	general.harvest_reset()
	while True:
		farm()
		
	