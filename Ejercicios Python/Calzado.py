


print('Bienvenidos Calzado Su Tienda')
print()
print()
disponible = int(input('De cuanto dinero dispone?: '))
print()
compra = 0
compra_articulos = []
compra_precio = []
precios_siniva = []
cant_articulos = []
multi_precios = []
multi_precio_siniva = []

while disponible >= 15000:
  print()
  print(f'Muy bien, dispones de ¢{disponible} para tus compras')
  compra1 = 0
  print('Que tipo de calzado busca?')
  print()
  print('1. Zapatos de vestir')
  print('2. Zapatos de trabajo')
  print('3. Tennis')
  print()
  opcion = int(input('Digite una opcion: '))
  print()

  if opcion == 1:
    print('Este es el menu de zapatos para vestir')
    print('1. Zapatillas = ¢15000')
    print('2. Suecos = ¢16000')
    print('3. Zapato de punta = ¢22000')
    print('Todos los precios incluyen el impuesto')

    opcion1 = int(input('Que zapato desea comprar?: '))

    if opcion1 == 1:
      cant1 = int(input('Elegiste Zapatillas, cuantos desea llevar?: '))
      compra1 = compra1 + (cant1 * int(15000))
      if compra1 < disponible:
        compra_articulos.append('Zapatillas')
        compra_precio.append(15000)
        cant_articulos.append(cant1)
        multi_precio_siniva.append(1.13)
      else:
        print('Vaya, lo minimo para gastar son ¢15000')
        break

    elif opcion1 == 2:
      cant1 = int(input('Elegiste Suecos, cuantos desea llevar?: '))
      compra1 = compra1 + (cant1 * 16000)
      if compra1 < disponible:
        compra_articulos.append('Suecos')
        compra_precio.append(16000)
        cant_articulos.append(cant1)
        multi_precio_siniva.append(1.13)
      else:
        print('Vaya, lo minimo para gastar son ¢15000')
        break

    elif opcion1 == 3:
      cant1 = int(input('Elegiste Zapatos de punta, cuantos desea llevar?: '))
      compra1 = compra1 + (cant1 * 22000)
      if compra1 < disponible:
        compra_articulos.append('Zapatos de punta')
        compra_precio.append(22000)
        cant_articulos.append(cant1)
        multi_precio_siniva.append(1.13)
      else:
        print('Vaya, lo minimo para gastar son ¢15000')
        break

    else:
      print()
      print('Opcion invalida')

  elif opcion == 2:
    print('Este es el menu de zapatos de trabajo')
    print('1. Caterpilar = ¢35000')
    print('2. Timberland = ¢26000')
    print('3. High Tech = ¢22000')
    print('Todos los precios incluyen el impuesto')

    opcion2 = int(input('Que zapato desea comprar?: '))

    if opcion2 == 1:
      cant2 = int(input('Elegiste Caterpilar, cuantos desea llevar?: '))
      compra1 = compra1 + (cant2 * 35000)
      if compra1 < disponible:
        compra_articulos.append('Caterpilar')
        compra_precio.append(35000)
        cant_articulos.append(cant2)
        multi_precio_siniva.append(1.13)
      else:
        print('Vaya, lo minimo para gastar son ¢15000')
        break
