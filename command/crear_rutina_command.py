from command.command import Command
from facade.sistema_fitness_facade import (
    SistemaFitnessFacade
)


class CrearRutinaCommand(Command):

    def __init__(
        self,
        facade: SistemaFitnessFacade
    ) -> None:

        self._facade = facade

    def ejecutar(self) -> str:

        return (
            self._facade
            .crear_rutina_perdida_peso()
        )