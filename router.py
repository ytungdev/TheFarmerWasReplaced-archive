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
def next():
	x,y = get_pos_x(), get_pos_y()
	dir = route[y][x]
	move(idx[dir])