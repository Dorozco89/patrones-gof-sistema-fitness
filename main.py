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


def mostrar_separador() -> None:
    print("\n" + "=" * 70 + "\n")


def main() -> None:

    facade = SistemaFitnessFacade()

    invocador = InvocadorComandos()

    comando_crear = CrearRutinaCommand(
        facade
    )

    comando_actualizar = (
        ActualizarRutinaCommand()
    )

    comando_eliminar = (
        EliminarRutinaCommand()
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
        invocador.ejecutar_comandos()
    )

    print("\nSISTEMA FITNESS GOF\n")

    for resultado in resultados:

        mostrar_separador()

        print(resultado)

    mostrar_separador()

    print(
        "Sistema ejecutado correctamente."
    )


if __name__ == "__main__":
    main()