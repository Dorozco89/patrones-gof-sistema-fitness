from models.rutina_fitness import RutinaFitness


class RutinaDecorator:

    def __init__(
        self,
        rutina: RutinaFitness
    ) -> None:

        self._rutina = rutina

    def mostrar_detalles(self) -> str:
        return self._rutina.mostrar_detalles()