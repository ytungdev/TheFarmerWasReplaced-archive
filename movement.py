direction = {
	'x':{'+':East,
		'-':West},
	'y':{'+':North,
		'-':South}
}
sign = ['+','-']


def follow_path(x1=0,y1=0,x2=get_world_size()-1,y2=get_world_size()-1):
	curr_x,curr_y = get_pos_x(),get_pos_y()
	if curr_x > x2 or curr_x < x1:
		go_to(x1,y1)
	if curr_y > y2 or curr_y < y1:
		go_to(x1,y1)
	
	# last col
	if curr_x == x2:
		# last row
		if curr_y == y2:
			go_to(x1,y1)
		else:
			go_to(x1,curr_y+1)
	else:
		move(direction['x']['+'])

def s_path(x1=0,y1=0,x2=get_world_size()-1,y2=get_world_size()-1):
	curr_x,curr_y = get_pos_x(),get_pos_y()
	if curr_x > x2 or curr_x < x1:
		go_to(x1,y1)
	if curr_y > y2 or curr_y < y1:
		go_to(x1,y1)
	
	# check odd row
	if (curr_y - y1)%2:
		last_col = x1
		forward = '-'
	else:
		last_col = x2
		forward = '+'
	
	# last col
	if curr_x == last_col:
		# last row
		if curr_y == y2:
			go_to(x1,y1)
			return				
		move(direction['y']['+'])
	else:
		move(direction['x'][forward])

def walk_region(x1,y1,x2,y2,fn):
	go_to(x1,y1)
	for j in range(y2-y1+1):
		for i in range(x2-x1):
			fn()
			move(direction['x'][sign[j%2]])
		fn()
		move(direction['y']['+'])
	go_to(x1,y1)

def go_to(x,y):
	x_diff = x - get_pos_x()
	y_diff = y - get_pos_y()
	
	if x_diff > 0:
		x_sign = '+'
	else:
		x_sign = '-'
 
	if y_diff > 0:
		y_sign = '+'
	else:
		y_sign = '-'

	for i in range(abs(x_diff)):
		move(direction['x'][x_sign])
	for j in range(abs(y_diff)):
		move(direction['y'][y_sign])