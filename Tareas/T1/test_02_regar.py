import unittest
from dccultivo import Predio
from tests_publicos.timeout_function import timeout

N_SECOND = 10


class TestRegar(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_ejemplo_enunciado_5x5(self):
        """
        Se crea un plano de riego 5x5, se riega al centro con área 1 y
        se comprueba que se retorne lo indicado
        """
        predio = Predio(codigo_predio="P1", alto=5, ancho=5)
        predio.plano_riego = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        resultado_estudiante = predio.regar(coordenadas=[2, 2], area=1)

        resultado_esperado = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertIsNone(resultado_estudiante)
        self.assertListEqual(predio.plano_riego, resultado_esperado)

    @timeout(N_SECOND)
    def test_01_ejemplo_enunciado_5x5_dos_riegos(self):
        """
        Se crea una plano de riego 5x5, se riega en (2,4) con área 2 y
        se comprueba que se retorne lo indicado
        """
        predio = Predio(codigo_predio="P2", alto=5, ancho=5)
        predio.plano_riego = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        predio.regar(coordenadas=[2, 2], area=1)
        resultado_estudiante_final = predio.regar(coordenadas=[2, 4], area=2)

        resultado_esperado = [
            [0, 0, 0, 1, 1],
            [0, 0, 2, 1, 1],
            [0, 1, 2, 2, 1],
            [0, 0, 2, 1, 1],
            [0, 0, 0, 1, 1],
        ]
        self.assertIsNone(resultado_estudiante_final)
        self.assertListEqual(predio.plano_riego, resultado_esperado)

    @timeout(N_SECOND)
    def test_02_varios_riegos_sucesivos(self):
        """
        Sea crea un plano de riego 6x8, se prueban riegos sucesivos en distintos lugares
        con distintas áreas  y se comprueba que se retorne lo indicado
        """
        predio = Predio(codigo_predio="P3", alto=6, ancho=8)
        predio.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        predio.regar(coordenadas=[1, 5], area=2)
        predio.regar(coordenadas=[4, 4], area=3)
        predio.regar(coordenadas=[3, 3], area=1)
        resultado_estudiante_final = predio.regar(coordenadas=[0, 0], area=2)

        resultado_esperado = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 1],
            [1, 2, 1, 3, 2, 2, 2, 2],
            [0, 1, 2, 2, 3, 2, 2, 1],
            [0, 1, 1, 2, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.assertIsNone(resultado_estudiante_final)
        self.assertListEqual(predio.plano_riego, resultado_esperado)

    @timeout(N_SECOND)
    def test03_varios_riegos_sucesivos_2(self):
        """
        Sea crea un plano de riego 12x14, se prueban riegos sucesivos en distintos lugares
        con distintas áreas y se comprueba que se retorne lo indicado
        """
        predio = Predio(codigo_predio="P3", alto=12, ancho=14)
        predio.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        predio.regar(coordenadas=[7, 3], area=2)
        predio.regar(coordenadas=[3, 2], area=1)
        predio.regar(coordenadas=[6, 5], area=3)
        predio.regar(coordenadas=[9, 7], area=2)
        predio.regar(coordenadas=[0, 13], area=4)
        resultado_estudiante_final = predio.regar(coordenadas=[6, 6], area=3)

        resultado_esperado = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
            [0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1],
            [0, 0, 2, 3, 3, 2, 2, 2, 2, 1, 0, 0, 0, 0],
            [0, 1, 2, 3, 3, 3, 2, 2, 2, 1, 0, 0, 0, 0],
            [0, 1, 2, 3, 3, 3, 3, 3, 3, 1, 0, 0, 0, 0],
            [0, 1, 2, 3, 3, 4, 3, 3, 3, 2, 0, 0, 0, 0],
            [0, 0, 1, 2, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        ]

        self.assertIsNone(resultado_estudiante_final)
        self.assertListEqual(predio.plano_riego, resultado_esperado)
