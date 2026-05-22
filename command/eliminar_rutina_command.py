from command.command import Command


class EliminarRutinaCommand(Command):

    def ejecutar(self) -> str:

        return (
            "Rutina fitness eliminada "
            "correctamente."
        )