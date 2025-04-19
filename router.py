idx = {
	'u' : North,
	'd' : South,
	'l' : West,
	'r' : East
}

route = [
	['u','r','u','r','r','u'],
	['u','d','u','d','u','l'],
	['u','d','u','d','r','u'],
	['r','d','r','d','u','l'],
	['u','l','u','l','r','u'],
	['u','d','l','d','l','l'],
]
dino_route = [
	['u','l','u','l','l','l'],
	['u','d','u','r','u','d'],
	['u','d','u','d','u','d'],
	['u','d','r','d','u','d'],
	['u','d','l','l','l','d'],
	['r','r','r','r','r','d'],
]

def next(route):
	x,y = get_pos_x(), get_pos_y()
	dir = route[y][x]
	move(idx[dir])