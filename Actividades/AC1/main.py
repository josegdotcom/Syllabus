import collections
from os.path import join
from utilidades import Anime  # Debes utilizar esta nametupled



def cargar_animes(ruta_archivo: str) -> list:
    carga_an = []
    with open(ruta_archivo, "r")as ra:
        rutas_a = ra.readlines()
        for ruta in rutas_a:
           ruta = ruta.rstrip().split(",")
           ruta[5] = ruta[5].split(";"); ruta[1] = int(ruta[1]); ruta[2] = int(ruta[2]); ruta[3] = int(ruta[3]); ruta[5].sort()
           an = Anime(ruta[0], ruta[1], ruta[2], ruta[3], ruta[4], ruta[5])
           carga_an.append(an)
    return carga_an


#####################################
#        Parte 2 - Consultas        #
#####################################
def animes_por_estreno(animes: list) -> dict:
    return "COMPLETAR"


def descartar_animes(generos_descartados: set, animes: list) -> list:
    return "COMPLETAR"


def resumen_animes_por_ver(*animes: Anime) -> dict:
    return "COMPLETAR"


def estudios_con_genero(genero: str, **estudios: list) -> list:
    return "COMPLETAR"


if __name__ == "__main__":
    #####################################
    #       Parte 1 - Cargar datos      #
    #####################################
    animes = cargar_animes(join("data", "ejemplo.chan"))
    indice = 0
    for anime in animes:
        print(f"{indice} - {anime}")
        indice += 1

"""    #####################################
    #        Parte 2 - Consultas        #
    #####################################
    # Solo se usará los 2 animes del enunciado.
    datos = [
        Anime(
            nombre="Hunter x Hunter",
            capitulos=62,
            puntaje=9,
            estreno=1999,
            estudio="Nippon Animation",
            generos={"Aventura", "Comedia", "Shonen", "Acción"},
        ),
        Anime(
            nombre="Sakura Card Captor",
            capitulos=70,
            puntaje=10,
            estreno=1998,
            estudio="Madhouse",
            generos={"Shoujo", "Comedia", "Romance", "Acción"},
        ),
    ]

    # animes_por_estreno
    estrenos = animes_por_estreno(datos)
    print(estrenos)

    # descartar_animes
    animes = descartar_animes({"Comedia", "Horror"}, datos)
    print(animes)

    # resumen_animes_por_ver
    resumen = resumen_animes_por_ver(datos[0], datos[1])
    print(resumen)

    # estudios_con_genero
    estudios = estudios_con_genero(
        "Shonen",
        Nippon_Animation=[datos[0]],
        Madhouse=[datos[1]],
    )
    print(estudios)"""
