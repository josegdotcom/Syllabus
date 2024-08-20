
import copy
# para regar
def cuadrado_sin_esquinas(mapa, z, epi_y, epi_x):
    # delimitamos los limites
    y_up = max(0, epi_y - z)
    y_down = min(len(mapa) - 1, epi_y + z)
    x_left = max(0, epi_x - z)
    x_right = min(len(mapa[0]) - 1, epi_x + z)
    # empezamos a regar excepto las esquinas
    for y in range(y_up, y_down + 1):
        for x in range(x_left, x_right + 1):
            if (epi_y - z == y and epi_x + z == x) or (epi_y + z == y and epi_x - z == x) or (epi_y - z == y and epi_x - z == x) or (epi_y + z == y and epi_x + z == x):
                mapa[y][x] = mapa[y][x]
            else:
                mapa[y][x] += 1
    # regado
    return mapa
# es hora de plantar
def plantar_cuadrado(plano, codigo_cultivo, coordenadas, alto, ancho):
    # quien es mapa al igual que las filas y columnas
    fila, columna = coordenadas 
    mapa = plano 
    # si se pasa NO
    if fila + alto > len(mapa) or columna + ancho > len(mapa[0]):
        return mapa, "can't"
    #si lla hay algo entonces NO
    for y in range(fila, fila + alto):
        for x in range(columna, columna + ancho):
            if mapa[y][x] != "X":
                return mapa, "can't"
    # lest plant
        for y in range(fila, fila + alto):
            for x in range(columna, columna + ancho):
                mapa[y][x] = codigo_cultivo
    # listo y con un mensaje que tabien
    return mapa, "bien"
#para las plagas
def plagas(mapa, i, j):
    #ubicamos al que hay que eliminar
    afectado = mapa[i][j]
    #en caso de que no exista
    if afectado == "X":
        return 0
    # definimos las cositas
    filas = len(mapa)
    columnas = len(mapa[0])
    celdas_eliminadas = 0
    # (esto era antes whiles) delimitamos el largo de la zone afectada
    y_fin = i
    for y in range(i, filas):
        if mapa[y][j] != afectado:
            break
    y_fin = y
    # ahora el ancho
    x_fin = j
    for x in range(j, columnas):
        if mapa[i][x] != afectado:
            break
    x_fin = x
    # contamos las celdas eliminadas y las eliminamos
    for y in range(i, y_fin + 1):
        for x in range(j, x_fin + 1):
            if mapa[y][x] == afectado:
                mapa[y][x] = "X"
                celdas_eliminadas += 1
    # exterminate
    return celdas_eliminadas


class Predio:
    def __init__(self, codigo_predio: str, alto: int, ancho: int) -> None:
        self.codigo_predio = codigo_predio
        self.alto = alto
        self.ancho = ancho
        self.plano = []
        self.plano_riego = []

    def crear_plano(self, tipo: str) -> None:
        mapa = []
        for i in range(self.alto):
            mapa.append([" "] * self.ancho)

        for y in range(self.alto):
            for x in range(self.ancho):
                if tipo == "normal":
                    mapa[y][x] = "X"
                elif tipo == "riego":
                    mapa[y][x] = 0

        if tipo == "normal":
            self.plano = mapa
        elif tipo == "riego":
            self.plano_riego = mapa
        

    def plantar(self, codigo_cultivo: int, coordenadas: list, alto: int, ancho: int) -> None:
        mapa = self.plano
        new_mapa, wtf = plantar_cuadrado(mapa, codigo_cultivo, coordenadas, alto, ancho)
        if wtf == "bien":
            self.plano = new_mapa

    def regar(self, coordenadas: list, area: int) -> None:
        mapa = self.plano_riego
        new_mapa = cuadrado_sin_esquinas(mapa, area, coordenadas[0], coordenadas[1])
        self.plano_riego = new_mapa

    def eliminar_cultivo(self, codigo_cultivo: int) -> int:
        total_celdas_eliminadas = 0
        mapa = self.plano

        for y in range(len(mapa)):
            for x in range(len(mapa[0])):
                if mapa[y][x] == codigo_cultivo:
                    celdas_eliminadas = plagas(mapa, y, x)
                    total_celdas_eliminadas += celdas_eliminadas

        self.plano = mapa
        return total_celdas_eliminadas


class DCCultivo:
    def __init__(self) -> None:
        self.predios = []

    def crear_predios(self, nombre_archivo: str) -> str:
        try:
            with open (nombre_archivo, "r") as arch:
                contenidos = arch.readlines()
                for cont in contenidos:
                    cont = cont.rstrip().split(",")
                    new_predio = Predio(cont[0], int(cont[1]), int(cont[2]))
                    new_predio.crear_plano("normal"); new_predio.crear_plano("riego")
                    self.predios.append(new_predio)

            return "Predios de DCCultivo cargados exitosamente"

        except FileNotFoundError:
            return "Fallo en la carga de DCCultivo"

    def buscar_y_plantar(self, codigo_cultivo: int, alto: int, ancho: int) -> bool:
        for predio in self.predios:
            mapa = predio.plano
            for y in range(len(mapa)):
                for x in range(len(mapa[0])):
                    _, resultado = plantar_cuadrado(mapa, codigo_cultivo, [y, x], alto, ancho)

                    if resultado == "bien":
                        predio.plantar(codigo_cultivo, [y, x], alto, ancho)
                        return True
        
        return False

    def buscar_y_regar(self, codigo_predio: str, coordenadas: list, area: int) -> None:
        for pre in self.predios:
            if pre.codigo_predio == codigo_predio:
                pre.regar(coordenadas, area)

    def detectar_plagas(self, lista_plagas: list[list]) -> list[list]:
        danos = []; ya = []
        for plaga in lista_plagas:
            codigo_predio, coordenadas = plaga[0], plaga[1]
            for pre in self.predios:
                if pre.codigo_predio == codigo_predio:
                    la_plaga = pre.plano[coordenadas[0]][coordenadas[1]]
                    celdas_eliminadas = pre.eliminar_cultivo(la_plaga)

                    if celdas_eliminadas > 0 and pre.codigo_predio not in ya:
                        danos.append([pre.codigo_predio, celdas_eliminadas])
                        ya.append(pre.codigo_predio)

                    elif celdas_eliminadas > 0 and pre.codigo_predio in ya:
                        for i in range(len(danos)):
                            if danos[i][0] == pre.codigo_predio:
                                danos[i][1] += celdas_eliminadas
        
        danos.sort(key=lambda x: (x[1], x[0]))
        return danos
