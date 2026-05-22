from strategy.estrategia_recomendacion import (
    EstrategiaRecomendacion
)


class SistemaRecomendador:

    def __init__(
        self,
        estrategia: EstrategiaRecomendacion
    ) -> None:

        self._estrategia = estrategia

    def cambiar_estrategia(
        self,
        estrategia: EstrategiaRecomendacion
    ) -> None:

        self._estrategia = estrategia

    def obtener_recomendacion(self) -> str:
        return self._estrategia.generar_recomendacion()