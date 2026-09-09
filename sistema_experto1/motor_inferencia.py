
from dataclasses import dataclass, field
from .base_hechos import ServidorEstado
from .base_reglas import REGLAS, REGLA_DEFECTO, Regla


@dataclass
class Diagnostico:
    severidad: str
    mensaje: str
    regla_disparada: str
    traza: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return f"{self.severidad}: {self.mensaje}"

    def explicar(self) -> str:
        """Módulo de Explicación: reconstruye el razonamiento paso a paso."""
        lineas = [f"Regla aplicada: {self.regla_disparada}"]
        lineas.append("Orden de evaluación:")
        lineas.extend(f"  - {paso}" for paso in self.traza)
        return "\n".join(lineas)


def diagnosticar_servidor(hechos: ServidorEstado) -> Diagnostico:
    """
    Recorre la Base de Reglas en orden de precedencia y devuelve el
    primer diagnóstico que dispare (estrategia de resolución de
    conflictos: primera regla que coincide, igual que en el Taller 1).
    """
    traza: list[str] = []

    for regla in REGLAS:
        cumple = regla.condicion(hechos)
        traza.append(f"{regla.nombre} -> {'CUMPLE' if cumple else 'no cumple'}")
        if cumple:
            return Diagnostico(
                severidad=regla.severidad,
                mensaje=regla.mensaje,
                regla_disparada=regla.nombre,
                traza=traza,
            )

    # Ninguna regla específica disparó: fallback
    traza.append(f"{REGLA_DEFECTO.nombre} -> CUMPLE (fallback)")
    return Diagnostico(
        severidad=REGLA_DEFECTO.severidad,
        mensaje=REGLA_DEFECTO.mensaje,
        regla_disparada=REGLA_DEFECTO.nombre,
        traza=traza,
    )
