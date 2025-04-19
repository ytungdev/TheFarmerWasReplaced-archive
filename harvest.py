import plant

pumpkin_count = 0
pumpkin_target = 16

def here(type):
	if type == Items.Pumpkin:
		if pumpkin_count == pumpkin_target:
			harvest()
		if can_harvest():
			pumpkin_count += 1
		plant(Entities.Pumpkin)
		return
	harvest()
	plant.here(type)
		
	
	
	