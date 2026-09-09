
from dataclasses import dataclass
from typing import Callable
from .base_hechos import ServidorEstado


@dataclass
class Regla:
    nombre: str
    severidad: str  # "CRITICO", "ADVERTENCIA", "NORMAL"
    condicion: Callable[[ServidorEstado], bool]
    mensaje: str



REGLAS: list[Regla] = [
    Regla(
        nombre="R1_sobrecalentamiento_sin_ventilador",
        severidad="CRITICO",
        condicion=lambda h: h.temperatura > 80 and not h.ventilador_encendido,
        mensaje=(
            "Sobrecalentamiento severo. Temperatura > 80C con ventilador "
            "apagado. Riesgo de apagado de hardware."
        ),
    ),
    Regla(
        nombre="R2_sobrecalentamiento_con_ventilador",
        severidad="CRITICO",
        condicion=lambda h: h.temperatura > 80 and h.ventilador_encendido,
        mensaje="Temperatura > 80C pese a ventilador activo. Revisar sistema de refrigeracion.",
    ),
    Regla(
        nombre="R3_saturacion_recursos",
        severidad="CRITICO",
        condicion=lambda h: h.cpu_uso > 90 and h.memoria_libre < 10,
        mensaje="Saturacion de recursos (CPU > 90% y memoria libre < 10%).",
    ),
    Regla(
        nombre="R4_recursos_y_latencia",
        severidad="ADVERTENCIA",
        condicion=lambda h: (h.cpu_uso > 75 or h.memoria_libre < 20) and h.ping_respuesta > 200,
        mensaje="Uso elevado de recursos combinado con latencia alta (ping > 200 ms).",
    ),
    Regla(
        nombre="R5_latencia_critica",
        severidad="ADVERTENCIA",
        condicion=lambda h: h.ping_respuesta > 500,
        mensaje="Latencia critica de red (ping > 500 ms).",
    ),
    Regla(
        nombre="R6_recursos_elevados",
        severidad="ADVERTENCIA",
        condicion=lambda h: h.cpu_uso > 75 or h.memoria_libre < 20,
        mensaje="CPU elevada o memoria baja. Monitorear tendencia.",
    ),
]

# Regla por defecto (fallback) si ninguna de las anteriores dispara.
REGLA_DEFECTO = Regla(
    nombre="R0_normal",
    severidad="NORMAL",
    condicion=lambda h: True,
    mensaje="Todos los parametros dentro de rango operativo.",
)
