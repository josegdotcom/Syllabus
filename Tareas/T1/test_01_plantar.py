import unittest
from dccultivo import Predio
from tests_publicos.timeout_function import timeout

N_SECOND = 10


class TestPlantar(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Ejemplo básico del enunciado. Plano vacío 5x7, código_predio = 1.
        código_cultivo = 3, dimensiones 3x3, plantar en (0,0).
        """
        plano = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio = Predio(codigo_predio="1", alto=5, ancho=7)
        predio.plano = plano

        resultado_estudiante = predio.plantar(
            codigo_cultivo=3, coordenadas=[0, 0], alto=3, ancho=3
        )
        resultado_esperado = [
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in resultado_esperado:
            print(fila)

        self.assertIsNone(resultado_estudiante)
        self.assertListEqual(predio.plano, resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Caso esquina, bloque pequeño. Plano vacío 7x7, código_predio = 7.
        código_cultivo = 5, dimensiones 1x1, plantar en (6,0).
        """
        plano = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio = Predio(codigo_predio="8", alto=7, ancho=7)
        predio.plano = plano

        resultado_estudiante = predio.plantar(
            codigo_cultivo=5, coordenadas=[6, 0], alto=1, ancho=1
        )
        resultado_esperado = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            [5, "X", "X", "X", "X", "X", "X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in resultado_esperado:
            print(fila)

        self.assertIsNone(resultado_estudiante)
        self.assertListEqual(predio.plano, resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Caso con cultivos ya agregados. Plano 3x2, código_predio = 2.
        código_cultivo = 4, dimensiones 2x2, plantar en (1,0).
        """
        plano = [
            [6, 6],
            ["X", "X"],
            ["X", "X"],
        ]

        predio = Predio(codigo_predio="2", alto=3, ancho=2)
        predio.plano = plano

        resultado_estudiante = predio.plantar(
            codigo_cultivo=4, coordenadas=[1, 0], alto=2, ancho=2
        )
        resultado_esperado = [
            [6, 6],
            [4, 4],
            [4, 4],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in resultado_esperado:
            print(fila)

        self.assertIsNone(resultado_estudiante)
        self.assertListEqual(predio.plano, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Caso con cultivos ya agregados (varios). Plano 4x9, código_predio = 15.
        código_cultivo = 0, dimensiones 2x4, plantar en (2,2).
        """
        plano = [
            [1, 1, 7, 7, "X", 9, "X", 2, "X"],
            [1, 1, 6, 6, "X", 9, "X", "X", 3],
            ["X", "X", "X", "X", "X", "X", 3, 4, 4],
            ["X", "X", "X", "X", "X", "X", "X", 4, 4],
        ]

        predio = Predio(codigo_predio="15", alto=4, ancho=9)
        predio.plano = plano

        resultado_estudiante = predio.plantar(
            codigo_cultivo=0, coordenadas=[2, 2], alto=2, ancho=4
        )
        resultado_esperado = [
            [1, 1, 7, 7, "X", 9, "X", 2, "X"],
            [1, 1, 6, 6, "X", 9, "X", "X", 3],
            ["X", "X", 0, 0, 0, 0, 3, 4, 4],
            ["X", "X", 0, 0, 0, 0, "X", 4, 4],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in resultado_esperado:
            print(fila)

        self.assertIsNone(resultado_estudiante)
        self.assertListEqual(predio.plano, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Caso complejo donde solo cabe un cultivo determinado. Plano 6x10, código_predio = 9.
        codigo_cultivo = 9, dimensiones 4x3, plantar en (2,5).
        """
        plano = [
            [0, 0, 0, 0, 3, 3, 2, 2, 6, 6],
            [0, 0, 0, 0, 3, 3, 2, 2, 6, 6],
            [1, 1, 1, 1, 7, "X", "X", "X", 6, 6],
            [1, 1, 1, 1, 7, "X", "X", "X", 8, 8],
            [5, 4, 4, 4, 7, "X", "X", "X", 8, 8],
            [5, 4, 4, 4, 7, "X", "X", "X", 8, 8],
        ]

        predio = Predio(codigo_predio="9", alto=6, ancho=10)
        predio.plano = plano

        resultado_estudiante = predio.plantar(
            codigo_cultivo=9, coordenadas=[2, 5], alto=4, ancho=3
        )
        resultado_esperado = [
            [0, 0, 0, 0, 3, 3, 2, 2, 6, 6],
            [0, 0, 0, 0, 3, 3, 2, 2, 6, 6],
            [1, 1, 1, 1, 7, 9, 9, 9, 6, 6],
            [1, 1, 1, 1, 7, 9, 9, 9, 8, 8],
            [5, 4, 4, 4, 7, 9, 9, 9, 8, 8],
            [5, 4, 4, 4, 7, 9, 9, 9, 8, 8],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in resultado_esperado:
            print(fila)

        self.assertIsNone(resultado_estudiante)
        self.assertListEqual(predio.plano, resultado_esperado)
