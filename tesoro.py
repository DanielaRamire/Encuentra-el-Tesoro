print("Hola Viajera(o) ")
nombrev = input("¿Como te llamas?  ")
print("hola  ",nombrev)
print("Desde ahora empezaras tu aventura")
print("Bienvenido a la isla Tu mision sera encontrar el tesoro")

print("Unos mostruos se acercan ,decide un camino para sobrevivir")
primerad = input("¿Derecha o izquierda? o ¿No sabes? ")

if primerad == "Derecha":   
    print("caiste en agujero")
    segundad=input("¿corres o esperas?")
    tercerad= input("Tomas una o la dos llaves")
    if segundad == "correr":
        print("Te salvaste,encuentras dos llaves ")
        print("")
        llaves = input("tomas una o las dos llaves")
        if llaves == "una":
            print("No es la llave")
            print("Game Over") 
            print("Fin")
        else:
            print("Abriste el tesoro")
            
    elif segundad == "esperar":
        print("Te devoro un oso")
        print("Game Over")       
        print("Fin")
elif primerad == "Izquierda":

     equipos = input("Nadar o esperar")
     if equipos== "nadar":
        print("Atacado por una tribu Game Over")
        print("fin")
     

     else:
        print("aparecen tres puertas")
        puerta = input("selecciona una puerta, la roja,la azul? o la amarilla")
        if puerta == "azul":
            print("Devorado por bestias Game Over")
            print("Fin")
        elif puerta == "roja":
            print("Eres quemado Gamer Over")
            print("Fin")
        elif puerta == "amarilla":
            print("Haz ganado ")
            print("Fin")
        
        else:
            print("Perdiste")
            print("Fin")



else:
    print("Llega otro buscador de tesoro")
    print("Le propone ir juntos en busqueda del cofre")
    aceptacion = input("¿Aceptas?  ")
    if aceptacion == "si":
        print("Los caminos desaparecieron se perdieron")
        print("Juntos encuentran un pasadizo secreto")
       
        pasadizo = input("¿Ingresar al pasadizo?")

        if pasadizo == "si":
            print("Descubren el tesoro perdido")
            print("Ganaron")
        elif pasadizo =="no":
            print("muerte por inanicion")
            print("Fin")
        
    else:
       print("Los caminos desaparecieron te perdiste")
       print("muerte por inanicion")
       print("Fin")


