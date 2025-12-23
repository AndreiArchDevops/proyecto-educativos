from flask import Flask, render_template, request

app = Flask(__name__)

def raiz_por_pares(numero, decimales=5):
    pasos = []
    num_str = str(numero)

    if len(num_str) % 2 != 0:
        num_str = "0" + num_str

    pares = [num_str[i:i+2] for i in range(0, len(num_str), 2)]
    resto = 0
    resultado = ""

    for par in pares:
        actual = resto * 100 + int(par)
        x = 0
        while (int(resultado + str(x)) * x) <= actual:
            x += 1
        x -= 1
        pasos.append(f"Se baja el par {par}, se prueba {x} porque ({resultado + str(x)}) × {x} ≤ {actual}")
        resto = actual - int(resultado + str(x)) * x
        resultado += str(x)

    # calcular decimales si hay residuo
    dec_result = resultado
    resto_decimal = resto
    for _ in range(decimales):
        resto_decimal *= 100
        x = 0
        while (int(dec_result + str(x)) * x) <= resto_decimal:
            x += 1
        x -= 1
        dec_result += str(x)
        resto_decimal -= int(dec_result[-1]) * int(dec_result[:-1] or "0")

    # resultado final como float con decimales
    raiz_final = float(dec_result[:-decimales] + "." + dec_result[-decimales:])
    return raiz_final, pasos, pares

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    pasos = []
    pares = []
    numero = None

    if request.method == "POST":
        numero = int(request.form["numero"])
        resultado, pasos, pares = raiz_por_pares(numero)

    return render_template(
        "index.html",
        resultado=resultado,
        pasos=pasos,
        pares=pares,
        numero=numero
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
