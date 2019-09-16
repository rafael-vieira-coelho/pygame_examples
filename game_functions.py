import pygame, sys


def verifica_comeu_maça(snake, apple):
    if snake.get_head_position() == apple.position:
        snake.length += 1
        apple.escolhe_posicao_aleatoria()


def desenha_retangulo(color, pos, settings):
    r = pygame.Rect((pos[0], pos[1]), (settings.GRIDSIZE, settings.GRIDSIZE))
    pygame.draw.rect(settings.surface, color, r)


def testa_eventos(event, snake, s):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            snake.point(s.UP)
        elif event.key == pygame.K_DOWN:
            snake.point(s.DOWN)
        elif event.key == pygame.K_LEFT:
            snake.point(s.LEFT)
        elif event.key == pygame.K_RIGHT:
            snake.point(s.RIGHT)


def atualiza_tela(snake, apple, s):
    s.surface.fill((255, 255, 255))
    snake.move()
    verifica_comeu_maça(snake, apple)
    snake.desenha()
    apple.desenha()
    escreve_pontuacao(snake, s)
    s.screen.blit(s.surface, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    s.fpsClock.tick(s.FPS + snake.length / 3)


def escreve_pontuacao(snake, s):
    font = pygame.font.Font(None, 36)
    text = font.render(str(snake.length), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = 20
    s.surface.blit(text, textpos)
