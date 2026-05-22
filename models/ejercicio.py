class Ejercicio:

    def __init__(
        self,
        nombre: str,
        series: int,
        repeticiones: int,
        tiempo_descanso: int
    ) -> None:
        self.nombre = nombre
        self.series = series
        self.repeticiones = repeticiones
        self.tiempo_descanso = tiempo_descanso

    def mostrar_ejercicio(self) -> str:
         
        return (
            f"Ejercicio: {self.nombre} | "
            f"Series: {self.series} | "
            f"Repeticiones: {self.repeticiones} | "
            f"Descanso: {self.tiempo_descanso} segundos"
        )