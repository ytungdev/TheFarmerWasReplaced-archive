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

## Sunflower
- Given:
    - max when :
        - having 10+ sunflower
        - picking sunflower with highest petals
- Logic:
    - Picking sunflower with highest petals to lowest without replanting
- Implementation:
    - store number of petals `val` in `vals`
    - store array of location with `val` in `locs`, where `locs[val][i] = (x,y)`
    - sort `vals`
    - for each `val[-1]` from sorted `vals` (max val)
        - `val = vals.pop()`
        - `loc = locs[val].pop`
        - harvest at loc

## Dinosaur

```
dino_route_6 = [
	['r','r','r','r','r','d'],
	['u','d','l','l','l','d'],
	['u','d','r','d','u','d'],
	['u','d','u','d','u','d'],
	['u','d','u','r','u','d'],
	['u','l','u','l','l','l'],
]

dino_route_8 = [
    ['r','r','r','r','r','r','r','d'],
    ['u','d','l','l','l','l','l','d'],
	['u','d','r','r','r','d','u','d'],
	['u','d','u','d','l','d','u','d'],
	['u','d','u','d','u','d','u','d'],
	['u','d','u','d','u','l','u','d'],
	['u','d','u','r','r','r','u','d'],
	['u','l','u','l','l','l','l','l'],
]
```
