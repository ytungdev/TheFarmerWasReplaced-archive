# TheFarmerWasReplaced-archive


## Entities


- Grass
    - Ground  : Grassland
    - Cost    : -
    - Harvest : Hay
    - Speical : -
- Bush
    - Ground  : Grassland
    - Cost    : -
    - Harvest : Wood
    - Special : -
- Tree
    - Ground  : Grassland
    - Cost    : -
    - Harvest : Wood
    - Special : no adjacent NESW
- Carrot
    - Ground  : Soil
    - Cost    : Wood, Hay
    - Harvest : Carrot
    - Special : -
- Pumpkin
    - Ground  : Soil
    - Cost    : Carrot
    - Harvest : Pumpkin
    - Special : Multiply when formed n^2 square, max at n=5
- Sunflower
    - Ground  : Soil
    - Cost    : Carrot
    - Harvest : Wood
    - Special : Multiply if harvest max petal with 10+ sunflower

## Route

#### Dinosaur route

- 6x6
```
['r','r','r','r','r','d'],
['u','d','l','l','l','d'],
['u','d','r','d','u','d'],
['u','d','u','d','u','d'],
['u','d','u','r','u','d'],
['u','l','u','l','l','l'],

dino_route = [
	['u','l','u','l','l','l'],
	['u','d','u','r','u','d'],
	['u','d','u','d','u','d'],
	['u','d','r','d','u','d'],
	['u','d','l','l','l','d'],
	['r','r','r','r','r','d'],
]
```
