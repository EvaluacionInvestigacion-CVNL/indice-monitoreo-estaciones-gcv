"""
Cálculo del Índice de Monitoreo de Estaciones (IME) - Red SIMA Monterrey
-----------------------------------------------------------------------
Evalúa las dos versiones oficiales del indicador:
1. Versión Días Válidos (NOM-172-SEMARNAT-2019)
2. Versión Horas Válidas (SINAICA / INECC)

Periodo: Octubre 2025 - Septiembre 2026
Red: SIMA Monterrey (15 estaciones x 6 contaminantes criterio)
"""

import os
import sys
import pandas as pd

# Evita errores de codificación en la consola de Windows (cp1252)
sys.stdout.reconfigure(encoding="utf-8")

# 1. Ubicar y cargar archivo de datos
archivo_csv = "cobertura_15_estaciones_monterrey_occam.csv"

# Verificar si está en la raíz o dentro de la carpeta 'resultados'
if not os.path.exists(archivo_csv) and os.path.exists(
    "resultados/cobertura_por_estacion.csv"
):
  archivo_csv = "resultados/cobertura_por_estacion.csv"

print(f"Cargando matriz de datos desde: {archivo_csv}...\n")
df = pd.read_csv(archivo_csv)

# 2. Constantes oficiales de la Red SIMA
TOTAL_ESTACIONES = 15
TOTAL_CONTAMINANTES = 6
DIAS_AÑO = 365
HORAS_AÑO = 8760

TOTAL_DIAS_ESPERADOS = TOTAL_ESTACIONES * TOTAL_CONTAMINANTES * DIAS_AÑO  # 32,850
TOTAL_HORAS_ESPERADAS = (
    TOTAL_ESTACIONES * TOTAL_CONTAMINANTES * HORAS_AÑO
)  # 788,400

# 3. Cálculos de Indicadores
tot_dias_validos = df["dias_validos"].sum()
ime_dias = (tot_dias_validos / TOTAL_DIAS_ESPERADOS) * 100

tot_horas_validas = df["horas_validas_totales"].sum()
ime_horas = (tot_horas_validas / TOTAL_HORAS_ESPERADAS) * 100

# 4. Impresión de Resultados en Consola
print("=" * 70)
print("     ÍNDICE DE MONITOREO DE ESTACIONES (IME) — RED SIMA MONTERREY")
print("                     (Octubre 2025 – Septiembre 2026)")
print("=" * 70)

print("\n 1. VERSIÓN DÍAS VÁLIDOS (Criterio NOM-172-SEMARNAT-2019)")
print(f"   • Días Válidos Obtenidos: {int(tot_dias_validos):>8,} días")
print(f"   • Días Esperados Red:     {TOTAL_DIAS_ESPERADOS:>8,} días")
print(f"   RESULTADO IME DÍAS:    {ime_dias:>8.2f}%\n")

print("⏱ 2. VERSIÓN HORAS VÁLIDAS (Protocolos SINAICA / INECC)")
print(f"   • Horas Válidas Obtenidas:{int(tot_horas_validas):>8,} horas")
print(f"   • Horas Esperadas Red:    {TOTAL_HORAS_ESPERADAS:>8,} horas")
print(f"   RESULTADO IME HORAS:   {ime_horas:>8.2f}%\n")

print("=" * 70)
print(" RESUMEN DE COBERTURA POR CONTAMINANTE CRITERIO")
print("=" * 70)

desglose = df.groupby("parametro")[["dias_validos", "horas_validas_totales"]].sum()
desglose.columns = ["Días Válidos", "Horas Válidas"]
desglose["% Cobertura Días"] = (
    desglose["Días Válidos"] / (TOTAL_ESTACIONES * DIAS_AÑO)
) * 100
desglose["% Cobertura Horas"] = (
    desglose["Horas Válidas"] / (TOTAL_ESTACIONES * HORAS_AÑO)
) * 100

print(desglose.round(2).to_string())
print("=" * 70)