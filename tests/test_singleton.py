import unittest

from singleton.configuracion_sistema import (
    ConfiguracionSistema
)


class TestSingleton(unittest.TestCase):

    def test_instancia_unica(
        self
    ) -> None:

        configuracion_1 = (
            ConfiguracionSistema()
        )

        configuracion_2 = (
            ConfiguracionSistema()
        )

        self.assertIs(
            configuracion_1,
            configuracion_2
        )

    def test_persistencia_configuracion(
        self
    ) -> None:

        configuracion_1 = (
            ConfiguracionSistema()
        )

        configuracion_1.modo_pruebas = True

        configuracion_2 = (
            ConfiguracionSistema()
        )

        self.assertTrue(
            configuracion_2.modo_pruebas
        )


if __name__ == "__main__":
    unittest.main()