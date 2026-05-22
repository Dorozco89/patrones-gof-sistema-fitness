from typing import List

from models.ejercicio import Ejercicio


class RutinaFitness:
    
    def __init__(
        self,
        nombre: str,
        objetivo: str,
        nivel_dificultad: str,
        duracion: int
    ) -> None:

        self.nombre = nombre
        self.objetivo = objetivo
        self.nivel_dificultad = nivel_dificultad
        self.duracion = duracion

        self.ejercicios: List[Ejercicio] = []
        self.caracteristicas_adicionales: List[str] = []

    def agregar_ejercicio(self, ejercicio: Ejercicio) -> None:
        """
        Agrega un ejercicio a la rutina.
        """

        self.ejercicios.append(ejercicio)

    def agregar_caracteristica(
        self,
        caracteristica: str
    ) -> None:
        
        self.caracteristicas_adicionales.append(
            caracteristica
        )

    def mostrar_detalles(self) -> str:
      
        ejercicios_info = "\n".join(
            ejercicio.mostrar_ejercicio()
            for ejercicio in self.ejercicios
        )

        caracteristicas = ", ".join(
            self.caracteristicas_adicionales
        )

        return (
            f"\nRutina: {self.nombre}\n"
            f"Objetivo: {self.objetivo}\n"
            f"Dificultad: {self.nivel_dificultad}\n"
            f"Duración: {self.duracion} minutos\n\n"
            f"Ejercicios:\n{ejercicios_info}\n\n"
            f"Características adicionales: "
            f"{caracteristicas if caracteristicas else 'Ninguna'}"
        )