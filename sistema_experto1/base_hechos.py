from dataclasses import dataclass


@dataclass
class ServidorEstado:
    """Métricas técnicas de un servidor en un instante dado."""

    cpu_uso: float               # % de uso de CPU (0-100)
    memoria_libre: float         # % de memoria libre (0-100)
    ping_respuesta: float        # latencia en ms
    temperatura: float           # temperatura en grados Celsius
    ventilador_encendido: bool   # estado del ventilador

    def __post_init__(self):
        # Validación básica de la Base de Hechos: un SE serio no debería
        # razonar sobre datos imposibles.
        for campo in ("cpu_uso", "memoria_libre"):
            valor = getattr(self, campo)
            if not (0 <= valor <= 100):
                raise ValueError(f"{campo} debe estar entre 0 y 100, recibido: {valor}")
        if self.ping_respuesta < 0:
            raise ValueError("ping_respuesta no puede ser negativo")

    def to_dict(self) -> dict:
        """Compatibilidad con el formato original basado en diccionarios."""
        return self.__dict__.copy()
