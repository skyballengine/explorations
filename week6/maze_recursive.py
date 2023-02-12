def find_gold(maze, position):
    """
    maze is a list of lists that represents a square maze
    ' ' is an empty square
    '#' is a wall
    'G' is where the gold is hidden
    position is a tuple of the current row and column

    returns a list of coordinates that leads to the gold
    """
    for ls in maze:
        print(ls, end="\n")
    row, col = position  # tuple unpacking
    if row < 0 or row >= len(maze):  # base case for row out of bounds
        return None
    if col < 0 or col >= len(maze[row]):  # base case for column out of bounds
        return None
    if maze[row][col] == '#':  # base case for hitting a wall
        return None
    if maze[row][col] == '.':  # base case for repeating a position
        return None
    if maze[row][col] == 'G':  # base case for finding the goal
        return [(row, col)]

    maze[row][col] = '.'  # mark current square to avoid revisiting
    partial_route = find_gold(maze, (row-1, col))  # try "up"
    if partial_route is not None:
        maze[row][col] = ' '  # unmark current square
        return [(row, col)] + partial_route
    partial_route = find_gold(maze, (row+1, col))  # try "down"
    if partial_route is not None:
        maze[row][col] = ' '  # unmark current square
        return [(row, col)] + partial_route
    partial_route = find_gold(maze, (row, col-1))  # try "left"
    if partial_route is not None:
        maze[row][col] = ' '  # unmark current square
        return [(row, col)] + partial_route
    partial_route = find_gold(maze, (row, col+1))  # try "right"
    if partial_route is not None:
        maze[row][col] = ' '  # unmark current square
        return [(row, col)] + partial_route
    maze[row][col] = ' '  # unmark current square


maiz = [[' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '#'],
        [' ', '#', ' ', '#', ' ', ' '],
        ['G', '#', '#', '#', '#', ' ']]

print(find_gold(maiz, (0,0)))
