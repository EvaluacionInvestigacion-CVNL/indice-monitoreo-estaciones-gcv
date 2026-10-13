# Índice de Monitoreo de Estaciones (IME) — Días Válidos

Este repositorio contiene el código y los datos procesados para el cálculo del **Índice de Monitoreo de Estaciones (IME)** en su versión de **Días Válidos**, evaluando el desempeño de la red SIMA del Área Metropolitana de Monterrey durante el periodo **Octubre 2025 – Septiembre 2026**.

## Metodología
El cálculo se fundamenta en la **NOM-172-SEMARNAT-2019** y los protocolos del **SINAICA (INECC)**:
- **Día Válido ($DV$):** Día calendario que cuenta con al menos **18 horas válidas** ($val = 1$) registradas.
- **Universo de la Red:** 15 estaciones de monitoreo $\times$ 6 contaminantes criterio ($\text{PM}_{2.5}$, $\text{PM}_{10}$, $\text{NO}_2$, $\text{SO}_2$, $\text{CO}$, $\text{O}_3$).
- **Días Esperados Totales:** $15 \times 6 \times 365 = \mathbf{32,850 \text{ días}}$.

$$IME_{\text{Días}} = \left( \frac{\sum DV}{32,850} \right) \times 100$$
