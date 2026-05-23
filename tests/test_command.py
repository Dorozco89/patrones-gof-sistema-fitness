import unittest

from command.actualizar_rutina_command import (
    ActualizarRutinaCommand
)
from command.crear_rutina_command import (
    CrearRutinaCommand
)
from command.eliminar_rutina_command import (
    EliminarRutinaCommand
)
from command.invocador_comandos import (
    InvocadorComandos
)
from facade.sistema_fitness_facade import (
    SistemaFitnessFacade
)


class TestCommand(unittest.TestCase):

    def test_crear_rutina_command(
        self
    ) -> None:

        facade = (
            SistemaFitnessFacade()
        )

        comando = (
            CrearRutinaCommand(
                facade
            )
        )

        resultado = (
            comando.ejecutar()
        )

        self.assertIn(
            "Rutina Quema Grasa",
            resultado
        )

        self.assertIn(
            "Pérdida de peso",
            resultado
        )

    def test_invocador_comandos(
        self
    ) -> None:

        facade = (
            SistemaFitnessFacade()
        )

        comando_crear = (
            CrearRutinaCommand(
                facade
            )
        )

        comando_actualizar = (
            ActualizarRutinaCommand()
        )

        comando_eliminar = (
            EliminarRutinaCommand()
        )

        invocador = (
            InvocadorComandos()
        )

        invocador.agregar_comando(
            comando_crear
        )

        invocador.agregar_comando(
            comando_actualizar
        )

        invocador.agregar_comando(
            comando_eliminar
        )

        resultados = (
            invocador
            .ejecutar_comandos()
        )

        self.assertEqual(
            len(resultados),
            3
        )


if __name__ == "__main__":
    unittest.main()