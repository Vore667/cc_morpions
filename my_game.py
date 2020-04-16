import pygame
pygame.init()
window = pygame.display.set_mode((600,700))
pygame.display.set_caption("Morpions")

background = pygame.image.load("/home/kali/Documents/Morpions/cc_morpions/Backroung.png")
round = pygame.image.load("/home/kali/Documents/Morpions/cc_morpions/round.png")
cross = pygame.image.load("/home/kali/Documents/Morpions/cc_morpions/croix.png")
board = [[''] * 3 for _ in range(0,3)]

def draw_board(board):

    window.fill([127,114,100])
    window.blit(background,(0,0))

    for y in range(0,3):
        for x in range(0,3):
            if board[y][x] == 'x':
                window.blit(cross, (x * 200 + 50, y * 200 + 50))
            elif board[y][x] == 'o':
                window.blit(round, (x * 200 + 50, y * 200 + 50))

def ask_position(board, turn):

    if pygame.mouse.get_pressed()[0]:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        pos_x = int(mouse_x / 200)
        pos_y = int(mouse_y / 200)

        if turn == "Player1":
            if(board[pos_y][pos_x] == ""):
                board[pos_y][pos_x] = "x"
                turn = "Player2"
            else:
                print("error")
        else:
            if(board[pos_y][pos_x] == ""):
                board[pos_y][pos_x] = "o"
                turn = "Player1"
            else:
                print("error")
    return turn

def end_game(board):
    for p in ['x', 'o']:
        if board[0][0] == p and board[0][1] == p and board[0][2] == p:
            return True
        if board[1][0] == p and board[1][1] == p and board[1][2] == p:
            return True
        if board[2][0] == p and board[2][1] == p and board[2][2] == p:
            return True
        if board[0][0] == p and board[1][0] == p and board[2][0] == p:
            return True
        if board[0][1] == p and board[1][1] == p and board[2][1] == p:
            return True
        if board[0][2] == p and board[1][2] == p and board[2][2] == p:
            return True
        if board[0][0] == p and board[1][1] == p and board[2][2] == p:
            return True
        if board[0][2] == p and board[1][1] == p and board[2][0] == p:
            return True
    return False

leave = False
turn = "Player1"

while not leave:
    turn = ask_position(board,turn)
    leave = end_game(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
        if event.type == pygame.MOUSEBUTTONUP:
            print("PRESSED")

    window.fill([127,114,100])
    window.blit(background, (0,0))
    draw_board(board)
    pygame.display.update()

pygame.quit()
quit()
                
                    

