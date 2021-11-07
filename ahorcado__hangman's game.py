#This code is writen in Python, comments in Spanish, so, if u want them in English i invite u to use https://www.deepl.com/translator
# re library  is not really necessary 4 this code, but it seemed usefull for my eyes. The idea of this code is to start with a group of 10 words, one is chosen "randomly" (we all know computers
# are unable to generate random numbers, there's a sequence we don't know used for each time we use random, so it's pseudo-random) , then
# that word is hidden (well, superseded) with low bars, and u have to guess typing a letter it's time, then u got chance to guess the full word
# if u want, then again one letter & one chance if u wanna try full word. It's de Hangman's game, u know we know.
"""El programa debe contar con las siguientes caracteristicas Debe de contener un banco de palabras con al menos 10. Al comienzo de la partida, se debe elegir una de manera aleatoria.
La mecánica es:

1.El programa pide al usuario una letra y este la escribe.

2.Comprueba si está en la palabra y en caso de error, indica que le quedan menos vidas (el jugador tiene 10 vidas al comenzar el juego).

3. Muestra la palabra con guiones en vez de las letras, cuando estás no hayan sido adivinadas.

4. El programa le pregunta si sabe la palabra oculta. De ser así, el usuario la introduce y comprueba si ha ganado o si sigue el juego.
Después de acabar el juego, se debe permitir reiniciar el juego, sin cerrar el programa.
Aspectos valorables
Adecuación a los requisitos del juego (que el programa haga lo que se pide).
Calidad del código: uso correcto de las estructuras de control, comentarios, limpieza, eficiencia…etc.
Usabilidad de la aplicación (que sea fácil interactuar con el juego).

1. Abuhado
Dícese de aquellas personas quienes tienen una apariencia que recuerda a la de un búho o ave similar.

2. Acecinar
Acto de salar las carnes y ponerlas al aire. Acción de convertir un producto cárnico en cecina.

3. Agigolado
Adjetivo, típico de la provincia de Segovia, que se usa para describir aquel a quien, al realizar algo con un poco de esfuerzo, siente que se ahoga y percibe una presión en el pecho.

4. Álveo
La madre de un accidente hidrográfico natural, normalmente un arroyo o río.

5. Arrebol
Es el efecto de la luz del Sol al proyectarse sobre las nubes matutinas y de la tarde, que les otorga tonalidades rojizas

6. Bahorrina
Conjunto de muchas cosas asquerosas que se han echado en agua, la cual se ha tornado sucia. También significa conjunto de gente soez y ruin.

7. Bonhomía
Afabilidad, sencillez, bondad y honradez en el carácter.

8. Burdégano
Híbrido entre un caballo y una asna.

9. Cagaprisas
Persona que es impaciente, quien tiene prisa siempre.

10.Supercalifragilisticoespialidoso
Expresión popularizada por la película Mary Poppins (1964) 
que parece usarse para indicar que todo puede ir más que bien. 

Se dice que la palabra en inglés (supercalifragilisticexpialidocious) 
ya la usó Helen Herman en 1931 con un sentido de grande, genial, glorioso, 
espléndido, superior, maravilloso
"""
import random,re,time,os
# necesitaré variables continuar para el while que se pueda repetir el juego, las vidas, un string para la palabra seleccionada, una lista con las letras de lapalabra para que se vayan restando las letras adivinadas
# entre otras cosas
#recuerdo a los profes que la librería os solamente funciona en Windows

palabras = ["Abuhado", "Acecinar", "Agigolado", "Álveo", "Arrebol", "Bahorrina", "Bonhomía", "Burdégano", "Cagaprisas","Supercalifragilisticoespialidoso"]
aleatorio = random.randint(0, 9)
vidas = 10
guess = ""
txt = ""  
adivinanza = palabras[aleatorio]
adivinanza = adivinanza.lower()  
txt = re.sub('[A-í]', '-', adivinanza)
adivinanza = list(adivinanza)
letras_antes = []
#txt = list(txt)
while (guess != adivinanza) and (txt != adivinanza):
    print("Bienvenido al ahorcado de Jaime, de 10 palabras se ha seleccionado", txt,''' para que la adivines.\n\t
    Necesito que en cada turno tuyo, metas una letra, date cuenta que puede llevar tilde, siempre ha de ser minúscula, y la palabra a adivinar está en minúsculas (relax).\nTen en cuenta que si metes una vocal y solamente aparece con tilde, se te resta vida\nDespués, si quieres puedes probar a meter la palabra completa.\n\t
    De acertarla, se termina el juego y puedes volver a empezar (con otra palabra) y salir. O sino seguir hasta tener la palabra. Recuerda que tienes 10 vidas,\ncada fallo o repetición de letra te resta 1.También resta poner cosas sin sentido!!!!  como más de una letra, números, símbolos, etc...\n\n\tRecuerda que las anteriores letras no las debes introducir de nuevo,son ''',letras_antes,'''\n\tTu letra: ''')
    letra = input("")
    letra = str(letra)
    letra = letra.lower()
    os.system("cls")
    #print("Por si acaso, adivinanza es ",adivinanza)
    if len(letra) > 1:
            print("\n\n\n\n\t\t\t(ㆆ _ ㆆ)    oye amigo, te he dicho una letra. No hagas trampas e introduce solamente una letra      ┌( ಠ_ಠ)┘   (つ◉益◉)つ (つ◉益◉)つ \n\n\t\t\t\tahora por listo -1 vida   ;)\n\n\n")
            vidas -= 1
            os.system("pause")
    elif letra.isalpha() == False:
            print("̿̿\n\n\n\n   ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿         oye amigo, tienes que meter texto, en concreto una letra, esto no me sirve      ╾━╤デ╦︻(▀̿Ĺ̯▀̿ ̿)  te vigilo..... y te quedas con -1 vida\n\n\n")
            vidas -= 1
            os.system("pause")
    elif letra.isalpha():
        if letra in letras_antes:
                print("\t\t┬──┬ ノ( ゜-゜ノ)\t\tEsta letra ya ha sido introducida, -1 vida  (˙ ͜ʟ˙)  mehh")
                vidas -= 1
                os.system("pause")
        elif letra in adivinanza:
                print("ok, parece que adivinaste una letra de la palabra, se la quitamos pues:\n\n\t\t\t")
                #print("De momento txt antes de sustituir es ",txt)
                x = 0
                txt = list(txt)
                while x < len(adivinanza):
                        if adivinanza[x] == letra:
                                #print("Hay que sustituir la letra",letra,"en la posición",x)
                                txt[x] = letra                
                        x += 1
                os.system("pause")                  
        elif (letra in adivinanza) == False:
                print("\n\n\t\t\t\t(¬_¬) vaya vaya, parece que esa letra no estaba en la palabra     '(ᗒᗣᗕ)՞  \n\n\n\t\t\t\t ¡¡¡¡¡-1 Vida!!!!!")
                vidas -= 1
                os.system("pause")
    letras_antes.append(letra)
    os.system("cls")
    if vidas == 0:
                os.system("cls")
                print("""________________             ________             _____              _____   _______________
                        |                |           /        \           |     \            /     | |               |     OVER  OVER
                        |                |          /   ____   \          |      \          /      | |               |     OVER  OVER
                        |     ___________|         /   /    \   \         |       \        /       | |     __________|     OVER  OVER
                        |    |                    /   /      \   \        |        \      /        | |     |               OVER  OVER
                        |    |                   /   /________\   \       |         \    /         | |     |_________      OVER  OVER
                        |    |  _________       /                  \      |     |\   \  /   /|     | |               |     OVER  OVER
                        |    | |         |     /       ______       \     |     | \   \/   / |     | |     __________|     OVER  OVER
                        |    | |__       |    /       /      \       \    |     |  \      /  |     | |     |               OVER  OVER
                        |    |____|      |   /       /        \       \   |     |   \    /   |     | |     |_________      OVER  OVER
                        |                |  /       /          \       \  |     |    \  /    |     | |               |     OVER  OVER
                        |________________| /_______/            \_______\ |_____|     \/     |_____| |_______________|     OVER  OVER """)
                print("\n\n\nLa palabra a descubrir era ",adivinanza,"\n\n")
                time.sleep(2)
                txt = adivinanza
                break
    elif txt == adivinanza:
                os.system("cls")
                print('''\n
                  __________     _________________   _______________    ____         __        ____
                 |          |   |                 | |               |  |    \       |  |      |    |
                 |  ______  |   |                 | |               |  |     \      |  |      |    |
                 |  |    |  |   |                 | |     __________|  |      \     |  |      |    |  
                 |  |____|  |   |_____       _____| |     |            |   |\  \    |  |      |    |
                 |         /          |     |       |     |_________   |   | \  \   |  |      |    |
                 |        /           |     |       |               |  |   |  \  \  |  |      |    |
                 |        \     ______|     |_____  |     __________|  |   |   \  \ |  |      |    |
                 |   ____  \   |                  | |     |            |   |    \  \|  |      |____|
                 |  |    |  |  |                  | |     |_________   |   |     \     |       ____
                 |  |____|  |  |                  | |               |  |   |      \    |      |    |
                 |__________|  |__________________| |_______________|  |___|       \___|      |____|\n\n


Te acabo de hackear las cuentas del PC, esto lleva un payload ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n 
( ━☞´◔‿ゝ◔`)━☞

( ━☞´◔‿ゝ◔`)━☞

( ━☞´◔‿ゝ◔`)━☞
''')            
                os.system("pause")
                print("\n\nBRAVO, adivinaste la palabra.\n\t\t\t\t¿Quieres volver a jugar?  si / sí / no  y le das a Enter\n\n\nRespuesta: ")
                respuesta = input("")
                respuesta = respuesta.lower()
                if (respuesta == "sí") or (respuesta == "si"):

                        print("Parece que pusiste sí, el juego continúa")
                        os.system("pause")
                        vidas = 10
                        guess = ""
                        aleatorio = random.randint(0, 9)
                        adivinanza = palabras[aleatorio]
                        letras_antes = []
                        txt = re.sub('[A-í]', '-', adivinanza)
                        txt = list(txt)                                                                                    
                else:
                        print("Has introducido 'no' o un texto no válido, ¡aquí termina el juego! \n\n\n\t\t\tgracias por jugar")
                        os.system("pause")
                        break                   #free!   God knows. G0d knows I want to break, freeee
    elif txt != adivinanza:
        print("\n\n\t\t\t¿Te apetece probar a ver si sabes la palabra?  si / sí / no / (todo lo que no sea sí será un no) \n\n\n\tRespuesta: ")
        respuesta = input("")
        respuesta = respuesta.lower()
        if (respuesta == "si") or (respuesta == "sí"):
                os.system("cls")
                print("\n\n\nRecuerda que si alguna vocal lleva tilde, la tienes que poner o fallarás este intento\n\n\t\t\tLa palabra es...  ")
                guess = input("")
                guess = list(guess)
                if guess != adivinanza:
                        print("Parece que no has acertado, el juego continúa y tienes -1 vida")
                        vidas -= 1
                        os.system("pause")
                #elif guess == adivinanza:
                        
    #os.system("cls")
    #print ("txt es",txt)                                                        podríamos decir que este codigo comentado
    #print("adivinanza es ", adivinanza)                                         me sirvió de pruebas y se quedará aquí para la posteridad
    #print("la longitud de la lista de posiciones a es", len(posiciones))        y su posible reutilizacion
    #print("posiciones de la letra en adivinanza es", posiciones)
    #print("x es ", x,"   y adivinanza[x-1] es", adivinanza[(x-1)],"\n\n\t\t\t\t\t")      we could say this commented code served me as a
    #print("la lista de letras es ", letras_antes,"\n\n")                                 try n fail test code, so will remain here 
    os.system("cls")                                                            #         for posterity and possible reuse
    x = 0
    while x < 5:
            print("\n\n\t\t\t\t\t\t",vidas,"❤\n\n\t\t\t\t\t\tVidas // Lifes\n\n")
            time.sleep(0.25)
            os.system("cls")
            time.sleep(0.15)
            x += 1
    print("\t\t\t\tPor si no lo pudiste leer, te quedan \n\n\t\t\t\t\t\t",vidas,"\tvidas\n\n")
    os.system("pause")
    os.system("cls")
        
    if vidas == 0:
                os.system("cls")
                print("""________________             ________             _____              _____   _______________
                        |                |           /        \           |     \            /     | |               |     OVER  OVER
                        |                |          /   ____   \          |      \          /      | |               |     OVER  OVER
                        |     ___________|         /   /    \   \         |       \        /       | |     __________|     OVER  OVER
                        |    |                    /   /      \   \        |        \      /        | |     |               OVER  OVER
                        |    |                   /   /________\   \       |         \    /         | |     |_________      OVER  OVER
                        |    |  _________       /                  \      |     |\   \  /   /|     | |               |     OVER  OVER
                        |    | |         |     /       ______       \     |     | \   \/   / |     | |     __________|     OVER  OVER
                        |    | |__       |    /       /      \       \    |     |  \      /  |     | |     |               OVER  OVER
                        |    |____|      |   /       /        \       \   |     |   \    /   |     | |     |_________      OVER  OVER
                        |                |  /       /          \       \  |     |    \  /    |     | |               |     OVER  OVER
                        |________________| /_______/            \_______\ |_____|     \/     |_____| |_______________|     OVER  OVER """)
                print("\n\n\nLa palabra a descubrir era ",adivinanza,"\n\n")
                time.sleep(2)
                txt = adivinanza
                break
    elif (guess == adivinanza) or (txt == adivinanza):
        os.system("cls")
        print(''' __________     _________________   _______________    ____         __        ____
                 |          |   |                 | |               |  |    \       |  |      |    |
                 |  ______  |   |                 | |               |  |     \      |  |      |    |
                 |  |    |  |   |                 | |     __________|  |      \     |  |      |    |  
                 |  |____|  |   |_____       _____| |     |            |   |\  \    |  |      |    |
                 |         /          |     |       |     |_________   |   | \  \   |  |      |    |
                 |        /           |     |       |               |  |   |  \  \  |  |      |    |
                 |        \     ______|     |_____  |     __________|  |   |   \  \ |  |      |    |
                 |   ____  \   |                  | |     |            |   |    \  \|  |      |____|
                 |  |    |  |  |                  | |     |_________   |   |     \     |       ____
                 |  |____|  |  |                  | |               |  |   |      \    |      |    |
                 |__________|  |__________________| |_______________|  |___|       \___|      |____|

Te acabo de hackear las cuentas del PC, esto lleva un payload ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°) 
( ━☞´◔‿ゝ◔`)━☞

( ━☞´◔‿ゝ◔`)━☞

( ━☞´◔‿ゝ◔`)━☞
''')            
        os.system("pause")
        print("\n\n\t\t\tnah es broma  ◔̯◔    (◟ᅇ)◜   ( ━☞´◔‿ゝ◔`)━☞  \n\n\n\n\n\t\tPulsa alguna tecla para continuar")
        os.system("pause") 
        os.system("cls")
        print("\n\nBRAVO, adivinaste la palabra.\n\t\t\t\t¿Quieres volver a jugar? (wanna play again?)\n\t  si / sí / no  + Enter (type yes or no in Spanish)\n\n\nRespuesta: ")
        respuesta = input("")
        respuesta = respuesta.lower()
        if (respuesta == "sí") or (respuesta == "si"):
                print("Parece que pusiste sí, el juego continúa")
                os.system("pause")
                vidas = 10
                guess = ""
                aleatorio = random.randint(0, 9)
                adivinanza = palabras[aleatorio]
                letras_antes = []
                txt = re.sub('[A-í]', '-', adivinanza)
                txt = list(txt)                                                                                    
        else:
                        print("Has introducido 'no' o un texto no válido, ¡aquí termina el juego! \n\n\n\t\t\tgracias por jugar")
                        os.system("pause")
                        txt = adivinanza
                        break  #free!   God knows. G0d knows I want to break, freeee                              
