from factory.entrenamiento import Entrenamiento


class EntrenamientoCardio(Entrenamiento):

    def obtener_descripcion(self) -> str:
        return (
            "Entrenamiento enfocado en "
            "resistencia cardiovascular "
            "y quema de grasa."
        )