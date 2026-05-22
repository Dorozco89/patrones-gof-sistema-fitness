from command.command import Command


class InvocadorComandos:

    def __init__(self) -> None:

        self._comandos = []

    def agregar_comando(
        self,
        comando: Command
    ) -> None:

        self._comandos.append(comando)

    def ejecutar_comandos(self) -> list[str]:

        resultados = []

        for comando in self._comandos:
            resultados.append(
                comando.ejecutar()
            )

        return resultados