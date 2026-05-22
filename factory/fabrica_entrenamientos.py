from factory.entrenamiento import Entrenamiento
from factory.entrenamiento_cardio import EntrenamientoCardio
from factory.entrenamiento_fuerza import EntrenamientoFuerza


class FabricaEntrenamientos:

    @staticmethod
    def crear_entrenamiento(
        tipo_entrenamiento: str
    ) -> Entrenamiento:

        tipo = tipo_entrenamiento.lower()

        if tipo == "cardio":
            return EntrenamientoCardio()

        if tipo == "fuerza":
            return EntrenamientoFuerza()

        raise ValueError(
            "Tipo de entrenamiento no válido."
        )