# Sentiment Analysis Tweepy

Este proyecto extrae tweets de empresas reconocidas, realiza un análisis de sentimientos y genera gráficos con los resultados.

## Estructura del Proyecto

- `data/`: Directorio para almacenar los datos.
  - `raw/`: Datos sin procesar extraídos de Twitter.
  - `processed/`: Datos procesados y listos para el análisis.
- `notebooks/`: Directorio para notebooks de Jupyter.
- `src/`: Directorio para el código fuente del proyecto.
  - `data_extraction.py`: Código para extraer tweets utilizando `tweepy`.
  - `sentiment_analysis.py`: Código para realizar el análisis de sentimientos.
  - `visualization.py`: Código para generar gráficos con los resultados del análisis.
- `tests/`: Directorio para pruebas unitarias.
  - `test_data_extraction.py`: Pruebas para el módulo de extracción de datos.
  - `test_sentiment_analysis.py`: Pruebas para el módulo de análisis de sentimientos.
  - `test_visualization.py`: Pruebas para el módulo de visualización.
- `requirements.txt`: Archivo para listar las dependencias del proyecto.
- `README.md`: Archivo para documentar el proyecto.

## Instalación

```bash
pip install -r requirements.txt