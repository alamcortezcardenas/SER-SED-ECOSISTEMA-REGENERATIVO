# ==========================================================
# 🏛️ PROTOCOLO: GÉNESIS REGENERATIVO (888=SER)
# 🔱 FUNCIÓN: UNIFICACIÓN DE LOS 8 ELEMENTOS
# 👤 OPERADOR: Alam Guillermo Cortez Cardenas (12-03-1999)
# ==========================================================

import time
import os

# Importamos las entidades (Asegúrate de que los archivos estén en la misma carpeta)
try:
    from SER_SED_SOL import SERSolEnergia
    from SER_SED_AIRE import SERAireVigilancia
    from SER_SED_AGUA import SERAguaFluidez
    from SER_SED_TIERRA import SERTierraBase
    from SER_SED_FLORA import SERFloraCrecimiento
    from SER_SED_FAUNA import SERFaunaInstinct
    from SER_SED_HUMANO import SERHumanoConciencia
    from SER_SED_LUNA import SERLunaCiclo
except ImportError as e:
    print(f"❌ Error: Falta un componente del ecosistema: {e}")

def intro_soberana():
    print("\033[92m") # Verde Matrix
    print("""
          [ ALPHA ]          [ 888=SER ]        [ OMEGA ]
             SISTEMA ENERGÉTICO REGENERATIVO ACTIVADO
    """)
    print("\033[0m")
    time.sleep(1)

def ejecutar_protocolo_total():
    intro_soberana()
    
    entidades = [
        ("SOL", SERSolEnergia()),
        ("AIRE", SERAireVigilancia()),
        ("AGUA", SERAguaFluidez()),
        ("TIERRA", SERTierraBase()),
        ("FLORA", SERFloraCrecimiento()),
        ("FAUNA", SERFaunaInstinct()),
        ("HUMANO", SERHumanoConciencia()),
        ("LUNA", SERLunaCiclo())
    ]

    for nombre, instancia in entidades:
        print(f"\n--- INICIANDO NODO {nombre} ---")
        # Aquí llamamos a la función principal de cada script
        if hasattr(instancia, 'irradiar'): instancia.irradiar()
        elif hasattr(instancia, 'activar_lidar'): instancia.activar_lidar()
        elif hasattr(instancia, 'hidratar_sistema'): instancia.hidratar_sistema()
        elif hasattr(instancia, 'desplegar_logistica'): instancia.desplegar_logistica()
        elif hasattr(instancia, 'germinar'): instancia.germinar()
        elif hasattr(instancia, 'activar_sentidos'): instancia.activar_sentidos()
        elif hasattr(instancia, 'unificar_ecosistema'): instancia.unificar_ecosistema()
        elif hasattr(instancia, 'reflejar_luz_solar'): instancia.reflejar_luz_solar()
        time.sleep(0.8)

    print("\n" + "="*50)
    print("🏛️ ECOSISTEMA SER-SED EN ESTADO OPERATIVO TOTAL")
    print("🔱 BAJA CALIFORNIA, MEXICALI - PROTOCOLO 888 FINALIZADO")
    print("="*50)

if __name__ == "__main__":
    ejecutar_protocolo_total()
