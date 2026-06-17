current_player = "X"
stop = False
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-",
]

def play(position):
    global current_player
    
    # Validar que la posición esté dentro del tablero (0 a 8)
    if position < 0 or position > 8:
        print("Invalid position! Choose between 0 and 8.")
        return False

    # Validar si el espacio ya está ocupado
    if board[position] != "-":
        print("That position is already taken! Try another one.")
        return False

    # Guardar la jugada en el tablero
    board[position] = current_player
    
    # Verificar si esta jugada causó una victoria
    if check_for_winner():
        print_board()
        print(f"🎉 Player {current_player} wins the game! 🎉")
        new_game()
        return True

    # Verificar si hay un empate (no quedan espacios vacíos)
    if "-" not in board:
        print_board()
        print("🤝 It's a tie!")
        new_game()
        return True

    # Cambiar de turno automáticamente
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    
    return True

def check_for_winner():
    # Definimos las combinaciones individualmente para evitar errores de sintaxis
    r1 = [0, 1, 2]
    r2 = [3, 4, 5]
    r3 = [6, 7, 8]
    c1 = [0, 3, 6]
    c2 = [1, 4, 7]
    c3 = [2, 5, 8]
    d1 = [0, 4, 8]
    d2 = [2, 4, 6]
    
    winning_combinations = [r1, r2, r3, c1, c2, c3, d1, d2]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "-":
            return True
            
    return False

def new_game():
    global current_player, board
    print("🔄 Starting a new game...")
    board = ["-"] * 9
    current_player = "X"

def print_board():
    print(f"""
    Current board ({current_player} turn):

    [{board[0]}] [{board[1]}] [{board[2]}]
    [{board[3]}] [{board[4]}] [{board[5]}]
    [{board[6]}] [{board[7]}] [{board[8]}]
    """)

# Mostrar el tablero por primera vez al iniciar
print_board()

while stop == False:
    command = input("What do you want?: ").strip().lower()

    if command == "stop":
        print("Goodbye! Thanks for playing.")
        stop = True
        
    elif command == "new_game":
        new_game()
        print_board()
        
    elif command.startswith("play "):
        try:
            position = int(command.split()[1])
            play(position)
            if not stop:
                print_board()
        except (IndexError, ValueError):
            print("Format incorrect! Use 'play <number>' (e.g., play 3)")
            
    else:
        print("Unknown command. Valid options: 'play <0-8>', 'new_game', 'stop'")
