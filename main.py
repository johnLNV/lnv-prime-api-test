from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sympy import isprime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def buscar_proximo_primo_real(n):
    candidato = n + 1
    while not isprime(candidato):
        candidato += 1
    return candidato

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "resultado": None})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, numero: str = Form(...)):
    try:
        numero_int = int(numero)
        proximo_primo = buscar_proximo_primo_real(numero_int)
        resultado = f"O próximo primo real é {proximo_primo}"
    except Exception as e:
        resultado = f"Erro: {str(e)}"
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "resultado": resultado
    })
