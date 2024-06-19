import os
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from routes import product_routes

app = FastAPI(
    title='Nonsense shop'
)

current_dir = os.path.dirname(os.path.abspath(__file__))
ssl_dir = os.path.join(current_dir, 'ssl')
cert_path = os.path.join(ssl_dir, 'cert.pem')
key_path = os.path.join(ssl_dir, 'key.pem')

app.mount("/static", StaticFiles(directory="static"), name="static")
# app.include_router(main_routes.router)
app.include_router(product_routes.router)

if __name__ == '__main__':
    try:
        uvicorn.run(app, host="127.0.0.1", port=8000, ssl_keyfile=key_path, ssl_certfile=cert_path)
    except Exception as e:
        print(e)
