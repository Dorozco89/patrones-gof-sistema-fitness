from abc import ABC, abstractmethod


class EstrategiaRecomendacion(ABC):

    @abstractmethod
    def generar_recomendacion(self) -> str:
        pass