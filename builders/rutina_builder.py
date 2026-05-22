from abc import ABC, abstractmethod

from models.ejercicio import Ejercicio
from models.rutina_fitness import RutinaFitness


class RutinaBuilder(ABC):

    @abstractmethod
    def crear_rutina(
        self,
        nombre: str,
        objetivo: str,
        nivel_dificultad: str,
        duracion: int
    ) -> None:
        pass

    @abstractmethod
    def agregar_ejercicio(
        self,
        ejercicio: Ejercicio
    ) -> None:
        pass

    @abstractmethod
    def obtener_rutina(self) -> RutinaFitness:
        pass
         
         