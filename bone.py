import movement

idx = {
	'u' : North,'d' : South,
	'l' : West,	'r' : East
}

dino_route_6 = [
	['r','r','r','r','r','d'],
	['u','d','l','l','l','d'],
	['u','d','r','d','u','d'],
	['u','d','u','d','u','d'],
	['u','d','u','r','u','d'],
	['u','l','u','l','l','l'],
]

dino_route_8 = [
    ['r','r','r','r','r','r','r','d'],
    ['u','d','l','l','l','l','l','d'],
	['u','d','r','r','r','d','u','d'],
	['u','d','u','d','l','d','u','d'],
	['u','d','u','d','u','d','u','d'],
	['u','d','u','d','u','l','u','d'],
	['u','d','u','r','r','r','u','d'],
	['u','l','u','l','l','l','l','l'],
]

def next(route):
	n = get_world_size()-1
	x,y = get_pos_x(), get_pos_y()
	dir = route[n-y][x]
	return move(idx[dir])

def farm(route):
	movement.go_to(0,0)
	change_hat(Hats.Dinosaur_Hat)
	cont = True
	while cont:
		cont = next(route)
	change_hat(Hats.Straw_Hat)

if __name__ == '__main__':
	clear()
	while True:
		farm(dino_route_8)
	