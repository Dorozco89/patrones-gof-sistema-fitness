from builders.constructor_rutina_avanzada import (
    ConstructorRutinaAvanzada
)
from builders.director_rutina import (
    DirectorRutina
)
from decorators.decorador_calentamiento import (
    DecoradorCalentamiento
)
from decorators.decorador_nutricion import (
    DecoradorNutricion
)
from factory.fabrica_entrenamientos import (
    FabricaEntrenamientos
)
from singleton.configuracion_sistema import (
    ConfiguracionSistema
)
from strategy.estrategia_ganancia_muscular import (
    EstrategiaGananciaMuscular
)
from strategy.estrategia_perdida_peso import (
    EstrategiaPerdidaPeso
)
from strategy.sistema_recomendador import (
    SistemaRecomendador
)


class SistemaFitnessFacade:

    def crear_rutina_perdida_peso(self):

        builder = ConstructorRutinaAvanzada()

        director = DirectorRutina(builder)

        rutina = director.construir_rutina_perdida_peso()

        rutina_decorada = (
            DecoradorNutricion(
                DecoradorCalentamiento(
                    rutina
                )
            )
        )

        entrenamiento = (
            FabricaEntrenamientos
            .crear_entrenamiento(
                "cardio"
            )
        )

        recomendador = SistemaRecomendador(
            EstrategiaPerdidaPeso()
        )

        configuracion = ConfiguracionSistema()

        return (
            f"{rutina_decorada.mostrar_detalles()}\n\n"
            f"Entrenamiento: "
            f"{entrenamiento.obtener_descripcion()}\n\n"
            f"Recomendación: "
            f"{recomendador.obtener_recomendacion()}\n\n"
            f"{configuracion.obtener_configuracion()}"
        )

    def crear_rutina_ganancia_muscular(self):

        builder = ConstructorRutinaAvanzada()

        director = DirectorRutina(builder)

        rutina = (
            director
            .construir_rutina_ganancia_muscular()
        )

        rutina_decorada = (
            DecoradorNutricion(
                DecoradorCalentamiento(
                    rutina
                )
            )
        )

        entrenamiento = (
            FabricaEntrenamientos
            .crear_entrenamiento(
                "fuerza"
            )
        )

        recomendador = SistemaRecomendador(
            EstrategiaGananciaMuscular()
        )

        configuracion = ConfiguracionSistema()

        return (
            f"{rutina_decorada.mostrar_detalles()}\n\n"
            f"Entrenamiento: "
            f"{entrenamiento.obtener_descripcion()}\n\n"
            f"Recomendación: "
            f"{recomendador.obtener_recomendacion()}\n\n"
            f"{configuracion.obtener_configuracion()}"
        )