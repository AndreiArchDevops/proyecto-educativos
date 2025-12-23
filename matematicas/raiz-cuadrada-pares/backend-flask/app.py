from flask import Flask, render_template, request

app = Flask(__name__)

def raiz_cuadrada_pares(numero, decimales=5):
    pasos = []
    resultado = 0
    residuo = 0
    numero_str = str(numero)
    
    # Separar en pares desde la derecha
    if len(numero_str) % 2 != 0:
        numero_str = '0' + numero_str
    pares = [int(numero_str[i:i+2]) for i in range(0, len(numero_str), 2)]
    
    for par in pares:
        residuo = residuo * 100 + par
        for x in range(10):
            if (resultado * 20 + x) * x > residuo:
                x -= 1
                break
        residuo -= (resultado * 20 + x) * x
        resultado = resultado * 10 + x
        pasos.append(f"Bajo par {par:02d}, pruebo {x}, residuo {residuo}, resultado {resultado}")

    # Calcular decimales
    for d in range(decimales):
        residuo *= 100
        for x in range(10):
            if (resultado * 20 + x) * x > residuo:
                x -= 1
                break
        residuo -= (resultado * 20 + x) * x
        resultado = resultado * 10 + x
        pasos.append(f"Decimal {d+1}: pruebo {x}, residuo {residuo}, resultado {resultado}")
    
    raiz_final = resultado / (10 ** decimales)
    return raiz_final, pasos

@app.route('/', methods=['GET', 'POST'])
def index():
    raiz = None
    pasos = []
    numero = ''
    if request.method == 'POST':
        numero = request.form.get('numero', '0')
        try:
            numero_int = int(numero)
            raiz, pasos = raiz_cuadrada_pares(numero_int, decimales=5)
        except ValueError:
            raiz = 'Número inválido'
            pasos = []
    return render_template('index.html', numero=numero, raiz=raiz, pasos=pasos)
