import general
import movement


NESW = [North, East, South, West]
oppo ={North:South,East:West,
		South:North,West:East}

split=[]
actions = []
step=0


def explore():
	if get_entity_type() != Entities.Hedge:
		return
	opts=[]
	# find possible path
	for dir in NESW:
		if step > 0:
			last = oppo[actions[-1]]
			if dir != last:		
				if move(dir):
					general.back(dir)
					opts.append(dir)
		else:
			if move(dir):
				general.back(dir)
				opts.append(dir)						
	# deadend
	if not opts:
        quick_print('!!! dead end !!!')
        if split:
            dest = split.pop()
            while step > dest:
                backward()
        else:
            quick_print('no exit')
            return
            
    # cache split
    if len(opts) > 1:
        split.append(step)
	# explore next
    for opt in opts:
		forward(opt)
		explore()

def forward(dir):
	global step
	move(dir)
	quick_print('  ',get_entity_type())
	if get_entity_type() == Entities.Treasure:
		quick_print('!!!!!!!!!!!!!!!!!!')
		#add_substance()
		harvest()
		clear()
	else:
		step+=1
		actions.append(dir)
	return False

def backward():
	global step
	dir = actions.pop()
	general.back(dir)
	step-=1
	quick_print('  step:',step)

def spawn_maze():
	movement.go_to(0,0)
	plant(Entities.Bush)
	add_substance()
	
def add_substance():
	n = get_world_size() * num_unlocked(Unlocks.Mazes)
	use_item(Items.Weird_Substance, n)


if __name__ == '__main__':
	while True:
		spawn_maze()
		explore()