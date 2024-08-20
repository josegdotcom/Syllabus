import unittest
from dccultivo import Predio, DCCultivo
from tests_publicos.timeout_function import timeout

N_SECOND = 10


class TestDetectarPlagas(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Caso simple. Un predio, una plaga. Se elimina una plaga.
        plano_4 3x4, código_predio = 4
        lista_plagas = [["4", [2,3]]]
        """
        plano_4 = [
            ["X", 3, 3, "X"],
            [7, "X", 4, 4],
            ["X", "X", 4, 4],
        ]
        predio_4 = Predio(codigo_predio="4", alto=3, ancho=4)
        predio_4.plano = plano_4

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_4]

        resultado_estudiante = dccultivo.detectar_plagas(lista_plagas=[["4", [2, 3]]])
        resultado_esperado = [["4", 4]]

        plano_4_esperado = [
            ["X", 3, 3, "X"],
            [7, "X", "X", "X"],
            ["X", "X", "X", "X"],
        ]
        predio_4_esperado = Predio(codigo_predio="4", alto=3, ancho=4)
        predio_4_esperado.plano = plano_4_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_4_esperado]

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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
        Caso de eliminación efectiva 2 plagas en diferentes predios.
        plano_A4 5x5, código_predio = A4
        plano_B2 2x2, código_predio = B2
        plano_C1 6x7, código_predio = C1
        lista_plagas = [["A4", [4,4]], ["B2", [0,0]], ["C1", [3,6]]]
        """
        plano_A4 = [
            ["X", "X", 2, 2, 1],
            ["X", "X", 4, 4, 1],
            [7, 7, "X", 0, 0],
            [7, 7, "X", 5, 5],
            [8, 8, 8, 8, 8],
        ]
        predio_A4 = Predio(codigo_predio="A4", alto=5, ancho=5)
        predio_A4.plano = plano_A4

        plano_B2 = [
            [1, "X"],
            ["X", 2],
        ]
        predio_B2 = Predio(codigo_predio="B2", alto=2, ancho=2)
        predio_B2.plano = plano_B2

        plano_C1 = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 5, "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            [9, "X", "X", "X", "X", "X", "X"],
            [9, "X", "X", "X", "X", "X", "X"],
        ]
        predio_C1 = Predio(codigo_predio="C1", alto=6, ancho=7)
        predio_C1.plano = plano_C1

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_A4, predio_B2, predio_C1]

        resultado_estudiante = dccultivo.detectar_plagas(
            lista_plagas=[["A4", [4, 4]], ["B2", [0, 0]], ["C1", [3, 6]]]
        )
        resultado_esperado = [["B2", 1], ["A4", 5]]

        plano_A4_esperado = [
            ["X", "X", 2, 2, 1],
            ["X", "X", 4, 4, 1],
            [7, 7, "X", 0, 0],
            [7, 7, "X", 5, 5],
            ["X", "X", "X", "X", "X"],
        ]
        predio_A4_esperado = Predio(codigo_predio="A4", alto=5, ancho=5)
        predio_A4_esperado.plano = plano_A4_esperado

        plano_B2_esperado = [
            ["X", "X"],
            ["X", 2],
        ]
        predio_B2_esperado = Predio(codigo_predio="B2", alto=2, ancho=2)
        predio_B2_esperado.plano = plano_B2_esperado

        plano_C1_esperado = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", 5, "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            [9, "X", "X", "X", "X", "X", "X"],
            [9, "X", "X", "X", "X", "X", "X"],
        ]
        predio_C1_esperado = Predio(codigo_predio="C1", alto=6, ancho=7)
        predio_C1_esperado.plano = plano_C1_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_A4_esperado,
            predio_B2_esperado,
            predio_C1_esperado,
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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
        Caso eliminación muchas plagas en un mismo predio.
        plano_0 4x7, código_predio = 0
        plano_Z 10x10, código_predio = Z
        lista_plagas = [["0", [1,2]], ["Z", [3,9]], ["0", [3, 5], ["Z", [7, 8]], ["Z", [0, 0]]]
        """
        plano_0 = [
            ["X", "X", 2, "X", "X", "X", "X"],
            [1, "X", 5, 5, "X", "X", 0],
            [1, "X", 5, 5, 9, 9, 9],
            ["X", "X", 5, 5, 9, 9, 9],
        ]
        predio_0 = Predio(codigo_predio="0", alto=4, ancho=7)
        predio_0.plano = plano_0

        plano_Z = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        predio_Z = Predio(codigo_predio="Z", alto=10, ancho=10)
        predio_Z.plano = plano_Z

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_0, predio_Z]

        resultado_estudiante = dccultivo.detectar_plagas(
            lista_plagas=[
                ["0", [1, 2]],
                ["Z", [3, 9]],
                ["0", [3, 5]],
                ["Z", [7, 8]],
                ["Z", [0, 0]],
            ]
        )
        resultado_esperado = [["0", 12], ["Z", 100]]

        plano_0_esperado = [
            ["X", "X", 2, "X", "X", "X", "X"],
            [1, "X", "X", "X", "X", "X", 0],
            [1, "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_0_esperado = Predio(codigo_predio="0", alto=4, ancho=7)
        predio_0_esperado.plano = plano_0_esperado

        plano_Z_esperado = [
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ]
        predio_Z_esperado = Predio(codigo_predio="Z", alto=10, ancho=10)
        predio_Z_esperado.plano = plano_Z_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [predio_0_esperado, predio_Z_esperado]

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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
        Caso de empate en eliminación de plagas en diferentes predios.
        plano_V 3x3, código_predio = V
        plano_K 3x3, código_predio = K
        plano_A 10x1, código_predio = A
        lista_plagas = [["V", [1, 1]], ["K", [1, 2]], ["A", [0, 0], "V", [2, 1]]]
        """
        plano_V = [
            [1, 1, 1],
            ["X", 8, "X"],
            ["X", 3, 3],
        ]
        predio_V = Predio(codigo_predio="V", alto=3, ancho=3)
        predio_V.plano = plano_V

        plano_K = [
            ["X", 0, 7],
            ["X", 4, 7],
            ["X", 2, 7],
        ]
        predio_K = Predio(codigo_predio="K", alto=3, ancho=3)
        predio_K.plano = plano_K

        plano_A = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
        predio_A = Predio(codigo_predio="A", alto=10, ancho=1)
        predio_A.plano = plano_A

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_V, predio_K, predio_A]

        resultado_estudiante = dccultivo.detectar_plagas(
            lista_plagas=[["V", [1, 1]], ["K", [1, 2]], ["A", [0, 0]], ["V", [2, 1]]]
        )
        resultado_esperado = [["A", 1], ["K", 3], ["V", 3]]

        plano_V_esperado = [
            [1, 1, 1],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ]
        predio_V_esperado = Predio(codigo_predio="V", alto=3, ancho=3)
        predio_V_esperado.plano = plano_V_esperado

        plano_K_esperado = [
            ["X", 0, "X"],
            ["X", 4, "X"],
            ["X", 2, "X"],
        ]
        predio_K_esperado = Predio(codigo_predio="K", alto=3, ancho=3)
        predio_K_esperado.plano = plano_K_esperado

        plano_A_esperado = [["X"], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
        predio_A_esperado = Predio(codigo_predio="A", alto=10, ancho=1)
        predio_A_esperado.plano = plano_A_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_V_esperado,
            predio_K_esperado,
            predio_A_esperado,
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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
        Caso múltiples predios, múltiples plagas.
        plano_A 2x1, código_predio = A
        plano_D 2x1, código_predio = D
        plano_B 2x1, código_predio = B
        plano_C 2x1, código_predio = C
        lista_plagas = [["A", [0, 0]], ["D", [1, 0]], ["B", [1, 0]], ["C", [0, 0]], ["A", [1, 0]]]
        """
        plano_A = [[0], [1]]
        predio_A = Predio(codigo_predio="A", alto=2, ancho=1)
        predio_A.plano = plano_A

        plano_D = [[8], [1]]
        predio_D = Predio(codigo_predio="D", alto=2, ancho=1)
        predio_D.plano = plano_D

        plano_B = [["X"], [3]]
        predio_B = Predio(codigo_predio="B", alto=2, ancho=1)
        predio_B.plano = plano_B

        plano_C = [[2], ["X"]]
        predio_C = Predio(codigo_predio="C", alto=2, ancho=1)
        predio_C.plano = plano_C

        dccultivo = DCCultivo()
        dccultivo.predios = [predio_A, predio_D, predio_B, predio_C]

        resultado_estudiante = dccultivo.detectar_plagas(
            lista_plagas=[
                ["A", [0, 0]],
                ["D", [1, 0]],
                ["B", [1, 0]],
                ["C", [0, 0]],
                ["A", [1, 0]],
            ]
        )
        resultado_esperado = [["B", 1], ["C", 1], ["D", 1], ["A", 2]]

        plano_A_esperado = [["X"], ["X"]]
        predio_A_esperado = Predio(codigo_predio="A", alto=2, ancho=1)
        predio_A_esperado.plano = plano_A_esperado

        plano_D_esperado = [[8], ["X"]]
        predio_D_esperado = Predio(codigo_predio="D", alto=2, ancho=1)
        predio_D_esperado.plano = plano_D_esperado

        plano_B_esperado = [["X"], ["X"]]
        predio_B_esperado = Predio(codigo_predio="B", alto=2, ancho=1)
        predio_B_esperado.plano = plano_B_esperado

        plano_C_esperado = [["X"], ["X"]]
        predio_C_esperado = Predio(codigo_predio="C", alto=2, ancho=1)
        predio_C_esperado.plano = plano_C_esperado

        dccultivo_esperado = DCCultivo()
        dccultivo_esperado.predios = [
            predio_A_esperado,
            predio_D_esperado,
            predio_B_esperado,
            predio_C_esperado,
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

        self.assertTrue(
            isinstance(resultado_estudiante, list)
            and all(isinstance(item, list) for item in resultado_estudiante)
        )
        self.assertListEqual(resultado_estudiante, resultado_esperado)
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
