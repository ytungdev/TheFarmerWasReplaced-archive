import movement
import general
import util

def plant_here():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)
	return measure()
	
map = []
def plant_in(x1,y1,x2,y2):
	global map
	w,h = x2-x1+1, y2-y1+1
	movement.go_to(x1,y1)
	for i in range(h):
		row = []
		for j in range(w):
			size = plant_here()
			row.append(size)
			movement.follow_path(x1,y1,x2,y2)
		map.append(row)
	for r in map:
		quick_print(r)

def sort_row(y):
	x = get_pos_x()
	cont = True
	movement.go_to(0,y)
	while cont:
		cont = False		
		for i in range(get_world_size()-1):
			this = measure()
			that = measure(East)
			quick_print('r:',map[y])
			if this > that:
				cont = True
				swap(East)
				map[y][i], map[y][i+1] = map[y][i+1], map[y][i]
			move(East)
		move(East)
		quick_print('r:',map[y])
	quick_print("r:done")

def sort_col(x):
	y = get_pos_y()
	cont = True
	movement.go_to(x,0)
	while cont:
		cont = False		
		for i in range(get_world_size()-1):
			this = measure()
			that = measure(North)
			quick_print('c:',map[y])
			if this > that:
				cont = True
				swap(North)
				map[i][x], map[i+1][x] = map[i+1][x], map[i][x]
			move(North)
		move(North)
		quick_print('c:',map[y])
	quick_print("c:done")
	

def farm():
	n = get_world_size()-1
	plant_in(0,0,n,n)

if __name__ == '__main__':
	farm()
	for i in range(get_world_size()):
		sort_row(i)

	for i in range(get_world_size()):
		sort_col(i)
	harvest()
		
	