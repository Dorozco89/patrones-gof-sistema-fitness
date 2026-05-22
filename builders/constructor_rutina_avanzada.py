from builders.rutina_builder import RutinaBuilder
from models.ejercicio import Ejercicio
from models.rutina_fitness import RutinaFitness


class ConstructorRutinaAvanzada(RutinaBuilder):

    def __init__(self) -> None:
        self._rutina = None

    def crear_rutina(
        self,
        nombre: str,
        objetivo: str,
        nivel_dificultad: str,
        duracion: int
    ) -> None:

        self._rutina = RutinaFitness(
            nombre,
            objetivo,
            nivel_dificultad,
            duracion
        )

    def agregar_ejercicio(
        self,
        ejercicio: Ejercicio
    ) -> None:

        self._rutina.agregar_ejercicio(
            ejercicio
        )

    def obtener_rutina(self) -> RutinaFitness:
        return self._rutina