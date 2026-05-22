from decorators.rutina_decorator import (
    RutinaDecorator
)


class DecoradorCalentamiento(
    RutinaDecorator
):

    def mostrar_detalles(self) -> str:

        return (
            f"{self._rutina.mostrar_detalles()}\n"
            f"Calentamiento recomendado: "
            f"10 minutos de movilidad articular y cardio suave."
        )