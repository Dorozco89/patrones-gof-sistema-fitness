from decorators.rutina_decorator import (
    RutinaDecorator
)


class DecoradorNutricion(
    RutinaDecorator
):

    def mostrar_detalles(self) -> str:

        return (
            f"{self._rutina.mostrar_detalles()}\n"
            f"Recomendación nutricional: "
            f"Consumir proteínas y mantenerse hidratado."
        )