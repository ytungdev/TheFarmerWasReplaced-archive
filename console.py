import general
import movement
import cactus

dirs = [North, East, South, West
opt = []
def options()
	for dir in dirs:
		if move(dir):
			opt.append(dir)
			move(South)	
	

	quick_print(opt)
options()