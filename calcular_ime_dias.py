"""
Cálculo del Índice de Monitoreo de Estaciones (IME) - Versión Días Válidos
--------------------------------------------------------------------------
Metodología: NOM-172-SEMARNAT-2019 / SINAICA - INECC
Periodo: Octubre 2025 - Septiembre 2026
Red: SIMA Monterrey (15 estaciones x 6 contaminantes criterio)
Criterio de Día Válido: >= 18 horas válidas (val = 1) en un día de 24h.
"""

import pandas as pd

# 1. Cargar archivo de datos
archivo_csv = "cobertura_15_estaciones_monterrey_occam.csv"
print(f"Cargando datos desde: {archivo_csv}...")
df = pd.read_csv(archivo_csv)

# 2. Constantes de la Red SIMA
TOTAL_ESTACIONES = 15
TOTAL_CONTAMINANTES = 6
DIAS_AÑO = 365
TOTAL_DIAS_ESPERADOS = TOTAL_ESTACIONES * TOTAL_CONTAMINANTES * DIAS_AÑO  # 32,850

# 3. Cálculo de Días Válidos
tot_dias_validos = df["dias_validos"].sum()
ime_dias = (tot_dias_validos / TOTAL_DIAS_ESPERADOS) * 100

# 4. Imprimir resultados
print("=" * 65)
print(" CÁLCULO DEL IME - VERSIÓN DÍAS VÁLIDOS (NOM-172)")
print("=" * 65)
print(f"• Días Válidos Obtenidos (DV):  {int(tot_dias_validos):,} días")
print(f"• Días Totales Esperados Red:    {TOTAL_DIAS_ESPERADOS:,} días")
print(f"• RESULTADO IME DÍAS VÁLIDOS:    {ime_dias:.2f}%\n")
print("Desglose por contaminante (Días Válidos totales):")
print(df.groupby("parametro")["dias_validos"].sum().to_string())
print("=" * 65)