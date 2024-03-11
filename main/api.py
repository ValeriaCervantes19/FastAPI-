# Importaciones
from fastapi import FastAPI

# Aplicación FastAPI
app = FastAPI()

# Endpoints
@app.get("/nombres")
async def obtener_nombres():
    return ["Juan", "María", "Pedro"]

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
