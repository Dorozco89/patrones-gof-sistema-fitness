import unittest

from factory.entrenamiento_cardio import (
    EntrenamientoCardio
)
from factory.entrenamiento_fuerza import (
    EntrenamientoFuerza
)
from factory.fabrica_entrenamientos import (
    FabricaEntrenamientos
)


class TestFactory(unittest.TestCase):

    def test_creacion_entrenamiento_cardio(
        self
    ) -> None:

        entrenamiento = (
            FabricaEntrenamientos
            .crear_entrenamiento(
                "cardio"
            )
        )

        self.assertIsInstance(
            entrenamiento,
            EntrenamientoCardio
        )

        self.assertEqual(
            entrenamiento.obtener_descripcion(),
            (
                "Entrenamiento enfocado en "
                "resistencia cardiovascular "
                "y quema de grasa."
            )
        )

    def test_creacion_entrenamiento_fuerza(
        self
    ) -> None:

        entrenamiento = (
            FabricaEntrenamientos
            .crear_entrenamiento(
                "fuerza"
            )
        )

        self.assertIsInstance(
            entrenamiento,
            EntrenamientoFuerza
        )

        self.assertEqual(
            entrenamiento.obtener_descripcion(),
            (
                "Entrenamiento enfocado en "
                "ganancia muscular "
                "y desarrollo de fuerza."
            )
        )


if __name__ == "__main__":
    unittest.main()