#coding:UTF-8
from graphics import *
import time
import random
from math import sqrt


def main():
    
    jogar = False
    inicio = True
    
    
    janela = GraphWin("BEM VINDO AO CHORIS",800,600) #Cria a janela principal
    inicio = Image(Point(400,300),"inicio.png")
    inicio.draw(janela)
    checkinicio = janela.getMouse()
    x = checkinicio.getX()
    y = checkinicio.getY()
   
    

    if x > 536 and x<721 and y > 337 and y < 393:     # CONFERE SE O BOTÃO JOGAR FOI SELECIONADO
        jogar=True
        janela.close()

    if x > 98 and x<281  and y>336 and y<394:
        janela.close()
        comandos = GraphWin("COMANDOS",800,600)        # CRIA A JANELA DE COMANDOS
        comandos.setBackground("Purple")
        comand = Text(Point(400,300),"COMANDOS:\nAS SETAS INDICAM A DIREÇÃO EM QUE O CHORIS IRÁ SE MOVER")  #COMANDOS
        comand.setSize(15)
        comand.draw(comandos)
        jogoini = Text(Point(500,400),"(JOGAR)")
        jogoini.setSize(12)
  
        jogoini.draw(comandos)
        check2 = comandos.getMouse()
        a = check2.getX()
        b = check2.getY()
        
        if a>462 and a<534  and b>389 and b<408 :
            jogar = True                                                       # CONFERE SE PODE COMEÇAR O JOGO
            comandos.close()
   
        
    

    if jogar == True:
        jogo = GraphWin("CHORIS",800,600)                                  # CRIA A JANELA DO JOGO
        cenario = Image(Point(400,300),"cena.png")                         # CRIA CENÁRIO
        cenario.draw(jogo)
        cenario2 = Image(Point(1197,300),"cena.png")        
        cenario2.draw(jogo)
        
        choris = Image(Point(150,470),"choris0.png")          # PERSONAGEM
        choris.draw(jogo)
        boxchoris = Circle(Point(150,500),25)
        

        obstaculo = Image(Point(820,510),"cone2.png")          # CRIA O PRIMEIRO OBSTÁCULO 
        circulo = Circle(Point(820,510),20)
        obstaculo.draw(jogo)
    
        
        obstaculo2 = Image(Point(850,540),"cone2.png")         # CRIA O SEGUNDO OBSTÁCULO 
        circulo2 = Circle(Point(850,540),20)
        obstaculo2.draw(jogo)
      

        obstaculo3 = Image(Point(880,485),"cone2.png")          # CRIA O TERCEIRO OBSTÁCULO 
        circulo3 = Circle(Point(880,485),20)
        obstaculo3.draw(jogo)
     

        obstaculo4 = Image(Point(1100,510),"cone2.png")         # CRIA O QUARTO OBSTÁCULO 
        circulo4 = Circle(Point(1100,510),20)
        obstaculo4.draw(jogo)
    
        
        obstaculo5 = Image(Point(1800,540),"cone2.png")         # CRIA O QUINTO OBSTÁCULO 
        circulo5 = Circle(Point(1800,540),20)
        obstaculo5.draw(jogo)


        obstaculo6 = Image(Point(1400,485),"cone2.png")         # CRIA O SEXTO OBSTÁCULO  
        circulo6 = Circle(Point(1400,485),20)
        obstaculo6.draw(jogo)

        end = False
    
        jogo.ligar_Buffer()         #LIGA O BUFFER DO CHECKKEY()
        colisao = False             #Colisão não detectada
        pontos = 0                  #SETA OS PONTOS PARA 0 
        
        while end!=True:
            framerate = 1/60.0
            velocidade = -500           # VELOCIDADE DOS CONES
            velocidade2 = -400
            velocidade3 = -300
            velocidade4 = -500         
            velocidade5 = -400
            velocidade6 = -300
            velcenario = -150           #VELOCIDADE DO CENÁRIO
            velo2 = -40
            tecla1 = jogo.checkKey_Buffer()
            update()
            
            
            if tecla1 == "Escape":              #CONFERE SE A TECLA ESC FOI PRESSIONADA
                end = True
            else:
                end = False
            

            xA = boxchoris.getCenter().getX()                             
            xB = circulo.getCenter().getX()
            yA = boxchoris.getCenter().getY()
            yB = circulo.getCenter().getY()
            
            distancia = sqrt((xA-xB)**2) + ((yA-yB)**2)
        
            somaDosRaios = boxchoris.getRadius() + circulo.getRadius()
            
            if (distancia < somaDosRaios):              # DETECÇÃO DE COLISÃO
                colisao = True

            ################################################
            
            
            xA2 = boxchoris.getCenter().getX()
            xB2 = circulo2.getCenter().getX()
            yA2 = boxchoris.getCenter().getY()
            yB2 = circulo2.getCenter().getY()
            
            distancia2 = sqrt((xA2-xB2)**2) + ((yA2-yB2)**2)
        
            somaDosRaios2 = boxchoris.getRadius() + circulo2.getRadius()

            
            if (distancia2 < somaDosRaios2):
                colisao = True
            

            #################################################
            
            xA3 = boxchoris.getCenter().getX()
            xB3 = circulo3.getCenter().getX()
            yA3 = boxchoris.getCenter().getY()
            yB3 = circulo3.getCenter().getY()
            
            distancia3 = sqrt((xA3-xB3)**2) + ((yA3-yB3)**2)
        
            somaDosRaios3 = boxchoris.getRadius() + circulo3.getRadius()

            
            if (distancia3 < somaDosRaios3):
                colisao = True
            
            #################################################
            
            xA4 = boxchoris.getCenter().getX()                             
            xB4 = circulo4.getCenter().getX()
            yA4 = boxchoris.getCenter().getY()
            yB4 = circulo4.getCenter().getY()
            
            distancia4 = sqrt((xA4-xB4)**2) + ((yA4-yB4)**2)
        
            somaDosRaios4 = boxchoris.getRadius() + circulo4.getRadius()
            
            if (distancia4 < somaDosRaios4):              # DETECÇÃO DE COLISÃO
                colisao = True

            ################################################
            
            
            xA5 = boxchoris.getCenter().getX()
            xB5 = circulo5.getCenter().getX()
            yA5 = boxchoris.getCenter().getY()
            yB5 = circulo5.getCenter().getY()
            
            distancia5 = sqrt((xA5-xB5)**2) + ((yA5-yB5)**2)
        
            somaDosRaios5 = boxchoris.getRadius() + circulo5.getRadius()

            
            if (distancia5 < somaDosRaios5):
                colisao = True
            

            #################################################
            
            xA6 = boxchoris.getCenter().getX()
            xB6 = circulo6.getCenter().getX()
            yA6 = boxchoris.getCenter().getY()
            yB6 = circulo6.getCenter().getY()
            
            distancia6 = sqrt((xA6-xB6)**2) + ((yA6-yB6)**2)
        
            somaDosRaios6 = boxchoris.getRadius() + circulo6.getRadius()

            
            if (distancia6 < somaDosRaios6):
                colisao = True
            
            #################################################
            
            
            ################################################
            
            
            if circulo.getCenter().getX()+20 <= 0:
                obstaculo.move(820,0)
                circulo.move(820,0)

            if circulo2.getCenter().getX()+20 <= 0:
                obstaculo2.move(850,0)
                circulo2.move(850,0)    

            if circulo3.getCenter().getX()+20 <= 0:
                obstaculo3.move(880,0)
                circulo3.move(880,0)

            if circulo4.getCenter().getX()+20 <= 0:
                obstaculo4.move(840,0)
                circulo4.move(840,0)

            if circulo5.getCenter().getX()+20 <= 0:
                obstaculo5.move(870,0)
                circulo5.move(870,0)    

            if circulo6.getCenter().getX()+20 <= 0:
                obstaculo6.move(930,0)
                circulo6.move(930,0)
            

            if colisao == False:
                obstaculo.move(velocidade * framerate, 0)
                circulo.move(velocidade*framerate,0)
                

                obstaculo2.move(velocidade2 * framerate, 0)
                circulo2.move(velocidade2*framerate,0)
                

                obstaculo3.move(velocidade3 * framerate, 0)
                circulo3.move(velocidade3*framerate,0)
                

                obstaculo4.move(velocidade * framerate, 0)
                circulo4.move(velocidade*framerate,0)
                

                obstaculo5.move(velocidade2 * framerate, 0)
                circulo5.move(velocidade2*framerate,0)
                
                
                obstaculo6.move(velocidade3 * framerate, 0)
                circulo6.move(velocidade3*framerate,0)
                
                cenario.move(velcenario*framerate,0)            
                cenario2.move(velcenario*framerate,0) 
                pontos = pontos+20*framerate
                print("%.2f" %pontos)
                update()
                
                if pontos > 150:
                    velocidade = velocidade*5
                    velocidade2 = velocidade2*5
                    velocidade3 = velocidade3*5
                    velcenario += - 20 
                    pontos = pontos+22*framerate
                    if pontos > 250:        
                        velocidade = velocidade*5
                        velocidade2 = velocidade2*5
                        velocidade3 = velocidade3*5
                        velcenario += - 20  
                        pontos = pontos+23*framerate
                    if pontos > 350:
                        velocidade = velocidade*5
                        velocidade2 = velocidade2*5
                        velocidade3 = velocidade3*5 
                        velcenario += - 20      
                        pontos = pontos+25*framerate          
                    if pontos > 450:
                        velocidade = velocidade*5
                        velocidade2 = velocidade2*5
                        velocidade3 = velocidade3*5
                        velcenario += - 20 
                        pontos = pontos+40*framerate
                        
                    if pontos >= 5000:
                        jogo.close()
                        venceu = GraphWin("YOU WINNN",800,600)                      #TELA DE VENCER
                        win = Image(Point(400,300),"win.png")
                        win.draw(venceu)
                        venceu.getMouse()
                        venceu.close()
                        end = True

               

                jogo.update()
                time.sleep(framerate)
            else: 
                jogo.close()
                gameover = GraphWin("Game-Over :(",800,600)             # FIM DE JOGO 
                fim = Image(Point(400,300),"endgame.png")
                fim.draw(gameover)
                numpontos = Text(Point(600,225),"%.2f" %pontos)
                numpontos.setSize(30)
                numpontos.setStyle("italic")
                numpontos.setTextColor("white")
                numpontos.draw(gameover)
                final = gameover.getMouse()
                gameover.close()
                end = True
            
            if cenario2.getAnchor().getX()<= 400:
                cenario.move(800,0)
                cenario2.move(799,0)
            
            def movimenta():   # FUNÇÃO DE MOVIMENTAÇÃO
                cima = False
                baixo = False

                if len(tecla1)>0 and "Up" in tecla1 :
                    cima = True
                    choris.move(0,-4)
                    boxchoris.move(0,-4)
                if cima == True and boxchoris.getCenter().getY()-22 <= 450 and boxchoris.getCenter().getY()-22 < 510   :
                    choris.move(0,10)
                    boxchoris.move(0,10)

                if len(tecla1)>0 and "Down" in tecla1 :
                    baixo = True
                    choris.move(0,4)
                    boxchoris.move(0,4)
                if baixo == True and boxchoris.getCenter().getY()+22 >= 565 and boxchoris.getCenter().getY()-22 < 555   :
                    choris.move(0,-10)
                    boxchoris.move(0,-10)
                    
                if len(tecla1)>0 and "Left" in tecla1:
                    choris.move(-4,0)
                    boxchoris.move(-4,0)
                if len(tecla1)>0 and "Right" in tecla1:
                    choris.move(4,0)
                    boxchoris.move(4,0)
                if choris.getAnchor().getX() - 10 <= 20:
                    choris.move(15,0)
                    boxchoris.move(15,0)
                if choris.getAnchor().getX() +20 >= 780:
                    choris.move(-15,0)
                    boxchoris.move(-15,0)
            movimenta()
            
         
main()
    
    
    
    

   