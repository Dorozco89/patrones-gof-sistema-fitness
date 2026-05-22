from abc import ABC, abstractmethod


class Entrenamiento(ABC):

    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass