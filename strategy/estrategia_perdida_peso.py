from strategy.estrategia_recomendacion import (
    EstrategiaRecomendacion
)


class EstrategiaPerdidaPeso(
    EstrategiaRecomendacion
):

    def generar_recomendacion(self) -> str:
        return (
            "Se recomienda realizar "
            "ejercicios cardiovasculares "
            "y mantener déficit calórico."
        )