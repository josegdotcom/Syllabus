import unittest
from dccultivo import Predio, DCCultivo
from tests_publicos.timeout_function import timeout

N_SECOND = 10


class TestBuscarYPlantarFacil(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Ejemplo básico del enunciado parte 1. Solo un predio en self.predios.
        plano_1 5x7, código_predio = 1.
        codigo_cultivo = 3, dimensiones 3x3.
        """
        plano_1 = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_1 = Predio(codigo_predio="1", alto=5, ancho=7)
        predio_1.plano = plano_1

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_1]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=3, alto=3, ancho=3
        )
        resultado_esperado = True

        plano_1_esperado = [
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_1_esperado = Predio(codigo_predio="1", alto=5, ancho=7)
        predio_1_esperado.plano = plano_1_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_1_esperado]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertIsInstance(resultado_estudiante, bool)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Ejemplo básico del enunciado parte 2. Dos predios en self.predios.
        plano_6 5x7, código_predio = 6.
        plano_4 7x8, código_predio = 4.
        codigo_cultivo = 1, dimensiones 2x2.
        """
        plano_6 = [
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_6 = Predio(codigo_predio="6", alto=5, ancho=7)
        predio_6.plano = plano_6

        plano_4 = [
            ["X", "X", 4, 4, "X", "X", 7, 7],
            ["X", "X", 4, 4, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 5, 5, 5, "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_4 = Predio(codigo_predio="4", alto=7, ancho=8)
        predio_4.plano = plano_4

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_6, predio_4]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=1, alto=2, ancho=2
        )
        resultado_esperado = True

        plano_6_esperado = [
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_6_esperado = Predio(codigo_predio="6", alto=5, ancho=7)
        predio_6_esperado.plano = plano_6_esperado

        plano_4_esperado = [
            ["X", "X", 4, 4, "X", "X", 7, 7],
            ["X", "X", 4, 4, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 5, 5, 5, "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_4_esperado = Predio(codigo_predio="4", alto=7, ancho=8)
        predio_4_esperado.plano = plano_4_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_6_esperado, predio_4_esperado]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Ejemplo básico del enunciado parte 3. Dos predios en self.predios.
        plano_2 5x7, código_predio = 2.
        plano_3 4x8, código_predio = 3.
        codigo_cultivo = 7, dimensiones 2x5.
        """
        plano_2 = [
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_2 = Predio(codigo_predio="2", alto=5, ancho=7)
        predio_2.plano = plano_2

        plano_3 = [
            ["X", "X", 5, 5, 5, "X", 7, 7],
            ["X", "X", 5, 5, 5, "X", "X", "X"],
            [3, 3, "X", "X", "X", "X", "X", 1],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_3 = Predio(codigo_predio="3", alto=4, ancho=8)
        predio_3.plano = plano_3

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_2, predio_3]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=7, alto=2, ancho=5
        )
        resultado_esperado = True

        plano_2_esperado = [
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, 1, 1, "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [7, 7, 7, 7, 7, "X", "X"],
            [7, 7, 7, 7, 7, "X", "X"],
        ]
        predio_2_esperado = Predio(codigo_predio="2", alto=5, ancho=7)
        predio_2_esperado.plano = plano_2_esperado

        plano_3_esperado = [
            ["X", "X", 5, 5, 5, "X", 7, 7],
            ["X", "X", 5, 5, 5, "X", "X", "X"],
            [3, 3, "X", "X", "X", "X", "X", 1],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_3_esperado = Predio(codigo_predio="3", alto=4, ancho=8)
        predio_3_esperado.plano = plano_3_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_2_esperado, predio_3_esperado]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertIsInstance(resultado_estudiante, bool)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Caso complejo con cultivos ya agregados. Tres predios en self.predios.
        plano_56 6x7, código_predio = 56.
        plano_42 2x1, código_predio = 42.
        plano_13 4x4, código_predio = 13.
        codigo_cultivo = 8, dimensiones 4x2.
        """
        plano_56 = [
            ["X", "X", "X", "X", "X", "X", "X"],
            [2, 2, 2, 2, 2, 4, 4],
            ["X", "X", "X", "X", "X", 4, 4],
            ["X", "X", "X", "X", "X", 4, 4],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", 1],
        ]
        predio_56 = Predio(codigo_predio="56", alto=6, ancho=7)
        predio_56.plano = plano_56

        plano_42 = [
            [7],
            [0],
        ]
        predio_42 = Predio(codigo_predio="42", alto=2, ancho=1)
        predio_42.plano = plano_42

        plano_13 = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
        ]
        predio_13 = Predio(codigo_predio="13", alto=4, ancho=4)
        predio_13.plano = plano_13

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_56, predio_42, predio_13]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=8, alto=4, ancho=2
        )
        resultado_esperado = True

        plano_56_esperado = [
            ["X", "X", "X", "X", "X", "X", "X"],
            [2, 2, 2, 2, 2, 4, 4],
            [8, 8, "X", "X", "X", 4, 4],
            [8, 8, "X", "X", "X", 4, 4],
            [8, 8, "X", "X", "X", "X", "X"],
            [8, 8, "X", "X", "X", "X", 1],
        ]
        predio_56_esperado = Predio(codigo_predio="56", alto=6, ancho=7)
        predio_56_esperado.plano = plano_56_esperado

        plano_42_esperado = [
            [7],
            [0],
        ]
        predio_42_esperado = Predio(codigo_predio="42", alto=2, ancho=1)
        predio_42_esperado.plano = plano_42_esperado

        plano_13_esperado = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
        ]
        predio_13_esperado = Predio(codigo_predio="13", alto=4, ancho=4)
        predio_13_esperado.plano = plano_13_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_56_esperado,
            predio_42_esperado,
            predio_13_esperado,
        ]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertIsInstance(resultado_estudiante, bool)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Caso de esquina. Solo un predio en self.predios.
        plano_9 5x5, código_predio = 9.
        codigo_cultivo = 0, dimensiones 2x3.
        """
        plano_9 = [
            [1, 1, 7, "X", "X"],
            [1, 1, 6, 6, "X"],
            ["X", "X", "X", 3, 3],
            ["X", 4, "X", "X", "X"],
            [2, "X", "X", "X", "X"],
        ]
        predio_9 = Predio(codigo_predio="9", alto=5, ancho=5)
        predio_9.plano = plano_9

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_9]

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=0, alto=2, ancho=3
        )
        resultado_esperado = True

        plano_9_esperado = plano_9 = [
            [1, 1, 7, "X", "X"],
            [1, 1, 6, 6, "X"],
            ["X", "X", "X", 3, 3],
            ["X", 4, 0, 0, 0],
            [2, "X", 0, 0, 0],
        ]
        predio_9_esperado = Predio(codigo_predio="9", alto=5, ancho=5)
        predio_9_esperado.plano = plano_9_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_9_esperado]

        print("DCCultivo.predios")
        for predio in dccultivo.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)
        print("DCCultivo.predios esperados")
        for predio in dccultivo_esperado.predios:
            print(f"Predio {predio.codigo_predio}")
            for fila in predio.plano:
                print(fila)

        self.assertIsInstance(resultado_estudiante, bool)
        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertEqual(len(dccultivo.predios), len(dccultivo_esperado.predios))

        for predio_estudiante, predio_esperado in zip(
            dccultivo.predios, dccultivo_esperado.predios
        ):
            self.assertEqual(
                predio_estudiante.codigo_predio, predio_esperado.codigo_predio
            )
            self.assertEqual(predio_estudiante.alto, predio_esperado.alto)
            self.assertEqual(predio_estudiante.ancho, predio_esperado.ancho)
            self.assertIsInstance(predio_estudiante, Predio)
            self.assertListEqual(predio_estudiante.plano, predio_esperado.plano)
