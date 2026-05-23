import unittest

from decorators.decorador_calentamiento import (
    DecoradorCalentamiento
)
from decorators.decorador_nutricion import (
    DecoradorNutricion
)
from models.rutina_fitness import (
    RutinaFitness
)


class TestDecorator(unittest.TestCase):

    def test_decorador_nutricion(
        self
    ) -> None:

        rutina = RutinaFitness(
            "Rutina Básica",
            "Salud general",
            "Principiante",
            45
        )

        rutina_decorada = (
            DecoradorNutricion(
                rutina
            )
        )

        resultado = (
            rutina_decorada
            .mostrar_detalles()
        )

        self.assertIn(
            "Recomendación nutricional",
            resultado
        )

    def test_decorador_calentamiento(
        self
    ) -> None:

        rutina = RutinaFitness(
            "Rutina Funcional",
            "Resistencia",
            "Intermedio",
            50
        )

        rutina_decorada = (
            DecoradorCalentamiento(
                rutina
            )
        )

        resultado = (
            rutina_decorada
            .mostrar_detalles()
        )

        self.assertIn(
            "Calentamiento recomendado",
            resultado
        )


if __name__ == "__main__":
    unittest.main()