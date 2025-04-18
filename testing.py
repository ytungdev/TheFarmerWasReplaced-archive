import movement

direction = {
	'x':{
		'+':East,
		'-':West},
	'y':{
		'+':North,
		'-':South
	}
}
signs = ['+','-']

def move_in_range(x1,y1,x2,y2):
	curr_x = get_pos_x()
	curr_y = get_pos_y()
	if curr_x > x2 or curr_x < x1:
		movement.go_to(x1,y1)
	if curr_y > y2 or curr_y < y1:
		movement.go_to(x1,y1)
	
	# check odd row
	if (curr_y - y1)%2:
		last_col = x1
		forward = '-'
		backward = '+'
	else:
		last_col = x2
		forward = '+'
		backward = '-'
	
	# in last row
	if curr_y == y2:
		# last col
		if curr_x == last_col:
			movement.go_to(x1,y1)
			return
	# last col
	if curr_x == last_col:
		move(movement.direction['y']['+'])
	else:
		move(movement.direction['x'][forward])

while True:
	movement.move_in_range(1,1,4,4)
