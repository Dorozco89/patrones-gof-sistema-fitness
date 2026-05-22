from builders.rutina_builder import RutinaBuilder
from models.ejercicio import Ejercicio
from models.rutina_fitness import RutinaFitness


class DirectorRutina:

    def __init__(
        self,
        builder: RutinaBuilder
    ) -> None:

        self._builder = builder

    def construir_rutina_perdida_peso(
        self
    ) -> RutinaFitness:

        self._builder.crear_rutina(
            "Rutina Quema Grasa",
            "Pérdida de peso",
            "Intermedio",
            60
        )

        self._builder.agregar_ejercicio(
            Ejercicio(
                "Burpees",
                4,
                15,
                30
            )
        )

        self._builder.agregar_ejercicio(
            Ejercicio(
                "Jumping Jacks",
                3,
                20,
                20
            )
        )

        return self._builder.obtener_rutina()

    def construir_rutina_ganancia_muscular(
        self
    ) -> RutinaFitness:

        self._builder.crear_rutina(
            "Rutina Hipertrofia",
            "Ganancia muscular",
            "Avanzado",
            90
        )

        self._builder.agregar_ejercicio(
            Ejercicio(
                "Press banca",
                4,
                10,
                60
            )
        )

        self._builder.agregar_ejercicio(
            Ejercicio(
                "Sentadilla",
                4,
                12,
                60
            )
        )

        return self._builder.obtener_rutina()