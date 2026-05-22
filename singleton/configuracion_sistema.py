class ConfiguracionSistema:

    _instancia = None

    def __new__(cls):

        if cls._instancia is None:
            cls._instancia = super(
                ConfiguracionSistema,
                cls
            ).__new__(cls)

            cls._instancia.nombre_gimnasio = (
                "Fitness GOF Center"
            )

            cls._instancia.modo_pruebas = False

        return cls._instancia

    def obtener_configuracion(self) -> str:

        return (
            f"Gimnasio: "
            f"{self.nombre_gimnasio} | "
            f"Modo pruebas: "
            f"{self.modo_pruebas}"
        )