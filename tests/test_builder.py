import unittest

from builders.constructor_rutina_avanzada import (
    ConstructorRutinaAvanzada
)
from builders.director_rutina import (
    DirectorRutina
)


class TestBuilder(unittest.TestCase):

    def test_creacion_rutina_perdida_peso(
        self
    ) -> None:

        builder = (
            ConstructorRutinaAvanzada()
        )

        director = DirectorRutina(
            builder
        )

        rutina = (
            director
            .construir_rutina_perdida_peso()
        )

        self.assertEqual(
            rutina.nombre,
            "Rutina Quema Grasa"
        )

        self.assertEqual(
            rutina.objetivo,
            "Pérdida de peso"
        )

        self.assertEqual(
            len(rutina.ejercicios),
            2
        )

    def test_creacion_rutina_ganancia_muscular(
        self
    ) -> None:

        builder = (
            ConstructorRutinaAvanzada()
        )

        director = DirectorRutina(
            builder
        )

        rutina = (
            director
            .construir_rutina_ganancia_muscular()
        )

        self.assertEqual(
            rutina.nombre,
            "Rutina Hipertrofia"
        )

        self.assertEqual(
            rutina.objetivo,
            "Ganancia muscular"
        )

        self.assertEqual(
            len(rutina.ejercicios),
            2
        )


if __name__ == "__main__":
    unittest.main()