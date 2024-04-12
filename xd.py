total=0
aux=0

while aux!=5:
    print("")
    aux=int(input("Menu\n1)Papas fritas a $1000\n2)Completo Italiano a $1400\n3)Cerveza a $3000\n4)Promociones\n5)Salir\n"))
    if aux>5 or aux<1:
        print("Ingrese solo opciones válidas")
        aux=int(input("Menu\n1)Papas fritas a $1000\n2)Italiano a $1400\n3)Cerveza a $3000\n4)Promociones\n5)Salir\n"))

    if aux==1:
        print("")
        print("Ha seleccionado Papas Fritas")
        total=total+1000

    if aux==2:
        print("")
        print("Ha seleccionado Completo Italiano")
        total=total+1400

    if aux==3:
        print("")
        print("Ha seleccionado Cerveza")
        total=total+3000

    if aux==4:
        print("")
        aux2=0
        while aux2!=4:
            aux2=int(input("Las promociones son las siguientes\n1)Papas Fritas + Bebida a $1500\n2)Completo Italiano + Cerveza a $3000\n3)Completo Italiano + Bebida a 1800$\n4)Salir\n"))
            if aux2==1:
                print("")
                print("Ha escogido la oferta de Papas fritas + bebida")
                total=total+1500

            if aux2==2:
                print("")
                print("Ha escogido la ofeta completo italiano + cerverza")
                total=total+3000

            if aux2==3:
                print("")
                print("Ha escogido la oferta completo italiano + bebida")
                total=total+1800
                
        print("ha salido del menu de promociones")



print(f"su total es de {total}")