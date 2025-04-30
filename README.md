# TheFarmerWasReplaced-archive

## Functions
- Actions
    - clear()
    - do_a_flip()
    - till()
    - harvest()
    - move()
    - plant()
    - print()/quick_print()
    - use_item()
    - swap()
    - change_hat()
- Detect
    - can_harvest() -> bool
    - get_pos_x()/get_pos_y()
    - get_world_size()
    - get_entity_type()
    - get_ground_type()
    - get_cost()
    - get_water()
    - measure()
- System
    - set_execution_speed()
    - set_world_size()
    - get_cost()
    - unlock()

## Entities

- Grass
    - Ground  : Grassland
    - Cost    : -
    - Item    : Hay
    - Speical : -
- Bush
    - Ground  : Grassland
    - Cost    : -
    - Item    : Wood
    - Special : -
- Carrot
    - Ground  : Soil
    - Cost    : Wood, Hay
    - Item    : Carrot
    - Special : -
- Tree
    - Ground  : Grassland
    - Cost    : -
    - Item    : Wood
    - Special : no adjacent NESW
- Sunflower
    - Ground  : Soil
    - Cost    : Carrot
    - Item    : Wood
    - Special : Multiply if harvest max petal with 10+ sunflower
    - Topic   : sorting/merge sort
- Pumpkin
    - Ground  : Soil
    - Cost    : Carrot
    - Item    : Pumpkin
    - Special : Multiply when formed n^2 square, max at n=5
- Cactus
    - Ground  : Soil
    - Cost    : Pumpkin
    - Item    : Cactus
    - Special : Multiply if all adjacent cacti are sorted
    - Topic   : bubble sort

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

## Maze
- Logic:
    - Use `step=0` to track state
    - Use `split=[]` to track state of splits
    - Use `actions=[]` to track sequnce of actions
    - `explore()`: explore the map and find treasure
        - find possible path at current cell as `options`
            - ignore last cell where we come from
        - if `len(options)` == 0: encounter dead end
            - `go_backward()` untill reaching state of last split
        - else: next state is possible
            - if `len(options)` > 1: encounter split
                - mark the current state and `split.append(step)`
            - for each `opt` in `options`:
                - `go_forward()` and `explore()`
