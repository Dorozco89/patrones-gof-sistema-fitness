import unittest

from strategy.estrategia_ganancia_muscular import (
    EstrategiaGananciaMuscular
)
from strategy.estrategia_perdida_peso import (
    EstrategiaPerdidaPeso
)
from strategy.sistema_recomendador import (
    SistemaRecomendador
)


class TestStrategy(unittest.TestCase):

    def test_estrategia_perdida_peso(
        self
    ) -> None:

        estrategia = (
            EstrategiaPerdidaPeso()
        )

        recomendador = (
            SistemaRecomendador(
                estrategia
            )
        )

        resultado = (
            recomendador
            .obtener_recomendacion()
        )

        self.assertEqual(
            resultado,
            (
                "Se recomienda realizar "
                "ejercicios cardiovasculares "
                "y mantener déficit calórico."
            )
        )

    def test_estrategia_ganancia_muscular(
        self
    ) -> None:

        estrategia = (
            EstrategiaGananciaMuscular()
        )

        recomendador = (
            SistemaRecomendador(
                estrategia
            )
        )

        resultado = (
            recomendador
            .obtener_recomendacion()
        )

        self.assertEqual(
            resultado,
            (
                "Se recomienda realizar "
                "entrenamientos de fuerza "
                "y mantener superávit calórico."
            )
        )


if __name__ == "__main__":
    unittest.main()