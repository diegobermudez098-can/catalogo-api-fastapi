# Mini-API de Catálogo (FastAPI)

Evidencia GA1-AA3-EV04 - Guía 1 de APIs con FastAPI (ADSO - SENA).

API de solo lectura para el catálogo de una tienda. Los productos están en una lista en memoria dentro de `main.py` (todavía no usa base de datos).

## Cómo instalar

1. Abrir una terminal dentro de la carpeta del proyecto.

2. Crear el entorno virtual:

```
python -m venv venv
```

3. Activarlo:

```
# Windows (PowerShell / CMD)
venv\Scripts\activate

# Linux o macOS
source venv/bin/activate
```

4. Instalar FastAPI y Uvicorn:

```
pip install fastapi "uvicorn[standard]"
```

## Cómo ejecutar

```
uvicorn main:app --reload
```

La API queda en http://127.0.0.1:8000

La documentación interactiva para probar los endpoints está en http://127.0.0.1:8000/docs

## Endpoints

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| GET | `/` | Mensaje de bienvenida |
| GET | `/productos` | Lista completa de productos |
| GET | `/productos/{producto_id}` | Producto con ese id |
| GET | `/categorias` | Categorías distintas de los productos |
| GET | `/buscar?nombre=...` | Productos cuyo nombre contenga el texto buscado |

## Capturas

Las capturas de `/docs` con cada endpoint probado ("Try it out") están en la carpeta `capturas/`.
