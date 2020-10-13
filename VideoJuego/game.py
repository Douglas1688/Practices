import pygame
import sys
import time,random
ancho=640
alto = 480
color_blanco = (255,255,255)
vidas=3
esperando_saque = True

color_azul = (0,0,64) #Color azul para el fondo
pygame.init()
#Inicializando pantalla
pantalla = pygame.display.set_mode((ancho,alto))
#Configurar título de pantalla
pygame.display.set_caption("Juego de ladrillos")
#Crea un reloj
reloj = pygame.time.Clock()
#Ajusta repetición de evento de tecla presionada
pygame.key.set_repeat(30)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Cargar imagen
        self.image = pygame.image.load('ball.png')
        #Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        #Posición inicial centrada en pantalla
        #self.rect.centerx = ancho//2
        self.rect.centerx = random.randint(0,ancho)
        #self.rect.centery = alto//2
        self.rect.centery = 200
        #Establecer velocidad inicial
        self.speed = [3,3]

    def update(self):
        #Evitar que salga por debajo
        if self.rect.top <=0:
            self.speed[1]=-self.speed[1]
        #Evitar que salga por la derecha
        if self.rect.right >= ancho or  self.rect.left <=0:
            self.speed[0]=-self.speed[0]

        #Mover en base a la posición actual y velocidad
        self.rect.move_ip(self.speed)


class Tabla(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('raya.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial centrada en pantalla en X
        self.rect.midbottom = (ancho//2,alto-20)
        # Establecer velocidad inicial
        self.speed = [0,0]

    def update(self,evento):
        #Buscar si se presionó flecha izquierda
        if evento.key == pygame.K_LEFT and self.rect.left >0:
            self.speed = [-30,0]
        #Si se presionó flecha derecha.
        elif evento.key == pygame.K_RIGHT and self.rect.right < ancho:
            self.speed = [30,0]
        else:
            self.speed = [0,0]
        self.rect.move_ip(self.speed)

class Blocks(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        #Cargar imagen
        self.image = pygame.image.load('block.png')
        #Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        #Posición inicial provista externamente
        self.rect.topleft = posicion


class Wall(pygame.sprite.Group):
    def __init__(self,cantidadBlocks):
        pygame.sprite.Group.__init__(self)
        pos_x=0
        pos_y=20
        for i in range(cantidadBlocks):
            block = Blocks((pos_x,pos_y))
            self.add(block)
            pos_x += block.rect.width
            if pos_x >= ancho:
                pos_x=0
                pos_y += block.rect.height
def juego_terminado():
    fuente = pygame.font.SysFont('Arial',72)
    texto = fuente.render('Juego Terminado :(',True,color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.center = [ancho//2,alto//2]
    pantalla.blit(texto,texto_rect)
    pygame.display.flip()

    time.sleep(3)
    #Salir
    sys.exit()

def mostrar_puntuacion():
    fuente = pygame.font.SysFont('Consolas',20)
    texto = fuente.render(str(puntuacion).zfill(5),True,color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.topleft = [0,0]
    pantalla.blit(texto,texto_rect)

def mostrar_vidas():
    fuente = pygame.font.SysFont('Consolas',20)
    cadena = "Vidas: " +str(vidas).zfill(2)
    texto = fuente.render(cadena,True,color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.topright = [ancho,0]
    pantalla.blit(texto,texto_rect)


ball = Ball()
tabla = Tabla()
muro = Wall(48)
puntuacion=0

while True:
    #Establecer FPS
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            tabla.update(evento)
            if esperando_saque == True and evento.key == pygame.K_SPACE:
                esperando_saque = False
                if ball.rect.centerx < ancho //2:
                    ball.speed = [3,-3]
                else:
                    ball.speed=[-3,-3]
    if esperando_saque == False:
        ball.update()
    else:
        ball.rect.midbottom = tabla.rect.midtop
    #Actualizar posición de la bola
    ball.update()
    #Colisión entre bola y tabla
    if pygame.sprite.collide_rect(ball,tabla):
        ball.speed[1]=-ball.speed[1]
    #colisión entre bola y muro
    lst = pygame.sprite.spritecollide(ball,muro,False)
    if lst:
        ladrillo = lst[0]
        cx = ball.rect.centerx
        if cx<ladrillo.rect.left or cx > ladrillo.rect.right:
            ball.speed[0] = -ball.speed[0]
        else:
            ball.speed[1] = -ball.speed[1]
        muro.remove(ladrillo)
        puntuacion+=10


    #Revisar si la bola sale de la pantalla
    if ball.rect.top > alto:
        vidas-=1
        esperando_saque = True



    pantalla.fill(color_azul)
    #mostrar puntuación
    mostrar_puntuacion()
    mostrar_vidas()
    pantalla.blit(ball.image,ball.rect)
    pantalla.blit(tabla.image,tabla.rect)
    muro.draw(pantalla)
    pygame.display.flip()
    if vidas <=0:
        juego_terminado()

