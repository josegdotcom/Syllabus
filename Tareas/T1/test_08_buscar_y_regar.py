import unittest
from dccultivo import Predio, DCCultivo
from tests_publicos.timeout_function import timeout

N_SECOND = 10


class TestBuscarYRegar(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_predio_unitario(self):
        """
        Se comprueba que el riego se realizó correctamente con un predio 5x6
        y que se retorne lo indicado
        """
        cultivo = DCCultivo()
        p1 = Predio("P1", 5, 6)
        p1.plano_riego = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        cultivo.predios.append(p1)

        codigo = "P1"
        resultado_estudiante = cultivo.buscar_y_regar(
            codigo_predio=codigo, coordenadas=[3, 2], area=2
        )
        plano_riego_esperado = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0],
        ]

        # tomar el predio de interés
        for predio in cultivo.predios:
            if predio.codigo_predio == codigo:
                pred = predio

        # comprobar si el plano de riego cambió correctamente
        self.assertIsNone(resultado_estudiante)
        self.assertListEqual(pred.plano_riego, plano_riego_esperado)

    @timeout(N_SECOND)
    def test_01_predio_cualquiera(self):
        """
        Se comprueba que el riego se realizó correctamente con un predio cualquiera y
        que se retorne lo indicado
        """
        cultivo = DCCultivo()
        p1 = Predio("P1", 5, 6)
        p1.plano_riego = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        p2 = Predio("P2", 6, 9)
        p2.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        p3 = Predio("P3", 3, 8)
        p3.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        p4 = Predio("P4", 5, 10)
        p4.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        p5 = Predio("P5", 10, 5)
        p5.plano_riego = [
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

        cultivo.predios.append(p1)
        cultivo.predios.append(p2)
        cultivo.predios.append(p3)
        cultivo.predios.append(p4)
        cultivo.predios.append(p5)

        codigo = "P4"
        resultado_estudiante = cultivo.buscar_y_regar(
            codigo_predio=codigo, coordenadas=[4, 3], area=3
        )
        plano_riego_esperado = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        ]

        # tomar el predio de interés
        for predio in cultivo.predios:
            if predio.codigo_predio == codigo:
                pred = predio

        self.assertIsNone(resultado_estudiante)
        self.assertListEqual(pred.plano_riego, plano_riego_esperado)

    @timeout(N_SECOND)
    def test_02_riegos_en_predios_distintos(self):
        """
        Se comprueba que los riegos se realizaron correctamente al regar varios predios distintos
        y que se retorne correctamente lo indicado
        """
        cultivo = DCCultivo()
        p1 = Predio("P1", 5, 6)
        p1.plano_riego = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        p2 = Predio("P2", 6, 9)
        p2.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        p3 = Predio("P3", 3, 8)
        p3.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        p4 = Predio("P4", 5, 10)
        p4.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        p5 = Predio("P5", 10, 5)
        p5.plano_riego = [
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

        cultivo.predios.append(p1)
        cultivo.predios.append(p2)
        cultivo.predios.append(p3)
        cultivo.predios.append(p4)
        cultivo.predios.append(p5)

        # probar el método con varios predios distintos
        cultivo.buscar_y_regar(codigo_predio="P1", coordenadas=[2, 2], area=1)
        plano_riego_esperado1 = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        cultivo.buscar_y_regar(codigo_predio="P2", coordenadas=[5, 5], area=2)
        plano_riego_esperado2 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0],
        ]

        cultivo.buscar_y_regar(codigo_predio="P3", coordenadas=[1, 3], area=1)
        plano_riego_esperado3 = [
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
        ]

        cultivo.buscar_y_regar(codigo_predio="P4", coordenadas=[3, 6], area=3)
        plano_riego_esperado4 = [
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        ]

        resultado_estudiante_final = cultivo.buscar_y_regar(
            codigo_predio="P5", coordenadas=[9, 4], area=5
        )
        plano_riego_esperado5 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]

        # extraemos los predios
        pred1, pred2, pred3, pred4, pred5 = cultivo.predios

        self.assertIsNone(resultado_estudiante_final)
        self.assertListEqual(pred1.plano_riego, plano_riego_esperado1)
        self.assertListEqual(pred2.plano_riego, plano_riego_esperado2)
        self.assertListEqual(pred3.plano_riego, plano_riego_esperado3)
        self.assertListEqual(pred4.plano_riego, plano_riego_esperado4)
        self.assertListEqual(pred5.plano_riego, plano_riego_esperado5)

    @timeout(N_SECOND)
    def test_03_riesgos_en_mas_distintos_2(self):
        """
        Se comprueba que los riegos se realizaron correctamente al regar varios predios distintos,
        y que se retorne correctamente lo indicado
        """
        cultivo = DCCultivo()
        p1 = Predio("P1", 7, 5)
        p1.plano_riego = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        p2 = Predio("P2", 8, 4)
        p2.plano_riego = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

        p3 = Predio("P3", 6, 6)
        p3.plano_riego = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        p4 = Predio("P4", 12, 14)
        p4.plano_riego = [
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

        p5 = Predio("P5", 10, 10)
        p5.plano_riego = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        cultivo.predios.append(p1)
        cultivo.predios.append(p2)
        cultivo.predios.append(p3)
        cultivo.predios.append(p4)
        cultivo.predios.append(p5)

        # probar el método con varios predios distintos
        cultivo.buscar_y_regar(codigo_predio="P1", coordenadas=[6, 4], area=4)
        plano_riego_esperado1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]

        cultivo.buscar_y_regar(codigo_predio="P2", coordenadas=[0, 0], area=5)
        plano_riego_esperado2 = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

        cultivo.buscar_y_regar(codigo_predio="P3", coordenadas=[3, 2], area=8)
        plano_riego_esperado3 = [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]

        cultivo.buscar_y_regar(codigo_predio="P4", coordenadas=[10, 1], area=10)
        plano_riego_esperado4 = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        ]

        resultado_estudiante_final = cultivo.buscar_y_regar(
            codigo_predio="P5", coordenadas=[0, 9], area=9
        )
        plano_riego_esperado5 = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        # extraemos los predios
        pred1, pred2, pred3, pred4, pred5 = cultivo.predios

        # comprobar que hayan sido regados correctamente
        self.assertIsNone(resultado_estudiante_final)
        self.assertListEqual(pred1.plano_riego, plano_riego_esperado1)
        self.assertListEqual(pred2.plano_riego, plano_riego_esperado2)
        self.assertListEqual(pred3.plano_riego, plano_riego_esperado3)
        self.assertListEqual(pred4.plano_riego, plano_riego_esperado4)
        self.assertListEqual(pred5.plano_riego, plano_riego_esperado5)
