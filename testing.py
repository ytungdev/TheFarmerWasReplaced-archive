import general
import movement

import pumpkin
import carrot
import bush

blueprint = {
	Entities.Pumpkin:[0,0,3,3]
}

for corp in blueprint:
	f = blueprint[corp]
	pumpkin.plant_in(f[0],f[1],f[2],f[3])