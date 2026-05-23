import unittest

from facade.sistema_fitness_facade import (
    SistemaFitnessFacade
)


class TestFacade(unittest.TestCase):

    def test_creacion_rutina_perdida_peso(
        self
    ) -> None:

        facade = (
            SistemaFitnessFacade()
        )

        resultado = (
            facade
            .crear_rutina_perdida_peso()
        )

        self.assertIn(
            "Rutina Quema Grasa",
            resultado
        )

        self.assertIn(
            "Pérdida de peso",
            resultado
        )

        self.assertIn(
            "Recomendación",
            resultado
        )

    def test_creacion_rutina_ganancia_muscular(
        self
    ) -> None:

        facade = (
            SistemaFitnessFacade()
        )

        resultado = (
            facade
            .crear_rutina_ganancia_muscular()
        )

        self.assertIn(
            "Rutina Hipertrofia",
            resultado
        )

        self.assertIn(
            "Ganancia muscular",
            resultado
        )

        self.assertIn(
            "Entrenamiento",
            resultado
        )


if __name__ == "__main__":
    unittest.main()