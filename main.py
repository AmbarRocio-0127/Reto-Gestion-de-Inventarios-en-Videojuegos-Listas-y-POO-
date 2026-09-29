"""Practica de Listas + POO"""
from clases.Item import Item

"""Inventario de Jugador"""
mochila = [
        Item("🗡️ Daga de Plata ⚔️ ", "Arma", 45),
        Item("🧪 Poción de Vida 🧴 ", "Poción", 50),
        Item("🛡️ Escudo de Acero 🛡️ ", "Escudo", 20)
    ]

"""Menu Principal"""
def menu_principal():
     print("\n===== 🎮 Gestion De Inventario De Videojuegos 🎮 =====")
     print("\n1) Mostrar equipamiento de Arsenal🎒 \n2) Modificando Arsenal⚙️ \n3) Insertar un Arsenal extra ➕📦 \n4) Arsenal Disponible🛡️⚔️ \n5) Salir 🔚")

"""Funcion para mostrar el equipamiento de articulos"""
def equipamiento_articulos():
    print(f"\n🎒 Mochila Cargada. 🧰 Items en inventario: {len(mochila)}")
    print(f"\n ⚔️ Articulo Equipado ⚔️: {mochila[0].nombre} \n 💥 Daño Base 💥: {mochila[0].poder}")
    
"""Funcion para modificar los objetos de la lista"""
def Modificando_objeto_lista():
    mochila[0].poder += 15
    print(f"\n🆙¡{mochila[0].nombre} Mejorada! ⚡Nuevo poder: {mochila[0].poder} ⚡")

"""Funcion para agregar mas objetos en la lista"""
def insertando_articulo():
    botin = Item("Espada de Acero", "Arma", 45)
    mochila.append(botin)
    
"""Funcion para listar Arsenal Disponible y con validación correspondiente"""
def arsenal_disponible():
    print("\n⚔️🛡️ ARSENAL DISPONIBLE 🛡️  ⚔️")
    for item in mochila:
        if item.tipo == "Arma":
            print(f"\n🎒 Ítem: {item.nombre}\n🏷️ Tipo: {item.tipo}\n⚡ Poder/Efecto: {item.poder} pts\n" + "-" * 35)
            print(f"\n ⚔️¡LISTA PARA LUCHAR! ⚔️🔥 Puedes usar tu {item.nombre} 🛡️ (Poder: {item.poder}) ⚡")
        else:
            print(f"\n🎒 Ítem: {item.nombre}\n🏷️ Tipo: {item.tipo}\n⚡ Poder/Efecto: {item.poder} pts\n" + "-" * 35)
def main():
    while True:
        menu_principal()
        opcion = int(input("\n🎯 Seleccione la opción deseada🕹️: "))
        match opcion:
            case 1:
                equipamiento_articulos()
            case 2:
                Modificando_objeto_lista()
            case 3:
                insertando_articulo()
            case 4:
                arsenal_disponible()
            case 5:
                break
            case _:
                print("\n⚠️ ¡Opción inválida! Por favor seleccione una opción válida.⚠️")

main()