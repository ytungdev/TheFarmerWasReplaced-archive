import plant
import movement
import general

idx = {
	'h':Items.Hay,
	'w':Items.Wood,
	'c':Items.Carrot,
	'p':Items.Pumpkin,
}

map = [
	['p','p','p','p','w','w'],
	['p','p','p','p','w','w'],
	['p','p','p','p','w','w'],
	['p','p','p','p','w','w'],
	['c','c','c','c','h','h'],
	['c','c','c','c','h','h'],
]

def check():
	x,y = get_pos_x(), get_pos_y()
	return idx[map[y][x]]

while True:
	for r in map:
		for c in r:
			corp = idx[c]
			plant.here(corp)
			movement.follow_path()
	general.harvest_all()

