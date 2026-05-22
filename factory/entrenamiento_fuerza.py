from factory.entrenamiento import Entrenamiento


class EntrenamientoFuerza(Entrenamiento):

    def obtener_descripcion(self) -> str:
        return (
            "Entrenamiento enfocado en "
            "ganancia muscular "
            "y desarrollo de fuerza."
        )