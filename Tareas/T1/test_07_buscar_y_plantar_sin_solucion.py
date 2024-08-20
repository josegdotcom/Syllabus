import unittest
from dccultivo import Predio, DCCultivo
from tests_publicos.timeout_function import timeout

N_SECOND = 10


class TestBuscarYPlantar(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Caso sin solución.
        Ejemplo del enunciado (fig. 3).
        Solo un predio en self.predios.
        plano_1 5x7 con código_predio = 1, incluye
            - bloque 3x3 con codigo_cultivo = 3 ya ubicado.
        codigo_cultivo = 5, dimensiones 1x10.
        """
        predio_1 = Predio("1", 5, 7)
        predio_1.plano = [
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]

        dccultivo = DCCultivo()
        dccultivo.predios.append(predio_1)

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=5, alto=1, ancho=10
        )
        resultado_esperado = False

        predio_1_esperado = Predio("1", 5, 7)
        predio_1_esperado.plano = [
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            [3, 3, 3, "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios.append(predio_1_esperado)

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
        Caso sin solución.
        Solo un predio en self.predios.
        predio_2 3x3 con código_predio = 2.
        codigo_cultivo = 2, dimensiones 4x5
        """
        predio_2 = Predio("2", 3, 3)
        predio_2.plano = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]

        dccultivo = DCCultivo()
        dccultivo.predios.append(predio_2)

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=2, alto=4, ancho=5
        )
        resultado_esperado = False

        predio_2_esperado = Predio("2", 3, 3)
        predio_2_esperado.plano = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ]

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios.append(predio_2_esperado)

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
    def test_2(self):
        """
        Caso sin solución.
        Dos predios en self.predios.
        predio_3 5x6, código_predio = 3, incluye:
            - bloque 4x4 con código_cultivo = 2 ya ubicado
        predio_4 7x3, código_predio = 4, incluye:
            - bloque 6x2 con código_cultivo = 3 ya ubicado

        codigo_cultivo = 4, dimensiones 3x2
        """
        predio_3 = Predio(codigo_predio="3", alto=5, ancho=6)
        predio_3.plano = [
            ["X", 2, 2, 2, 2, "X"],
            ["X", 2, 2, 2, 2, "X"],
            ["X", 2, 2, 2, 2, "X"],
            ["X", 2, 2, 2, 2, "X"],
            ["X", "X", "X", "X", "X", "X"],
        ]

        predio_4 = Predio(codigo_predio="4", alto=7, ancho=3)
        predio_4.plano = [
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", "X", "X"],
        ]

        dccultivo = DCCultivo()
        dccultivo.predios.append(predio_3)
        dccultivo.predios.append(predio_4)

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=4, alto=3, ancho=2
        )
        resultado_esperado = False

        predio_3_esperado = Predio(codigo_predio="3", alto=5, ancho=6)
        predio_3_esperado.plano = [
            ["X", 2, 2, 2, 2, "X"],
            ["X", 2, 2, 2, 2, "X"],
            ["X", 2, 2, 2, 2, "X"],
            ["X", 2, 2, 2, 2, "X"],
            ["X", "X", "X", "X", "X", "X"],
        ]

        predio_4_esperado = Predio(codigo_predio="4", alto=7, ancho=3)
        predio_4_esperado.plano = [
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", 3, 3],
            ["X", "X", "X"],
        ]

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios.append(predio_3_esperado)
        dccultivo_esperado.predios.append(predio_4_esperado)

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
        Caso sin solución.
        Dos predios en self.predios
        predio_5 8x8, código_predio = 5, incluye:
            - bloque 4x5 con código_cultivo = 2 ya ubicado
            - bloque 6x2 con código_cultivo = 3 ya ubicado

        predio_6 7x5, código_predio = 6, incluye
            - bloque 3x3, código_predio = 4 ya ubicado
            - bloque 4x3, código_predio = 5 ya ubicado
        codigo_cultivo = 7, dimensiones 4x3
        """

        predio_5 = Predio(codigo_predio="5", alto=8, ancho=8)
        predio_5.plano = [
            [3, 3, "X", "X", "X", "X", "X", "X"],
            [3, 3, "X", "X", "X", "X", "X", "X"],
            [3, 3, "X", "X", "X", "X", "X", "X"],
            [3, 3, 2, 2, 2, 2, 2, "X"],
            [3, 3, 2, 2, 2, 2, 2, "X"],
            [3, 3, 2, 2, 2, 2, 2, "X"],
            ["X", "X", 2, 2, 2, 2, 2, "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]

        predio_6 = Predio(codigo_predio="6", alto=7, ancho=5)
        predio_6.plano = [
            [4, 4, 4, "X", "X"],
            [4, 4, 4, "X", "X"],
            [4, 4, 4, "X", "X"],
            ["X", "X", 5, 5, 5],
            ["X", "X", 5, 5, 5],
            ["X", "X", 5, 5, 5],
            ["X", "X", 5, 5, 5],
        ]

        dccultivo = DCCultivo()
        dccultivo.predios.append(predio_5)
        dccultivo.predios.append(predio_6)

        resultado_estudiante = dccultivo.buscar_y_plantar(
            codigo_cultivo=7, alto=4, ancho=3
        )
        resultado_esperado = False

        predio_5_esperado = Predio(codigo_predio="5", alto=8, ancho=8)
        predio_5_esperado.plano = [
            [3, 3, "X", "X", "X", "X", "X", "X"],
            [3, 3, "X", "X", "X", "X", "X", "X"],
            [3, 3, "X", "X", "X", "X", "X", "X"],
            [3, 3, 2, 2, 2, 2, 2, "X"],
            [3, 3, 2, 2, 2, 2, 2, "X"],
            [3, 3, 2, 2, 2, 2, 2, "X"],
            ["X", "X", 2, 2, 2, 2, 2, "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]

        predio_6_esperado = Predio(codigo_predio="6", alto=7, ancho=5)
        predio_6_esperado.plano = [
            [4, 4, 4, "X", "X"],
            [4, 4, 4, "X", "X"],
            [4, 4, 4, "X", "X"],
            ["X", "X", 5, 5, 5],
            ["X", "X", 5, 5, 5],
            ["X", "X", 5, 5, 5],
            ["X", "X", 5, 5, 5],
        ]

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios.append(predio_5_esperado)
        dccultivo_esperado.predios.append(predio_6_esperado)

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
