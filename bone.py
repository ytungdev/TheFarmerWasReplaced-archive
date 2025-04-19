import movement

idx = {
	'u' : North,'d' : South,
	'l' : West,	'r' : East
}

dino_route_6 = [
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
	return move(idx[dir])

def farm(route):
	movement.go_to(0,0)
	change_hat(Hats.Dinosaur_Hat)
	cont = True
	while cont:
		cont = next(route)
	change_hat(Hats.Straw_Hat)

if __name__ == '__main__':
	while True:
		farm(dino_route_6)
	