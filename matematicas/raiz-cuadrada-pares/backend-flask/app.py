from flask import Flask, render_template, request

app = Flask(__name__)

def raiz_por_pares(numero):
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

        pasos.append(
            f"Se baja el par {par}, se prueba {x} porque ({resultado + str(x)}) × {x} ≤ {actual}"
        )

        resto = actual - int(resultado + str(x)) * x
        resultado += str(x)

    return resultado, pasos


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    pasos = []
    pares = []
    numero = None

    if request.method == "POST":
        numero = int(request.form["numero"])
        resultado, pasos = raiz_por_pares(numero)

        num_str = str(numero)
        if len(num_str) % 2 != 0:
            num_str = "0" + num_str

        pares = [num_str[i:i+2] for i in range(0, len(num_str), 2)]

    return render_template(
        "index.html",
        resultado=resultado,
        pasos=pasos,
        pares=pares,
        numero=numero
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
