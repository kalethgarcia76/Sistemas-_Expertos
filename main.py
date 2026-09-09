from sistema_experto1 import ServidorEstado, diagnosticar_servidor


def construir_casos_de_prueba() -> list[ServidorEstado]:
    """Cada caso está diseñado para activar una rama distinta del motor."""
    return [
        # Caso 1 -> NORMAL (fallback)
        ServidorEstado(cpu_uso=45, memoria_libre=35, ping_respuesta=120,
                        temperatura=65, ventilador_encendido=True),

        # Caso 2 -> CRITICO (temperatura + ventilador apagado)
        ServidorEstado(cpu_uso=55, memoria_libre=40, ping_respuesta=90,
                        temperatura=85, ventilador_encendido=False),

        # Caso 3 -> CRITICO (temperatura alta pero ventilador SÍ activo)
        ServidorEstado(cpu_uso=50, memoria_libre=45, ping_respuesta=100,
                        temperatura=88, ventilador_encendido=True),

        # Caso 4 -> CRITICO (saturación de recursos)
        ServidorEstado(cpu_uso=95, memoria_libre=8, ping_respuesta=150,
                        temperatura=70, ventilador_encendido=True),

        # Caso 5 -> ADVERTENCIA (recursos elevados + latencia > 200)
        ServidorEstado(cpu_uso=80, memoria_libre=30, ping_respuesta=250,
                        temperatura=60, ventilador_encendido=True),

        # Caso 6 -> ADVERTENCIA (latencia crítica aislada)
        ServidorEstado(cpu_uso=40, memoria_libre=50, ping_respuesta=600,
                        temperatura=55, ventilador_encendido=True),

        # Caso 7 -> ADVERTENCIA (solo CPU elevada, sin latencia alta)
        ServidorEstado(cpu_uso=82, memoria_libre=40, ping_respuesta=100,
                        temperatura=60, ventilador_encendido=True),
    ]


def main():
    casos = construir_casos_de_prueba()

    print("=" * 70)
    print("SISTEMA EXPERTO - DIAGNÓSTICO IT")
    print("=" * 70)

    for i, caso in enumerate(casos, start=1):
        diagnostico = diagnosticar_servidor(caso)
        print(f"\nCaso {i}: {caso.to_dict()}")
        print(f"  Veredicto: {diagnostico}")

    # Ejemplo de uso del Módulo de Explicación con un caso puntual
    print("\n" + "=" * 70)
    print("EJEMPLO DE EXPLICACIÓN DETALLADA (Caso 5)")
    print("=" * 70)
    diagnostico_detallado = diagnosticar_servidor(casos[4])
    print(diagnostico_detallado.explicar())


if __name__ == "__main__":
    main()