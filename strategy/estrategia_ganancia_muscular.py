from strategy.estrategia_recomendacion import (
    EstrategiaRecomendacion
)


class EstrategiaGananciaMuscular(
    EstrategiaRecomendacion
):

    def generar_recomendacion(self) -> str:
        return (
            "Se recomienda realizar "
            "entrenamientos de fuerza "
            "y mantener superávit calórico."
        )