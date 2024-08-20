import unittest
from dccultivo import Predio
from tests_publicos.timeout_function import timeout

N_SECOND = 10


class TestEliminarCultivo(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Caso ejemplo enunciado, solo un cultivo en el predio. Todo el predio queda con "X".
        Plano 5x7, código_predio = 1.
        código_cultivo = 3.
        """

        plano = [
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio = Predio(codigo_predio="1", alto=5, ancho=7)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=3)
        resultado_esperado = 9

        predio_esperado = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Caso cultivo en una esquina.
        Plano 2x9, código_predio = 34.
        código_cultivo = 0.
        """

        plano = [
            ["X", "X", "X", 3, "X", "X", "X", "X", "X"],
            ["X", 1, "X", 3, "X", "X", "X", "X", 0],
        ]
        predio = Predio(codigo_predio="34", alto=2, ancho=9)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=0)
        resultado_esperado = 1

        predio_esperado = [
            ["X", "X", "X", 3, "X", "X", "X", "X", "X"],
            ["X", 1, "X", 3, "X", "X", "X", "X", "X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Caso múltiples cultivos complejo.
        Plano 10x10, código_predio = 64.
        código_cultivo = 9.
        """

        plano = [
            [2, 2, "X", "X", "X", "X", 3, 3, 3, 3],
            [2, 2, "X", "X", "X", "X", 3, 3, 3, 3],
            [1, 1, 1, 1, 1, 1, 3, 3, 3, 3],
            ["X", "X", "X", "X", "X", "X", 3, 3, 3, 3],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", 5, 5, 5, "X", "X", "X", "X", "X"],
            ["X", "X", 5, 5, 5, 9, 9, "X", "X", "X"],
            ["X", "X", "X", "X", "X", 9, 9, "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio = Predio(codigo_predio="64", alto=10, ancho=10)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=9)
        resultado_esperado = 4

        predio_esperado = [
            [2, 2, "X", "X", "X", "X", 3, 3, 3, 3],
            [2, 2, "X", "X", "X", "X", 3, 3, 3, 3],
            [1, 1, 1, 1, 1, 1, 3, 3, 3, 3],
            ["X", "X", "X", "X", "X", "X", 3, 3, 3, 3],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", 5, 5, 5, "X", "X", "X", "X", "X"],
            ["X", "X", 5, 5, 5, "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Caso de un cultivo en todo el predio. Predio final vacío.
        Plano 6x6, código_predio = 97.
        codigo_cultivo = 7.
        """

        plano = [
            [7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7],
        ]
        predio = Predio(codigo_predio="97", alto=6, ancho=6)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=7)
        resultado_esperado = 36

        predio_esperado = [
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Caso de cultivo en plano con solo una columna.
        Plano 9x1, código_predio = 42.
        codigo_cultivo = 4.
        """

        plano = [
            ["X"],
            ["X"],
            [2],
            [2],
            [6],
            [7],
            [4],
            [4],
            [8],
        ]
        predio = Predio(codigo_predio="42", alto=9, ancho=1)
        predio.plano = plano

        resultado_estudiante = predio.eliminar_cultivo(codigo_cultivo=4)
        resultado_esperado = 2

        predio_esperado = [
            ["X"],
            ["X"],
            [2],
            [2],
            [6],
            [7],
            ["X"],
            ["X"],
            [8],
        ]

        print("Predio.plano")
        for fila in predio.plano:
            print(fila)
        print("Predio esperado")
        for fila in predio_esperado:
            print(fila)

        self.assertIsInstance(resultado_estudiante, int)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(predio.plano, predio_esperado)
