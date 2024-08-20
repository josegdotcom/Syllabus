import unittest
from dccultivo import Predio
from tests_publicos.timeout_function import timeout

N_SECOND = 10


class TestCrearPlano(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_plano_3x3(self):
        """
        Plano 3x3, se verifica que se haya creado el plano normal, el de riego y
        que se retorne lo esperado
        """

        predio = Predio(codigo_predio="P0", alto=3, ancho=3)

        resultado_estudiante1 = predio.crear_plano(tipo="normal")
        plano_normal_esperado = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]

        resultado_estudiante2 = predio.crear_plano(tipo="riego")
        plano_riego_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.assertIsNone(resultado_estudiante1)
        self.assertIsNone(resultado_estudiante2)
        self.assertListEqual(predio.plano, plano_normal_esperado)
        self.assertListEqual(predio.plano_riego, plano_riego_esperado)

    @timeout(N_SECOND)
    def test_01_plano_5x6(self):
        """
        Plano 5x6, se verifica que se haya creado el plano normal y el de riego
        """
        predio = Predio(codigo_predio="P1", alto=5, ancho=6)

        resultado_estudiante1 = predio.crear_plano(tipo="normal")
        plano_normal_esperado = [
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
        ]

        resultado_estudiante2 = predio.crear_plano(tipo="riego")
        plano_riego_esperado = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        self.assertIsNone(resultado_estudiante1)
        self.assertIsNone(resultado_estudiante2)
        self.assertListEqual(predio.plano, plano_normal_esperado)
        self.assertListEqual(predio.plano_riego, plano_riego_esperado)

    @timeout(N_SECOND)
    def test_02_plano_10x5(self):
        """
        Plano 10x5, se verifica que se haya creado el plano normal y el de riego
        """
        predio = Predio(codigo_predio="P2", alto=10, ancho=5)

        resultado_estudiante1 = predio.crear_plano(tipo="normal")
        plano_normal_esperado = [
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
        ]

        resultado_estudiante2 = predio.crear_plano(tipo="riego")
        plano_riego_esperado = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.assertIsNone(resultado_estudiante1)
        self.assertIsNone(resultado_estudiante2)
        self.assertListEqual(predio.plano, plano_normal_esperado)
        self.assertListEqual(predio.plano_riego, plano_riego_esperado)

    @timeout(N_SECOND)
    def test_03_plano_15x13(self):
        """
        Plano 15x13, se verifica que se haya creado el plano normal y el de riego
        """
        predio = Predio(codigo_predio="P3", alto=13, ancho=15)

        resultado_estudiante1 = predio.crear_plano(tipo="normal")
        plano_normal_esperado = [
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ]

        resultado_estudiante2 = predio.crear_plano(tipo="riego")
        plano_riego_esperado = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        self.assertIsNone(resultado_estudiante1)
        self.assertIsNone(resultado_estudiante2)
        self.assertListEqual(predio.plano, plano_normal_esperado)
        self.assertListEqual(predio.plano_riego, plano_riego_esperado)
