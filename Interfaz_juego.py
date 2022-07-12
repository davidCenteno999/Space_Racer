#Estrctura principal


import pygame 
from random import randint


pygame.init()


def obstaculos_alien_mov(obstaculos_lista):
    if obstaculos_lista!=[]:
        for obstaculo in obstaculos_lista:
            obstaculo.x -=3
            if obstaculo.y==100 or obstaculo.y == 200 or obstaculo.y== 300 or obstaculo.y== 400 or obstaculo.y== 500 or obstaculo.y== 600:
                pantalla.blit(Alien,obstaculo)
            else:
                pantalla.blit(Alien2,obstaculo)
        obstaculos_lista=[obstaculo for obstaculo in obstaculos_lista if obstaculo.x > -100]

        return obstaculos_lista
    else:
        return []

def colisiones1(jugador,obstaculo_lista):#funcion para colicion con enemigos
    if obstaculo_lista!=[]:
        for obstaculo in obstaculo_lista:
            if jugador.colliderect(obstaculo):
                obstaculo_lista.remove(obstaculo)
                return  5

def generador_jefe(lista_jefe):
    if lista_jefe!=[]:
        for jefe in lista_jefe:
            jefe.x-=4
            pantalla.blit(Jefe,jefe)
        lista_jefe=[jefe for jefe in lista_jefe if jefe.x > -100]
        return lista_jefe
    else:
        return []

def colision_jefe(jugador,lista_jefe):
    if lista_jefe!=[]:
        for jefe in lista_jefe:
            if jugador.colliderect(jefe):
                lista_jefe.remove(jefe)
                return 15

def generador_monedas(lista_monedas):
    if lista_monedas!=[]:
        for moneda in lista_monedas:
            moneda.x-=3
            pantalla.blit(Moneda_obj,moneda)
        lista_monedas=[moneda for moneda in lista_monedas if moneda.x > -100]

        return lista_monedas
    else:
        return []

def colisiones2(jugador,lista_monedas):
    if lista_monedas!=[]:
        for moneda in lista_monedas:
            if jugador.colliderect(moneda):
                lista_monedas.remove(moneda)
                return 1

def generador_imanes(lista_iman):
    if lista_iman!=[]:
        for iman in lista_iman:
            iman.x-=4
            pantalla.blit(Poder_iman,iman)
        lista_iman=[iman for iman in lista_iman if iman.x > -100]

        return lista_iman
    else:
        return []

def colisiones3(jugador,lista_iman):
    if lista_iman!=[]:
        for iman in lista_iman:
            if jugador.colliderect(iman):
                lista_iman.remove(iman)
                return True

def generador_campo_fuerza(lista_campo_fuerza):
    if lista_campo_fuerza!=[]:
        for campo_fuerza in lista_campo_fuerza:
            campo_fuerza.x-=4
            pantalla.blit(Poder_campo_fuerza,campo_fuerza)
        lista_campo_fuerza=[campo_fuerza for campo_fuerza in lista_campo_fuerza if campo_fuerza.x > -100]

        return lista_campo_fuerza
    else:
        return []

def colisiones4(jugador,lista_campo_fuerza):
    if lista_campo_fuerza!=[]:
        for campo_fuerza in lista_campo_fuerza:
            if jugador.colliderect(campo_fuerza):
                lista_campo_fuerza.remove(campo_fuerza)
                return True

#Campo de fuerza del jugador
def campo_fuerza_coll(jugador,lista_aliens):
    if lista_aliens!=[]:
        for alien in lista_aliens:
            if jugador.colliderect(alien):
                lista_aliens.remove(alien)

#Iman atrae monedas
def iman_monedas(lista_monedas):
    if lista_monedas!=[]:
        for moneda in lista_monedas:
            if moneda.x<150:
                lista_monedas.remove(moneda)
                return 1

def competidor(jugador,lista_aliens):
    if lista_aliens!=[]:
        for alien in lista_aliens:
            if jugador.colliderect(alien):
                lista_aliens.remove(alien)
                return 10

def competidor_detec_a(jugador,lista_alien):
    if lista_alien!=[]:
        for alien in lista_alien:
            if   alien.x<100 and (alien.y==400 or alien.y==390) and  jugador.y==400:#80<alien.x<100
                return True
def competidor_detec_b(jugador,lista_alien):
    if lista_alien!=[]:
        for alien in lista_alien:
            if  alien.x-10<100 and (alien.y==500 or alien.y==490 )  and jugador.y==500:
                return True
def competidor_detec_c(jugador,lista_alien):
    if lista_alien!=[]:
        for alien in lista_alien:
            if alien.x-10<100 and (alien.y==600 or alien.y==590) and   jugador.y==600:
                return True


pantalla = pygame.display.set_mode((1170,700))#Dimensiones pantalla
Titulo="Space Racers"

#Velocidad de animacion
Reloj=pygame.time.Clock()

#Musica juego
pygame.mixer.music.load("Proyecto Final/Imagenes/game_music.mp3")
pygame.mixer.music.play(-1)

#Icono juego
icono1 = pygame.image.load("Proyecto Final/Imagenes/ic.png")
pygame.display.set_icon(icono1)

#Fondo pantalla de inicio
Imagen_fondo_1=pygame.image.load("Proyecto Final/Imagenes/fondo_general.jpg")

#Titulo principal de la pagina
fuente_j= pygame.font.SysFont("Times New Roman",90)
texto_juego=fuente_j.render("Space Racers", False, (191, 200, 0))


#Botones generales
Boton_crear_partida=pygame.image.load("Proyecto Final/Imagenes/ajustes.png")
Boton_crear_partida_rect=Boton_crear_partida.get_rect(topleft=(1095,30))
Boton_inicio_partida=pygame.image.load("Proyecto Final/Imagenes/jugar.png")
Boton_inicio_partida_rect=Boton_inicio_partida.get_rect(topleft=(1095,130))
Boton_salida=pygame.image.load("Proyecto Final/Imagenes/salir.png")
Boton_salida_rect=Boton_salida.get_rect(topleft=(1095,230))
Boton_ayuda=pygame.image.load("Proyecto Final/Imagenes/acerca de.png")
Boton_ayuda_rect=Boton_ayuda.get_rect(topleft=(1095,330))
Acerca_de=pygame.image.load("Proyecto Final/Imagenes/info.png")
Acerca_de_rect=Acerca_de.get_rect(topleft=(1095,430))

#Personas
Persona=pygame.image.load("Proyecto Final/Imagenes/Persona.png")
Persona_rect=Persona.get_rect(topleft=(1010,30))
Personas=pygame.image.load("Proyecto Final/Imagenes/Personas.png")
Personas_rect=Personas.get_rect(topleft=(925,30))

fuente1= pygame.font.SysFont("Times New Roman",23)
Nombres_jugadores=fuente1.render("Nombres:",False,(200,200,200))

#Informacion
Dato1= fuente1.render("Creador: David Josue Centeno Araya", False, (200,200,200))
Dato2= fuente1.render("Juego de naves espaciales",False,(200,200,200))

#Texto (nombre de jugadores)
texto= ""
fuente= pygame.font.SysFont("Times New Roman",23)
rectangulo_texto=pygame.Rect(925,130,50,30)#Rectangulo de base de texto
color_rectangulo_texto=pygame.Color(255,255,255)#Color de rectangulo(0,205,50)

#Naves
Nave1=pygame.image.load("Proyecto Final/Imagenes/Nave.png")
Nave1_rect=Nave1.get_rect(topleft=(20,300))

Nave2=pygame.image.load("Proyecto Final/Imagenes/Nave2.png")
Nave2_rect=Nave2.get_rect(topleft=(20,300))

Nave3=pygame.image.load("Proyecto Final/Imagenes/Nave3.png")
Nave3_rect=Nave3.get_rect(topleft=(20,300))

Nave4=pygame.image.load("Proyecto Final/Imagenes/Nave4.png")
Nave4_rect=Nave4.get_rect(topleft=(20,300))

Nave5=pygame.image.load("Proyecto Final/Imagenes/Nave5.png")
Nave5_rect=Nave5.get_rect(topleft=(20,500))

#Zonas disponibles
Zona_espacio=pygame.image.load("Proyecto Final/Imagenes/T1.jpg")
Zona_espacio_rect=Zona_espacio.get_rect(topleft=(850,140))

Zona_volcanica=pygame.image.load("Proyecto Final/Imagenes/T2.jpg")
Zona_volcanica_rect=Zona_volcanica.get_rect(topleft=(650,140))

Zona_helada=pygame.image.load("Proyecto Final/Imagenes/T3.jpg")
Zona_helada_rect=Zona_helada.get_rect(topleft=(650,260))

Zona_montañas=pygame.image.load("Proyecto Final/Imagenes/T4.jpg")
Zona_montañas_rect=Zona_montañas.get_rect(topleft=(850,260))

#Fondos
Imagen_fondo_2=pygame.image.load("Proyecto Final/Imagenes/fondo_espacio.jpg")
Imagen_fondo_3=pygame.image.load("Proyecto Final/Imagenes/fondo2.jpg")
Imagen_fondo_4=pygame.image.load("Proyecto Final/Imagenes/fondo3.jpg")
Imagen_fondo_5=pygame.image.load("Proyecto Final/Imagenes/fondo4.jpg")
#Obstaculos
Alien=pygame.image.load("Proyecto Final/Imagenes/alien.png")
Alien2=pygame.image.load("Proyecto Final/Imagenes/alien_j.png")

Obstaculos_aliens= []

#Moenda_objeto
Moneda_obj=pygame.image.load("Proyecto Final/Imagenes/moneda.png")

Monedas_lista=[]

#Jefe
Jefe=pygame.image.load("Proyecto Final/Imagenes/jefe.png")

Jefe_lista=[]
#Tiempo obstaculos
obstaculos_tiempo=pygame.USEREVENT + 1
pygame.time.set_timer(obstaculos_tiempo,1800)

#Timepo monedas
monedas_tiempo=pygame.USEREVENT + 1
pygame.time.set_timer(monedas_tiempo,1900)

#Tiempo poderes generador
poder_iman_tiempo=pygame.USEREVENT + 1
pygame.time.set_timer(poder_iman_tiempo,2000)

poder_campo_fuerza_timepo=pygame.USEREVENT + 1
pygame.time.set_timer(poder_campo_fuerza_timepo,2000)

#2
#Tiempo poderes
poder_iman_tiempo2=pygame.USEREVENT + 1
pygame.time.set_timer(poder_iman_tiempo2,900)

poder_campo_fuerza_timepo2=pygame.USEREVENT + 1
pygame.time.set_timer(poder_campo_fuerza_timepo2,900)

#3
#Tiempo jefe
jefe_tiempo=pygame.USEREVENT + 1
pygame.time.set_timer(jefe_tiempo,900)

#Poderes
Poder_campo_fuerza=pygame.image.load("Proyecto Final/Imagenes/galaxy.png")
Poder_iman=pygame.image.load("Proyecto Final/Imagenes/iman.png")
Lista_campos_fuerza=[]
Lista_imanes=[]


#Monedas_imagen
Monedas_cont=pygame.image.load("Proyecto Final/Imagenes/moneda.png")


#Clase para barra de vida de jugador
class Jugador_vida:
    def __init__(self,vida):
        self.max_vida =vida
    def barra_salud(self,pant,vida):
        self.vida=vida
        if self.vida>90:
            pygame.draw.rect(pant,(255,0,0),((210,30),(self.max_vida-self.vida,20)))
        elif self.vida>60:
            pygame.draw.rect(pant,(255,128,0),((210,30),(self.max_vida-self.vida,20)))
        else:
            pygame.draw.rect(pant,(0,255,0),((210,30),(self.max_vida-self.vida,20)))
    def barra_salud2(self,pant,vida2):
        self.vida2=vida2
        if self.vida2>90:
            pygame.draw.rect(pant,(255,0,0),((630,30),(self.max_vida-self.vida2,20)))
        elif self.vida2>60:
            pygame.draw.rect(pant,(255,128,0),((630,30),(self.max_vida-self.vida2,20)))
        else:
            pygame.draw.rect(pant,(0,255,0),((630,30),(self.max_vida-self.vida2,20)))
  

#Contador poder campo de fuerza
fuente_p=pygame.font.SysFont("didot.ttc",25)
contador1="0"
rectangulo_texto1=pygame.Rect(1010,550,60,40)

#Contador iman
contador2="0"
rectangulo_texto2=pygame.Rect(1010,590,60,40)

#Monedas
contador3="0"
rectangulo_texto3=pygame.Rect(1010,630,60,40)

#Poderes valores
Poder_im=False
Poder_camp=False

#Barra de vida
vida_perdida=0
Barra_vida=Jugador_vida(100)
vida_perdida2=0
Barra_vida2=Jugador_vida(100)
#Nombre jugador
Nombre=fuente.render("Jugador:", False, (200, 200, 200))
Nombre2_m=fuente.render("Jugador2:", False, (200, 200, 200))
#Mensaje de perdida del juego
fuente_men_ele= pygame.font.SysFont("Times New Roman",70)
Perdida=fuente_men_ele.render("Game Over",False,(255,0,0))
Gane=fuente_men_ele.render("You win",False,(255,0,0))

#Texto de informacion del juego
teclado=pygame.image.load("Proyecto Final/Imagenes/teclado.png")
fuente3= pygame.font.SysFont("Times New Roman",15)
t1=fuente3.render("En el siguiente apartado podrá encontrar los movimientos básicos de las naves ",False,(0,255,0))
t12=fuente3.render("y algunas recomendaciones del sistema de colisiones.",False,(0,255,0))
t2=fuente3.render("Tecla 1: permite a la nave ascender y pasar de carril.(recuadro verde)",False,(0,255,0))
t3=fuente3.render("Tecla 2: permite a la nave descender y pasar de carril.(recuadro naranja)",False,(0,255,0))
t4=fuente3.render("Tecla 9: permite a la nave moverse hacia atrás.(recuadro celeste)",False,(0,255,0))
t5=fuente3.render("Tecla 0: permite a la nave moverse hacia adelante.(recuadro rojo)",False,(0,255,0))
t6=fuente3.render("*IMPORTANTE: tenga en cuenta que el jugador solo ",False,(0,255,0))
t66=fuente3.render("cuenta con tres carriles por lo tanto los",False,(0,255,0))
t7=fuente3.render("movimientos de acenso y descenso se encuentran ",False,(0,255,0))
t77=fuente3.render("limitados. Para el caso de los movimientos hacia" ,False,(0,255,0))
t8=fuente3.render(" adelante o hacia atrás también se encuentran" ,False,(0,255,0))
t88=fuente3.render("limitados, el alcance de la nave en cuanto movimientos ",False,(0,255,0))
t9=fuente3.render("está determinado por la mitad del carril en que se",False,(0,255,0))
t10=fuente3.render("encuentra y los movimientos hacia atrás se encuentran",False,(0,255,0))
t1e=fuente3.render("también limitados siendo el borde izquierdo ",False,(0,255,0))
t11=fuente3.render("de la interfaz el límite.",False,(0,255,0))
Partida_Doble=False
Juego_perdido=False
Juego_ganado=False
Fondo_montaña=False
Fondo_helado=False
Fondo_volcanico=False
Fondo_espacio=False
Zonas=False
Informacion_juego=False
Informacion=False
Lista_nombres=[]
texto_activo=False
crear=False
Juego=False
Proceso = True
while Proceso:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Proceso=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Boton_crear_partida_rect.collidepoint(event.pos) and Juego==False:
                crear=True#
                Juego=False
                texto_activo=True  #
                Zonas=False
                Informacion=False
                Informacion_juego=False
                Lista_nombres=[]
            if crear==True and Personas_rect.collidepoint(event.pos) and Juego==False:
                Partida_Doble=True
            if Boton_inicio_partida_rect.collidepoint(event.pos):
                Zonas=True#
                crear=False
                Informacion=False
                Informacion_juego=False
            if Acerca_de_rect.collidepoint(event.pos):
                Informacion=True#
                Zonas=False
                crear=False
                Informacion_juego=False
            if Boton_ayuda_rect.collidepoint(event.pos):
                Informacion_juego=True#
                Zonas=False
                crear=False
                Informacion=False
            if Boton_salida_rect.collidepoint(event.pos):
                crear=False
                Informacion=False
                Informacion_juego=False
                Fondo_espacio=False
                Fondo_montaña=False
                Fondo_volcanico=False
                Fondo_helado=False
                Zonas=False
                Juego=False
                Partida_Doble=False
                contador1="0"
                contador2="0"
                contador3="0"
                Barra_vida=Jugador_vida(100)
                vida_perdida=0
                Juego_perdido=False
                
            if Zona_espacio_rect.collidepoint(event.pos):#Zonas
                Fondo_espacio=True
                Zonas=False
                Fondo_volcanico=False
                Fondo_helado=False
                Fondo_montaña=False
                crear=False
                Juego=True
                
            if Zona_volcanica_rect.collidepoint(event.pos):
                Fondo_volcanico=True
                Zonas=False
                Fondo_espacio=False
                Fondo_helado=False
                Fondo_montaña=False
                crear=False
                Juego=True
                 
            if Zona_helada_rect.collidepoint(event.pos):
                Fondo_helado=True
                Zonas=False
                Fondo_espacio=False
                Fondo_volcanico=False
                Fondo_montaña=False
                crear=False
                Juego=True
            if Zona_montañas_rect.collidepoint(event.pos):
                Fondo_montaña=True
                Zonas=False
                Fondo_espacio=False
                Fondo_volcanico=False
                Fondo_helado=False
                crear=False
                Juego=True

        if event.type == pygame.KEYDOWN:
            if texto_activo==True:
                if event.key==pygame.K_BACKSPACE:
                    texto=texto[:-1]
                        
                elif event.key == pygame.K_SPACE:
                    Lista_nombres+=[texto]
                    texto=""
                else:
                    texto+= event.unicode
            if event.key==pygame.K_1:#Movimientos de jugador
                if Fondo_espacio==True and 50<Nave1_rect.y-100< 350 and Juego_perdido==False and Juego_ganado==False:
                    Nave1_rect.y-=100
                    
                elif Fondo_volcanico==True and 50<Nave2_rect.y-100< 350 and Juego_perdido==False and Juego_ganado==False:
                    Nave2_rect.y-=100
                elif Fondo_helado==True and 50<Nave3_rect.y-100< 350 and Juego_perdido==False and Juego_ganado==False:
                    Nave3_rect.y-=100
                elif Fondo_montaña==True and 50<Nave4_rect.y -100< 400 and Juego_perdido==False and Juego_ganado==False:
                    Nave4_rect.y-=100
                    
            elif event.key==pygame.K_2:
                if Fondo_espacio==True and 50<Nave1_rect.y+100 < 350 and Juego_perdido==False and Juego_ganado==False:
                    Nave1_rect.y+=100
                elif Fondo_volcanico==True and 50<Nave2_rect.y+100 < 310 and Juego_perdido==False and Juego_ganado==False:
                    Nave2_rect.y+=100
                elif Fondo_helado==True and 50<Nave3_rect.y+100 < 350 and Juego_perdido==False and Juego_ganado==False:
                    Nave3_rect.y+=100
                elif Fondo_montaña==True and 50<Nave4_rect.y +100< 400 and Juego_perdido==False and Juego_ganado==False:
                    Nave4_rect.y+=100
            elif event.key==pygame.K_0:
                if Fondo_espacio==True and Nave1_rect.x+50 < 520 and Juego_perdido==False and Juego_ganado==False:
                    Nave1_rect.x+=50
                elif Fondo_volcanico==True and Nave2_rect.x+50 < 520 and Juego_perdido==False and Juego_ganado==False:
                    Nave2_rect.x+=50
                elif Fondo_helado==True and Nave3_rect.x+50 < 520 and Juego_perdido==False and Juego_ganado==False:
                    Nave3_rect.x+=50
                elif Fondo_montaña==True and Nave4_rect.x+50 < 520 and Juego_perdido==False and Juego_ganado==False:
                    Nave4_rect.x+=50
            elif event.key==pygame.K_9:
                if Fondo_espacio==True and Nave1_rect.x-50 > 0 and Juego_perdido==False and Juego_ganado==False:
                    Nave1_rect.x-=50
                elif Fondo_volcanico==True and Nave2_rect.x-50 > 0 and Juego_perdido==False and Juego_ganado==False:
                    Nave2_rect.x-=50
                elif Fondo_helado==True and Nave3_rect.x-50 > 0 and Juego_perdido==False and Juego_ganado==False:
                    Nave3_rect.x-=50
                elif Fondo_montaña==True and Nave4_rect.x-50 > 0 and Juego_perdido==False and Juego_ganado==False:
                    Nave4_rect.x-=50
        if event.type == obstaculos_tiempo and Juego==True and Juego_perdido==False and Juego_ganado==False: #Generador de obstaculos
            #Generador aliens
            ele=randint(1,10)
            if ele==10 and randint(1,15)%3==0:
                Obstaculos_aliens+=[Alien.get_rect(topleft=(randint(1400,9300),100))]
            elif ele==1 and randint(1,10)%2==0:
                Obstaculos_aliens+=[Alien2.get_rect(topleft=(randint(1400,9300),80))]
            elif ele==2:
                Obstaculos_aliens+=[Alien.get_rect(topleft=(randint(1400,9300),200))]
            elif ele==3 and randint(1,30)%3==0:
                Obstaculos_aliens+=[Alien2.get_rect(topleft=(randint(1400,9300),180))]
            elif ele==4 and randint(1,10)%2==0:
                Obstaculos_aliens+=[Alien.get_rect(topleft=(randint(1400,9300),300))]
            elif  randint(1,30)==15:
                Obstaculos_aliens+=[Alien2.get_rect(topleft=(randint(1400,9300),290))]
            elif  randint(1,20)%5==0:#Segundo nivel
                Obstaculos_aliens+=[Alien.get_rect(topleft=(randint(1400,9300),400))]
            elif ele==5 and randint(1,20)%5==0 and Partida_Doble==True:
                Obstaculos_aliens+=[Alien2.get_rect(topleft=(randint(1400,9300),390))]
            elif ele==6 and randint(1,20)%2==0 and Partida_Doble==True:
                Obstaculos_aliens+=[Alien2.get_rect(topleft=(randint(1400,9300),500))]
            elif ele==7 and randint(1,20)%2==0 and Partida_Doble==True:
                Obstaculos_aliens+=[Alien.get_rect(topleft=(randint(1400,9300),490))]
            elif ele==8 and randint(1,20)%3==0 and Partida_Doble==True:
                Obstaculos_aliens+=[Alien.get_rect(topleft=(randint(1400,9300),600))]
            elif ele==9 and randint(1,20)%4==0 and Partida_Doble==True:
                Obstaculos_aliens+=[Alien2.get_rect(topleft=(randint(1400,9300),590))]
        if event.type == monedas_tiempo and Juego==True and Juego_perdido==False:
            #Gnerador monedas
            ele2=randint(1,3)
            if ele2==1 and randint(1,10)==2:
                Monedas_lista+=[Moneda_obj.get_rect(topleft=(randint(1200,9000),100))]
            elif ele2==2 and randint(1,20)%2==0:
                Monedas_lista+=[Moneda_obj.get_rect(topleft=(randint(1200,9000),200))]
            elif ele2==3 and randint(1,30)%3==0:
                Monedas_lista+=[Moneda_obj.get_rect(topleft=(randint(1200,9000),300))]

        if event.type == poder_campo_fuerza_timepo and Juego==True and Juego_perdido==False and Juego_ganado==False:#Generador campo de fuerza
            #Generador campos de fuerza
            ele3=randint(1,3)
            if ele3==1 and randint(1,30)==20:
                Lista_campos_fuerza+=[Poder_campo_fuerza.get_rect(topleft=(randint(1600,10000),100))]
            elif ele3==2 and randint(1,20)==15: 
                Lista_campos_fuerza+=[Poder_campo_fuerza.get_rect(topleft=(randint(1600,10000),200))]
            elif ele3==3 and randint(1,10)==9:
                Lista_campos_fuerza+=[Poder_campo_fuerza.get_rect(topleft=(randint(1600,10000),300))]
        if event.type == poder_iman_tiempo and Juego==True and Juego_perdido==False and Juego_ganado==False: #Generador iman
            #Generador imanes
            ele4=randint(1,3)
            if ele4==1 and randint(1,30)==3:
                Lista_imanes+=[Poder_iman.get_rect(topleft=(randint(1600,5000),100))]
            elif ele4==2 and randint(1,20)==19:
                Lista_imanes+=[Poder_iman.get_rect(topleft=(randint(1600,5000),200))]
            elif ele4==3 and randint(1,20)==5:
                Lista_imanes+=[Poder_iman.get_rect(topleft=(randint(1600,5000),300))]
        if event.type== jefe_tiempo and Juego==True and Juego_perdido==False:
            #Generador jefe
            ele5=randint(1,6)
            if ele5==1 and randint(1,50)%7==0:
                Jefe_lista+=[Jefe.get_rect(topleft=(randint(1600,8000),100))]
            elif ele5==2 and randint(1,50)%9==0:
                Jefe_lista+=[Jefe.get_rect(topleft=(randint(1600,8000),200))]
            elif ele5==3 and randint(1,50)==19:
                Jefe_lista+=[Jefe.get_rect(topleft=(randint(1600,8000),300))]
            elif ele5==4 and randint(1,50)==49 and Partida_Doble==True:
                Jefe_lista+=[Jefe.get_rect(topleft=(randint(1600,8000),400))]
            elif ele5==5 and randint(1,50)==3 and Partida_Doble==True:
                Jefe_lista+=[Jefe.get_rect(topleft=(randint(1600,8000),500))]
            elif ele5==6 and randint(1,10)%7==0 and Partida_Doble==True:#ele5==6 and randint(1,50)==13:
                Jefe_lista+=[Jefe.get_rect(topleft=(randint(1600,8000),600))]
        if event.type == poder_iman_tiempo2 and Juego==True and Poder_im==True and int(contador2)!=0:
            contador2=str(int(contador2)-1)
        elif int(contador2)==0 and Poder_im==True:
            Poder_im=False
        if event.type == poder_campo_fuerza_timepo2 and Juego==True and Poder_camp==True and int(contador1)!=0:
            contador1=str(int(contador1)-1)
        elif int(contador1)==0 and Poder_camp==True:
            Poder_camp=False 

    
    
    
    if Fondo_espacio==False and Fondo_volcanico==False and Fondo_helado==False and Fondo_montaña==False:
        pantalla.blit(Imagen_fondo_1,(0,0))
        pantalla.blit(texto_juego,(350,300))
    elif Fondo_espacio==True:
        pantalla.blit(Imagen_fondo_2,(0,0))
    elif Fondo_volcanico==True:
        pantalla.blit(Imagen_fondo_3,(0,0))
    elif Fondo_helado==True:
        pantalla.blit(Imagen_fondo_4,(0,0))
    elif Fondo_montaña==True:
        pantalla.blit(Imagen_fondo_5,(0,0))

    
    
    if Zonas==True:
        pygame.draw.rect(pantalla,(70,40,130),((590,120),(500,250)))
        pantalla.blit(Zona_helada,Zona_helada_rect)
        pantalla.blit(Zona_espacio,Zona_espacio_rect)
        pantalla.blit(Zona_volcanica,Zona_volcanica_rect)
        pantalla.blit(Zona_montañas,Zona_montañas_rect)
        pygame.draw.rect(pantalla,(153,102,204),((650,140),(150,90)),7)
        pygame.draw.rect(pantalla,(153,102,204),((850,140),(150,90)),7)
        pygame.draw.rect(pantalla,(153,102,204),((650,260),(150,90)),7)
        pygame.draw.rect(pantalla,(153,102,204),((850,260),(150,90)),7)

    if crear == True and Juego==False:
        pygame.draw.rect(pantalla,(70,40,130),((920,30),(160,60)))
        pantalla.blit(Persona,Persona_rect)
        pantalla.blit(Personas,Personas_rect)
        pantalla.blit(Nombres_jugadores,(925,100))
            
                                
        #Nombres jugadores
        texto_despliegue= fuente.render(texto,True,(0,255,0))
        pantalla.blit(texto_despliegue,rectangulo_texto) #Generar el texto
        pygame.draw.rect(pantalla,color_rectangulo_texto,rectangulo_texto,2)#Generar una forma
        rectangulo_texto.w= max(5,texto_despliegue.get_width()+10)

    if Informacion_juego==True:
        pygame.draw.rect(pantalla,(0,0,0),((290,20),(520,650)))
        pygame.draw.rect(pantalla,(0,255,0),((290,20),(520,650)),3)
        pantalla.blit(teclado,(305,250))
        pantalla.blit(t1,(305,40))
        pantalla.blit(t12,(305,70))
        pantalla.blit(t2,(305,100))
        pantalla.blit(t3,(305,130))
        pantalla.blit(t4,(305,160))
        pantalla.blit(t5,(305,190))
        pantalla.blit(t6,(305,400))
        pantalla.blit(t66,(305,420))
        pantalla.blit(t7,(305,440))
        pantalla.blit(t77,(305,460))
        pantalla.blit(t8,(305,480))
        pantalla.blit(t88,(305,500))
        pantalla.blit(t9,(305,520))
        pantalla.blit(t10,(305,540))
        pantalla.blit(t1e,(305,560))
        pantalla.blit(t11,(305,580))
    if Informacion==True:
        pygame.draw.rect(pantalla,(70,40,130),((690,430),(400,200)))
        pantalla.blit(Dato1,(695,430))
        pantalla.blit(Dato2,(695,500))

    if Juego==True:
       
        pygame.draw.rect(pantalla,(70,40,130),((200,20),(390,40)))#290,430,435
        pygame.draw.rect(pantalla,(0,0,0),((340,25),(200,30)))
        pygame.draw.rect(pantalla,(0,255,0),((340,25),(200,30)),3)
        pantalla.blit(Nombre,(345,25))
        if Partida_Doble==True:
            pygame.draw.rect(pantalla,(70,40,130),((620,20),(390,40)))
            pygame.draw.rect(pantalla,(0,0,0),((760,25),(200,30)))
            pygame.draw.rect(pantalla,(0,255,0),((760,25),(200,30)),3)
            pantalla.blit(Nombre2_m,(765,25))
        if Lista_nombres!=[] and len(Lista_nombres)==1:
            Nombre2=fuente.render(Lista_nombres[-1],False,(200,200,200))
            pantalla.blit(Nombre2,(430,25))
        elif Lista_nombres!=[] and len(Lista_nombres)==2 and Partida_Doble==True:
            Nombre2=fuente.render(Lista_nombres[0],False,(200,200,200))
            pantalla.blit(Nombre2,(430,25))
            Nombre3=fuente.render(Lista_nombres[1],False,(200,200,200))
            pantalla.blit(Nombre3,(855,25))
        #Generador de aliens y mensaje de perdida
        if Juego_perdido==False and Juego_perdido==False and Juego_ganado==False:    
            Obstaculos_aliens=obstaculos_alien_mov(Obstaculos_aliens)
            Jefe_lista=generador_jefe(Jefe_lista)
            Monedas_lista=generador_monedas(Monedas_lista)
            Lista_imanes=generador_imanes(Lista_imanes)
            Lista_campos_fuerza=generador_campo_fuerza(Lista_campos_fuerza)
        elif Juego_perdido==True:
            pantalla.blit(Perdida,(350,300))
        elif Juego_ganado==True:
            pantalla.blit(Gane,(350,300))
        #Despliegue de fondos
        if Fondo_espacio==True:
            pantalla.blit(Nave1,Nave1_rect)
        elif Fondo_volcanico==True:
            pantalla.blit(Nave2,Nave2_rect)
        elif Fondo_helado==True:
            pantalla.blit(Nave3,Nave3_rect)
        elif Fondo_montaña==True:
            pantalla.blit(Nave4,Nave4_rect)
        if  Partida_Doble==True:
            pantalla.blit(Nave5,Nave5_rect)
        #Barra de vida de jugador
        if vida_perdida>=100:
            Juego_perdido=True
        if vida_perdida2>=100:
            Juego_ganado=True
        Barra_vida.barra_salud(pantalla,vida_perdida)
        if Partida_Doble==True:
            Barra_vida2.barra_salud2(pantalla,vida_perdida2)
        #Nave1################################################################
        if Fondo_espacio==True:
            Colision=colisiones1(Nave1_rect,Obstaculos_aliens)#Coliciones aliens
            Colision2=colisiones2(Nave1_rect,Monedas_lista)#Colisiones monedas
            Colision_jefe_col=colision_jefe(Nave1_rect,Jefe_lista)
               
            if Poder_im==False:
                Colision3=colisiones3(Nave1_rect,Lista_imanes)
            else:
                Suma=iman_monedas(Monedas_lista)
                if Suma!=None:
                    contador3=str(int(contador3) +Suma)
            if Poder_camp==False:
                Colision4=colisiones4(Nave1_rect,Lista_campos_fuerza)
            else:
                Colision=campo_fuerza_coll(Nave1_rect,Obstaculos_aliens)
        #Nave2##################################################################
        if Fondo_volcanico==True:
            Colision=colisiones1(Nave2_rect,Obstaculos_aliens)#Coliciones aliens
            Colision2=colisiones2(Nave2_rect,Monedas_lista)#Colisiones monedas
            Colision_jefe_col=colision_jefe(Nave2_rect,Jefe_lista)
            if Poder_im==False:
                Colision3=colisiones3(Nave2_rect,Lista_imanes)
            else:
                Suma=iman_monedas(Monedas_lista)
                if Suma!=None:
                    contador3=str(int(contador3) +Suma)
            if Poder_camp==False:
                Colision4=colisiones4(Nave2_rect,Lista_campos_fuerza)
            else:
                Colision=campo_fuerza_coll(Nave2_rect,Obstaculos_aliens)
        #Nave3####################################################################
        if Fondo_helado==True:
            Colision=colisiones1(Nave3_rect,Obstaculos_aliens)#Coliciones aliens
            Colision2=colisiones2(Nave3_rect,Monedas_lista)#Colisiones monedas
            Colision_jefe_col=colision_jefe(Nave3_rect,Jefe_lista)
            if Poder_im==False:
                Colision3=colisiones3(Nave3_rect,Lista_imanes)#Colicciones iman
            else:
                Suma=iman_monedas(Monedas_lista)
                if Suma!=None:
                    contador3=str(int(contador3) +Suma)
            if Poder_camp==False:
                Colision4=colisiones4(Nave3_rect,Lista_campos_fuerza)#Colicciones campo de fuerza
            else:
                Colision=campo_fuerza_coll(Nave3_rect,Obstaculos_aliens)
        #Nave4#################################################################
        if Fondo_montaña==True:
            Colision=colisiones1(Nave4_rect,Obstaculos_aliens)#Coliciones aliens
            Colision2=colisiones2(Nave4_rect,Monedas_lista)#Colisiones monedas
            Colision_jefe_col=colision_jefe(Nave4_rect,Jefe_lista)
            if Poder_im==False:
                Colision3=colisiones3(Nave4_rect,Lista_imanes)
            else:
                Suma=iman_monedas(Monedas_lista)
                if Suma!=None:
                    contador3=str(int(contador3) +Suma)
            if Poder_camp==False:
                Colision4=colisiones4(Nave4_rect,Lista_campos_fuerza)
            else:
                Colision=campo_fuerza_coll(Nave4_rect,Obstaculos_aliens)
        if Partida_Doble==True:
            if competidor_detec_a(Nave5_rect,Obstaculos_aliens)!=None:
                Nave5_rect.y=500
            if competidor_detec_b(Nave5_rect,Obstaculos_aliens)!=None:
                Nave5_rect.y=600
            if competidor_detec_c(Nave5_rect,Obstaculos_aliens)!=None:
                Nave5_rect.y=500
            if competidor_detec_a(Nave5_rect,Jefe_lista)!=None:
                Nave5_rect.y=600
            if competidor_detec_b(Nave5_rect,Jefe_lista)!=None:
                Nave5_rect.y=400
            if competidor_detec_c(Nave5_rect,Jefe_lista)!=None:
                Nave5_rect.y=500
        Colision_comp=competidor(Nave5_rect,Obstaculos_aliens)
        Colision_comp_jefe=competidor(Nave5_rect,Jefe_lista)
        if Colision_comp!=None:
            vida_perdida2+=Colision_comp
        if Colision_comp_jefe!=None:
            vida_perdida2+=Colision_comp_jefe
        #Colicciones multiples
        if Colision!=None and Poder_camp==False:
            vida_perdida+=Colision
        if Colision_jefe_col!=None:
            vida_perdida+=Colision_jefe_col
        if Colision2!=None and Poder_im==False:
            contador3=str(int(contador3)+Colision2)
        if Colision3!=None and Poder_im==False:
            Poder_im=True
            contador2="60"
        if Colision4!=None and Poder_camp==False:
            Poder_camp=True
            contador1="20"    
    #Botones en pantalla
    pygame.draw.rect(pantalla,(70,40,130),((1080,0),(100,700)))
    pantalla.blit(Boton_crear_partida,Boton_crear_partida_rect)
    pantalla.blit(Boton_inicio_partida,Boton_inicio_partida_rect)
    pantalla.blit(Boton_salida,Boton_salida_rect)
    pantalla.blit(Boton_ayuda,Boton_ayuda_rect)
    pantalla.blit(Acerca_de,Acerca_de_rect)

    #Habilidades
    if Juego==True:
        pygame.draw.rect(pantalla,(70,40,130),((910,500),(300,230)))
        pygame.draw.rect(pantalla,(0,0,0),((930,520),(200,170)))
        pygame.draw.rect(pantalla,(0,255,0),((940,530),(180,150)),3)
        #PC
        if Poder_camp==True:
            pygame.draw.circle(pantalla,(0,170,228),(970,560),15)
        else:
            pygame.draw.circle(pantalla,(255,0,0),(970,560),15)
        pygame.draw.circle(pantalla,(67,75,77),(970,560),15,3)
        #SC
        if Poder_im==True:
            pygame.draw.circle(pantalla,(0,170,228),(970,600),15)
        else:
            pygame.draw.circle(pantalla,(255,0,0),(970,600),15)
        pygame.draw.circle(pantalla,(67,75,77),(970,600),15,3)
        #Contador campo de fuerza
        texto_despliegue1= fuente_p.render(contador1,True,(200,200,200))
        pantalla.blit(texto_despliegue1,rectangulo_texto1) #Generar el texto
        #Contador poder iman
        texto_despliegue2= fuente_p.render(contador2,True,(200,200,200))
        pantalla.blit(texto_despliegue2,rectangulo_texto2) #Generar el texto
        #Contador moneda
        texto_despliegue3= fuente_p.render(contador3,True,(200,200,200))
        pantalla.blit(texto_despliegue3,rectangulo_texto3) #Generar el texto
        pantalla.blit(Monedas_cont,(1065,625))
        pantalla.blit(Poder_campo_fuerza,(1060,540))
        pantalla.blit(Poder_iman,(1060,580))    
   

    pygame.display.set_caption(Titulo)
   
    
    pygame.display.update()
    Reloj.tick(35)
pygame.quit()