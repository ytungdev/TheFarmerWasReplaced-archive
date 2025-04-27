import movement

def spawn_maze():
	movement.go_to(0,0)
	plant(Entities.Bush)
	lvl = 2
	n = get_world_size() * lvl
	use_item(Items.Weird_Substance, n)

def solve_maze():
	def options():
		

if __name__ == '__main__':
	
	spawn_maze()
