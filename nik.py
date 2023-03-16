import pygame

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Defina o título da janela
pygame.display.set_caption("Viagem para o Lar")

# Defina a cor de fundo da tela
background_color = (255, 255, 255)

# Crie o jogador
player_width = 50
player_height = 50
player_x = (screen_width - player_width) / 10
player_y = screen_height - player_height
player_speed = 0
player_gravity = 0.5
#player_jump_speed = -10
player_flying_speed = -5  # velocidade constante enquanto a tecla espaço estiver pressionada
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Defina o relógio para controlar a taxa de atualização da tela
clock = pygame.time.Clock()

# Crie um loop para manter o jogo em execução
running = True
while running:
    # Verifique se algum evento aconteceu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpe a tela com a cor de fundo
    screen.fill(background_color)

    # Verifique se o jogador pulou
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_speed = player_flying_speed
    else:
        player_speed += player_gravity

    # Atualize a posição do jogador com base na velocidade vertical atual
    player.y += player_speed

    # Limitar o movimento do jogador ao espaço da tela
    if player.y > screen_height - player_height:
        player.y = screen_height - player_height
        player_speed = 0
    if player.y < 0:
        player.y = 0
        player_speed = 0

    # Desenhe o jogador na tela
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Atualize a tela
    pygame.display.flip()

    # Defina a taxa de atualização da tela
    clock.tick(60)

# Encerre o Pygame
pygame.quit()
