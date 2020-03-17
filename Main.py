import Game
import os

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def main():
	game = Game.Hanoi(3)
	game.print_board()

	while (True):
		print("Move ring from: ", end=" ")
		source = int(input()) - 1
		print("Move ring to: ", end=" ")
		destination = int(input()) - 1
		game.make_move(source, destination)
		clear_screen()
		game.print_board()
		if(game.check_victory()):
			print("You win!")
			break


if __name__ == "__main__":
    main()
