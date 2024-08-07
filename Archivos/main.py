import pygame
from settings import *
from personajes import Personaje
from weapon import Weapon
from weapon import Bullet
import os
from items import Item
from random import randint
import json
import csv
from Funciones import *

pygame.init()
pygame.mixer.init()


#Barra salud
corazon_completo = pygame.image.load("Barra_salud//corazon_completo.png")
corazon_completo = escalar_imagen(corazon_completo, ESCALA_BARRA_VIDA)
corazon_mitad = pygame.image.load("Barra_salud//corazon_mitad.png")
corazon_mitad = escalar_imagen(corazon_mitad, ESCALA_BARRA_VIDA)
corazon_vacio = pygame.image.load("Barra_salud//corazon_vacio.png")
corazon_vacio = escalar_imagen(corazon_vacio, ESCALA_BARRA_VIDA)


#Personaje
animaciones = []
for i in range(6):
    img = pygame.image.load(f"Characters//Correr//adventurer-run-0{i}.png")
    img = escalar_imagen(img, ESCALA_PERSONAJE)
    animaciones.append(img)

#Enemigos
directorio_enemigos = "Enemigos"
tipo_enemigo = nombre_carpetas(directorio_enemigos)
animaciones_enemigos = []
for enem in tipo_enemigo:
    lista_temp = []
    ruta_temp = f"Enemigos//{enem}"
    num_animaciones = contar_elementos(ruta_temp)
    for i in range(num_animaciones):
        imagen_enemigo = pygame.image.load(f"{ruta_temp}//{enem}_{i+1}.png")
        imagen_enemigo = escalar_imagen(imagen_enemigo, ESCALA_ENEMIGOS)
        lista_temp.append(imagen_enemigo)
    animaciones_enemigos.append(lista_temp)
print(lista_temp)


#Arma
imagen_magnum = pygame.image.load("Weapons//UNSC//magnum.png") 
imagen_magnum = escalar_imagen(imagen_magnum, ESCALA_ARMA)

#Balas
imagen_balas = pygame.image.load("Laser Sprites//01.png")
imagen_balas = escalar_imagen(imagen_balas, ESCALA_BALA)

#Cargar imagenes
posion_1 = pygame.image.load("Items//potion_1.png")
posion_1 = escalar_imagen(posion_1, ESCALA_POSION)

coin = pygame.image.load("Items//coin_3.png")
coin = escalar_imagen(coin, ESCALA_COIN)






        
#Crear jugador clase Personaje
jugador = Personaje(50, 50, animaciones, 100, 0)

# Crear enemigo clase Personaje
caballero = Personaje(randint(0, ANCHO_PANTALLA - ANCHO_PERSONAJE), randint(0,ALTO_PANTALLA - ALTO_PERSONAJE), animaciones_enemigos[0], 75, 1)
esqueleto = Personaje(randint(0, ANCHO_PANTALLA - ANCHO_PERSONAJE), randint(0,ALTO_PANTALLA - ALTO_PERSONAJE), animaciones_enemigos[1], 75, 2)
monstruo = Personaje(randint(0, ANCHO_PANTALLA - ANCHO_PERSONAJE), randint(0,ALTO_PANTALLA - ALTO_PERSONAJE), animaciones_enemigos[2], 75, 3)

lista_enemigos = []
lista_enemigos.append(caballero)
lista_enemigos.append(esqueleto)
lista_enemigos.append(monstruo)




#Crear arma clase WEAPON
magnum = Weapon(imagen_magnum, imagen_balas)


moneda = Item(350,25,0,coin)
posion_1 = Item(380,55,1,posion_1)



#Crear grupo sprites
grupo_balas = pygame.sprite.Group()
grupo_items = pygame.sprite.Group()

grupo_items.add(moneda)
grupo_items.add(posion_1)



font = pygame.font.Font("Font//PixeloidSans-Bold.ttf", 15)
font_game_over = pygame.font.Font("Font//PixeloidSans-Bold.ttf", 100)
font_score_final = pygame.font.Font("Font//PixeloidSans-Bold.ttf", 32)
font_reinicio = pygame.font.Font("Font//PixeloidSans-Bold.ttf", 32 )
font_inicio = pygame.font.Font("Font//PixeloidSans-Bold.ttf", 15 )
font_titulo = pygame.font.Font("Font//PixeloidSans-Bold.ttf", 70 )
font_nombre = pygame.font.Font("Font//PixeloidSans-Bold.ttf", 40 )


game_over_txt = font_game_over.render("Game Over", True, BLACK)
texto_boton_menu = font_reinicio.render("Menu", True, BLACK)

boton_jugar = pygame.Rect(ANCHO_PANTALLA / 2 - 100, ALTO_PANTALLA / 2 - 70, 150, 50)
boton_opciones = pygame.Rect(ANCHO_PANTALLA / 2 - 100, ALTO_PANTALLA / 2 + 10, 150, 50)
boton_salir = pygame.Rect(ANCHO_PANTALLA / 2 - 100, ALTO_PANTALLA / 2 + 100, 150, 50)
boton_subir_volumen = pygame.Rect(ANCHO_PANTALLA / 2 - 100, ALTO_PANTALLA / 2 - 70, 180, 50)
boton_bajar_volumen = pygame.Rect(ANCHO_PANTALLA / 2 - 100, ALTO_PANTALLA / 2 + 10, 180, 50)
boton_volver = pygame.Rect(ANCHO_PANTALLA / 2 - 100, ALTO_PANTALLA / 2 + 100, 180, 50)
boton_ingresar = pygame.Rect(ANCHO_PANTALLA/2 - 100, ALTO_PANTALLA/2 + 50, 200, 50)
cuadro_texto_usuario = pygame.Rect(ANCHO_PANTALLA/2 - 100, ALTO_PANTALLA/2 - 100, 200, 50)

texto_boton_jugar = font_inicio.render("Jugar", True, BLACK)
texto_boton_opciones = font_inicio.render("Opciones", True, BLACK)
texto_boton_salir = font_inicio.render("Salir", True, BLACK)
texto_boton_subir_volumen = font_inicio.render("Subir volumen", True, BLACK)
texto_boton_bajar_volumen = font_inicio.render("Bajar Volumen", True, BLACK)
texto_boton_volver = font_inicio.render("Volver", True, BLACK)

fondo = pygame.image.load("Background//fondo.png")
fondo = escalar_fondo(fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))
fondo_inicio = pygame.image.load("Background//fondo_inicio.png")
fondo_inicio = escalar_fondo(fondo_inicio, (ANCHO_PANTALLA, ALTO_PANTALLA))
fondo_opciones = pygame.image.load("Background//fondo_opciones.png")
fondo_opciones = escalar_fondo(fondo_opciones, (ANCHO_PANTALLA, ALTO_PANTALLA))
fondo_usuario = pygame.image.load("Background//fondo_usuario.png")
fondo_usuario = escalar_fondo(fondo_usuario, (ANCHO_PANTALLA, ALTO_PANTALLA))


num_monedas_iniciales = 10  # Ajusta el número de monedas iniciales
regenerar_monedas(grupo_items, num_monedas_iniciales, coin)

ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Videojuego")


#definir variables movimiento
mover_izquierda = False
mover_derecha = False
mover_arriba = False
mover_abajo = False

sonido_disparo = pygame.mixer.Sound("sound effects//Laser.wav")
sonido_game_over = pygame.mixer.Sound("sound effects//Game_over.wav")
sonido_gameplay = pygame.mixer.Sound("sound effects//Cancion_gameplay.wav")
sonido_menu = pygame.mixer.Sound("sound effects//Cancion_menu.wav")

sonidos = ["sound effects//Laser.wav",
           "sound effects//Game_over.wav",
           "sound effects//Cancion_gameplay.wav",
           "sound effects//Cancion_menu.wav"]

guardar_rutas_json(sonidos, "Archivos//Sonidos.json")

user_text = ""

fuente_inicio_txt = font_inicio.render("Ingresar", True, BLACK)

volumen = 0.5

pygame.mixer.music.set_volume(volumen)


run = True
mostrar_inicio = True
mostrar_opciones = False
mostrar_usuario = True
sonido_game_over_escuchado = False

nuevos_usuarios_juego = []

reloj = pygame.time.Clock()

while run:
    # Verificar si se está mostrando la pantalla de inicio
    if mostrar_inicio:
        # Reproducir música de menú si no está sonando
        if not pygame.mixer.get_busy():
            sonido_menu.play(-1)
        
        # Mostrar la pantalla de inicio
        pantalla_inicio(ventana, fondo_inicio, font_titulo, boton_jugar, boton_opciones, boton_salir, texto_boton_jugar, texto_boton_opciones, texto_boton_salir)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Salir del juego si se cierra la ventana
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se hizo clic en el botón de jugar
                if boton_jugar.collidepoint(event.pos):
                    mostrar_inicio = False
                    sonido_menu.stop()  # Detener la música de menú
                    sonido_gameplay.play(-1)  # Reproducir música de juego
                # Verificar si se hizo clic en el botón de opciones
                if boton_opciones.collidepoint(event.pos):
                    mostrar_inicio = False
                    mostrar_opciones = True
                # Verificar si se hizo clic en el botón de salir
                if boton_salir.collidepoint(event.pos):
                    run = False  # Salir del juego si se hace clic en salir

    # Verificar si se está mostrando el menú de opciones
    elif mostrar_opciones:
        # Mostrar el menú de opciones
        menu_opciones2(ventana, fondo_opciones, font_titulo, ANCHO_PANTALLA, ALTO_PANTALLA, boton_subir_volumen, boton_bajar_volumen, boton_volver, texto_boton_subir_volumen, texto_boton_bajar_volumen, texto_boton_volver, font_inicio, volumen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Salir del juego si se cierra la ventana
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Subir el volumen si se hace clic en el botón correspondiente
                if boton_subir_volumen.collidepoint(event.pos):
                    volumen = min(1.0, volumen + 0.1)  # Asegurarse de que el volumen no supere 1.0
                    pygame.mixer.music.set_volume(volumen)  # Ajustar el volumen de la música
                # Bajar el volumen si se hace clic en el botón correspondiente
                if boton_bajar_volumen.collidepoint(event.pos):
                    volumen = max(0.0, volumen - 0.1)  # Asegurarse de que el volumen no sea menor que 0.0
                    pygame.mixer.music.set_volume(volumen)  # Ajustar el volumen de la música
                # Volver al menú principal si se hace clic en el botón correspondiente
                if boton_volver.collidepoint(event.pos):
                    mostrar_opciones = False
                    mostrar_inicio = True

    # Verificar si se está mostrando la pantalla de usuario
    elif mostrar_usuario:
        # Mostrar la pantalla de ingreso de usuario
        pantalla_usuario(ventana, fondo_usuario, font_inicio, user_text, fuente_inicio_txt, font_nombre, cuadro_texto_usuario, boton_ingresar)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Salir del juego si se cierra la ventana
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se hizo clic en el botón de ingresar
                if boton_ingresar.collidepoint(event.pos):
                    mostrar_usuario = False
            elif event.type == pygame.KEYDOWN:
                # Guardar el nombre de usuario si se presiona Enter
                if event.key == pygame.K_RETURN:
                    user_name = user_text
                    mostrar_usuario = False
                # Eliminar el último carácter del texto si se presiona Backspace
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                # Agregar el carácter presionado al texto del usuario
                else:
                    user_text += event.unicode

    else:
        # Limitar la velocidad de fotogramas del juego
        reloj.tick(FPS)

        # Dibujar el fondo
        ventana.blit(fondo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Salir del juego si se cierra la ventana
            
            if event.type == pygame.KEYDOWN:
                # Controlar el movimiento del jugador con las teclas WASD
                if event.key == pygame.K_a:
                    mover_izquierda = True
                if event.key == pygame.K_d:
                    mover_derecha = True
                if event.key == pygame.K_w:
                    mover_arriba = True
                if event.key == pygame.K_s:
                    mover_abajo = True

            if event.type == pygame.KEYUP:
                # Detener el movimiento del jugador cuando se sueltan las teclas
                if event.key == pygame.K_a:
                    mover_izquierda = False
                if event.key == pygame.K_d:
                    mover_derecha = False
                if event.key == pygame.K_w:
                    mover_arriba = False
                if event.key == pygame.K_s:
                    mover_abajo = False

        if jugador.vivo:
            # Calcular movimiento del jugador
            delta_x = 0
            delta_y = 0

            # Dibujar al jugador en la pantalla
            jugador.dibujar(ventana)

            # Ajustar el movimiento del jugador según las teclas presionadas
            if mover_arriba:
                delta_y = -VELOCIDAD
            if mover_abajo:
                delta_y = VELOCIDAD
            if mover_izquierda:
                delta_x = -VELOCIDAD
            if mover_derecha:
                delta_x = VELOCIDAD
            
            # Mover al jugador
            jugador.movimiento(delta_x, delta_y)

            # Actualizar y mover enemigos
            for ene in lista_enemigos:
                ene.mov_enemigos(jugador)
                ene.update()
                print(ene.energia)

            regenerar_enemigos(lista_enemigos, animaciones_enemigos)

            # Actualizar el arma
            bala = magnum.update(jugador)
            if bala:
                grupo_balas.add(bala)  # Agregar nueva bala al grupo de balas
                sonido_disparo.play()  # Reproducir sonido de disparo
            for bala in grupo_balas:
                bala.update(lista_enemigos)  # Actualizar posición de las balas

            # Actualizar ítems
            grupo_items.update(jugador)

            # Regenerar monedas si no hay monedas en pantalla
            if len([item for item in grupo_items if item.item_type == 0]) == 0:
                regenerar_monedas(grupo_items, num_monedas_iniciales, coin)

        # Dibujar el jugador
        jugador.dibujar(ventana)
        
        # Eliminar enemigos con energía cero y dibujar enemigos restantes
        for ene in lista_enemigos[:]:
            if ene.energia == 0:
                lista_enemigos.remove(ene)
            else:
                ene.update()
                ene.dibujar(ventana)

        # Dibujar el arma
        magnum.dibujar(ventana)

        # Dibujar balas
        for bala in grupo_balas:
            bala.update(lista_enemigos)
            bala.dibujar(ventana)

        # Dibujar la vida del jugador
        vida_jugador(jugador, ventana, corazon_completo, corazon_mitad, corazon_vacio)

        # Dibujar texto en pantalla
        dibujar_txt_pantalla(f"Score: {jugador.score}", font, YELLOW, 700, 5, ventana)

        # Actualizar el estado del jugador
        jugador.update()

        # Dibujar ítems
        grupo_items.draw(ventana)

        # Manejar el final del juego si el jugador no está vivo
        if not jugador.vivo:
            nuevo_usuario = guardar_usuario_2(user_text, jugador.score, nuevos_usuarios_juego, "Archivos//usuarios.csv")
            sonido_gameplay.stop()
            if not sonido_game_over_escuchado:
                sonido_game_over.play()  # Reproducir sonido de game over
                sonido_game_over_escuchado = True

            # Mostrar pantalla de Game Over
            ventana.fill(RED)
            text_rect = game_over_txt.get_rect(center=(ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2 - 100))
            ventana.blit(game_over_txt, text_rect)
            dibujar_txt_pantalla(f"SCORE: {jugador.score}", font_score_final, BLACK, ANCHO_PANTALLA / 2 - 100, ALTO_PANTALLA / 2, ventana)
            boton_menu = pygame.Rect(ANCHO_PANTALLA / 2 - 120, ALTO_PANTALLA / 2 + 100, 200, 70)
            pygame.draw.rect(ventana, WHITE, boton_menu)
            ventana.blit(texto_boton_menu, (boton_menu.x + 40, boton_menu.y + 10))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Volver al menú principal si se hace clic en el botón de menú
                    if boton_menu.collidepoint(event.pos) and not jugador.vivo:
                        jugador.vivo = True
                        jugador.energia = 100
                        jugador.score = 0
                        mostrar_inicio = True
                        sonido_game_over_escuchado = False
                        sonido_menu.play(-1)  # Reproducir música de menú nuevamente

        
    
        pygame.display.update()

pygame.quit()


