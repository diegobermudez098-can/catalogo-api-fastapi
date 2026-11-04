# Mini-API de Catálogo - Guía 1 (GA1-AA3-EV04)
# API de solo lectura. Los productos viven en una lista en memoria.

from fastapi import FastAPI

app = FastAPI()

# "Base de datos" temporal en memoria
productos = [
    {"id": 1, "nombre": "Teclado mecanico", "precio": 120000, "categoria": "Perifericos"},
    {"id": 2, "nombre": "Mouse gamer",      "precio": 85000,  "categoria": "Perifericos"},
    {"id": 3, "nombre": "Monitor 24",       "precio": 650000, "categoria": "Pantallas"},
]


# 1. GET / -> mensaje de bienvenida
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la Mini-API de Catalogo"}


# 2. GET /productos -> lista completa
@app.get("/productos")
def listar_productos():
    return productos


# 3. GET /productos/{producto_id} -> un producto por su id
@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    for producto in productos:
        if producto["id"] == producto_id:
            return producto


# 4. GET /categorias -> categorías distintas (sin repetir)
@app.get("/categorias")
def listar_categorias():
    categorias = []
    for producto in productos:
        if producto["categoria"] not in categorias:
            categorias.append(producto["categoria"])
    return categorias


# 5. GET /buscar?nombre=... -> productos cuyo nombre contenga el texto
@app.get("/buscar")
def buscar_productos(nombre: str = ""):
    resultado = []
    for producto in productos:
        # lower() para que "teclado" encuentre "Teclado mecanico"
        if nombre.lower() in producto["nombre"].lower():
            resultado.append(producto)
    return resultado
