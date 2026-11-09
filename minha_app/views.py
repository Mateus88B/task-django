from django.http import HttpResponse
from pathlib import Path

def home(request):
    caminho = Path(__file__).parent / "index.html"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        pagina = arquivo.read()

    return HttpResponse(pagina)