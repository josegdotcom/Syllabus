import pretty_print as pp
import entities as en

# imprimir todos los items de la lista
def print_items(items) -> None:
    print("> Items para elegir:")
    for i in range(len(items)):
        print(
            f"{i+1}) {items[i].nombre}: ${items[i].precio} / {items[i].puntos} puntos"
        )
        
# cargamos los nuevos items
def cargar_intems() -> list:
    charge = []
    with open("items.dcc", "r") as i:
        items = i.readlines()
        for item in items:
            item = item.rstrip().split(",")
            new_item = Item(item[0], int(item[1]),int(item[2]))
            charge.append(new_item)
    return charge

# creamos un usuario nuevo
def crear_usuario(tiene_subs: bool) -> Usuario:
    new_user = en.Usuario(tiene_subs)
    en.new_user.print_usuario
    return new_user

if __name__ == "__main__":
    yo = crear_usuario(True)
    carga = cargar_intems()
    pp.print_items(carga)
    for car in carga:
        yo.en.agregar_item(car)
    pp.yo.print_canasta()
    en.yo.comprar()
    pp.yo.print_usuario()