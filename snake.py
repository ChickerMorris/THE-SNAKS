#snake game
#Author Zachary Morris
#curses is framework (Detail) to help make the game
#poping removes from an entity, pushing adds to an entity
	#importing all imports
import random
import curses
#creating scrolling
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
#creating new window
w = curses.newwin(sh, sw, 0, 0)
#create a keypad entry
w.keypad(1)
w.timeout(100)

#numerical values to size where the snake is
snk_x = sw/4
snk_y = sh/2
#create snake starting position
snake =[
	[snk_y, snk_x],
	[snk_y, snk_x-1],
	[snk_y, snk_x-2]
]

#creates food
food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)#makes the food shaped like PI

#adds right key functionallity
key = curses.KEY_RIGHT

#loop for movement, eating food, and ending game
while True:
	next_key = w.getch()
	key = key if next_key == -1 else next_key
	
	if snake [0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1]:
		curses.endwin()
		quit()
	#creates snake
	new_head = [snake[0][0], snake[0][1]]

	if key == curses.KEY_DOWN:
		new_head [0] += 1
		new_head[snake[0][0], snake[0][1]]
	if key == curses.KEY_UP:
		new_head [0] -= 1
		new_head[snake[0][0], snake[0][1]]
	if key == curses.KEY_LEFT:
		new_head [0] -= 1
		new_head[snake[0][0], snake[0][1]]
	if key == curses.KEY_RIGHT:
		new_head [0] += 1
	snake.insert(0, new_head)
	#check if snake has eaten food
	if snake[0] == food:
		food == None
		while food is None:
			nf = [
				random.randiant(1, sh-1),
				random.randiant(1, sw-1)
			]
			food = nf if nf not in state else None
		#create another food
		w.addch[food[0], food[1], curses.ACS_PI]
	else:
		tail = snake.pop()
		w.addch(tail[0], tail[1], ' ')

	w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)


