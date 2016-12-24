#dynamic programming solution
#answer: 137846528820

def printGrid(grid):
	for row in grid:
		for elt in row:
			print(elt, end=" ")
		print("\n")

def getPaths(grid, startx, starty, goalx, goaly):
	if startx == goalx and starty == goaly:
		return 1
	if (startx > goalx or starty > goaly):
		return 0
	#look up
	if grid[startx][starty] != 0:
		return grid[startx][starty]
	else:
		grid[startx][starty] = getPaths(grid, startx+1, starty, goalx, goaly) + \
			getPaths(grid, startx, starty+1, goalx, goaly)

		return grid[startx][starty]


def main():
	gridWidth, gridHeight = 20, 20
	grid = [[0 for x in range(gridWidth+1)] for y in range(gridHeight+1)]

	startx, starty = 0, 0
	goalx, goaly = 20,20

	#print('printing grid');
	#printGrid(grid)

	ans = getPaths(grid, startx, starty, goalx, goaly)
	print('answer: ', str(ans))

	#print('printing grid');
	#printGrid(grid)

main()
