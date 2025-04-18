import movement

movement.go(1,1)
for i in range(4):
	for j in range(4):
		plant(Entities.Bush)
		move(East)
	move(North)
