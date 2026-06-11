import os
import random
import subprocess
import tempfile
import threading
from flask import Flask, request
from slack_sdk import WebClient

app = Flask(__name__)

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)

SOUNDS_FOLDER = "RajoyBotSounds"

AUDIOS = {
    "cuanto_peor":            "Cuanto peor mejor para todos",
    "es_el_vecino":           "Es el alcalde",
    "y_la_europea":           "Pues... eh... Y la europea?",
    "la_segunda_ya_tal":      "La segunda ya tal",
    "me_gusta_cataluna":      "Me gusta Cataluna",
    "hoy_estoy_aqui":         "Me ha pasado una cosa",
    "somos_sentimientos":     "Somos sentimientos",
    "muy_espanoles":          "Los espanoles muy espanoles",
    "lo_que_hemos_hecho":     "Lo que nosotros hemos hecho",
    "viva_el_vino":           "Viva el vino",
    "ceramica_talavera_v2":   "La ceramica de Talavera",
    "no_es_cierto":           "No es cierto",
    "ser_serio":              "Lo unico serio",
    "solidario":              "Ser solidario",
    "maquinas":               "Maquina-inception",
    "300_anos":               "Dentro de 300 anos",
    "agua_cae_cielo":         "Agua que cae del cielo",
    "no_mas_iva":             "No mas IVA",
    "bajar_los_impuestos":    "Bajar los impuestos",
    "hilitos":                "Hilitos de na",
    "proximo_ano_2016":       "Lo mejor para el proximo ano 2016",
    "lo_imposible":           "Lo imposible",
    "que_se_puede_hacer":     "Que se puede hacer",
    "eta_gran_nacion":        "ETA es una gran nacion",
    "chuches":                "Chuches",
    "un_vaso_es_un_vaso":     "Vaso",
    "piensan_antes_hablar":   "Piensan antes de hablar?",
    "its_very_difficult":     "It's very difficult todo esto",
    "galileo":                "Como decia Galileo...",
    "75_millones":            "75 millones de espanoles",
    "fin_de_la_cita":         "Fin de la cita",
    "no_he_dormido_nada":     "No he dormido nada, no me pregunten demasiado",
    "domo_arigato_gozaimasu": "Domo arigato gozaimasu",
    "te_dejo_mi_tractor":     "Te dejo mi tractor",
    "toma_democracia":        "Toma democracia",
    "por_las_carreteras":     "Por las carreteras tienen que ir coches",
    "ha_estado_muy_bien":     "Ha estado muy bien",
    "aroma_de_lo_absurdo":    "Percibe el aroma de lo absurdo?",
    "no_entiendo_mi_letra":   "Hoy estoy aqui",
    "dentro_de_un_orden":     "Estoy dentro de un orden y por tanto en equilibrio gracias",
}

def ogg_a_mp3(ogg_path):
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False, dir="/tmp")
    tmp.close()
    resultado = subprocess.run(
        ["ffmpeg", "-y", "-i", ogg_path, "-q:a", "2", tmp.name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if resultado.returncode != 0:
        raise Exception(f"ffmpeg error: {resultado.stderr.decode()}")
    return tmp.name

def enviar_audio(channel_id, nombre, descripcion):
    ogg_path = os.path.join(SOUNDS_FOLDER, f"{nombre}.ogg")
    mp3_path = ogg_a_mp3(ogg_path)
    try:
        client.files_upload_v2(
            channel=channel_id,
            file=mp3_path,
            filename=f"{nombre}.mp3",
            initial_comment=f"🎙️ {descripcion}"
        )
    finally:
        os.unlink(mp3_path)

@app.route("/", methods=["GET", "HEAD"])
def ping():
    return "OK", 200

@app.route("/rajoy", methods=["POST"])
def rajoy():
    channel_id = request.form.get("channel_id")
    texto = request.form.get("text", "").strip().lower()

    if texto == "lista":
        lista = "\n".join([f"• `{k}` - {v}" for k, v in AUDIOS.items()])
        return f"*Audios disponibles:*\n{lista}", 200

    if texto:
        coincidencias = {
            k: v for k, v in AUDIOS.items()
            if texto in k.lower() or texto in v.lower()
        }
        nombre = random.choice(list(coincidencias.keys())) if coincidencias else random.choice(list(AUDIOS.keys()))
    else:
        nombre = random.choice(list(AUDIOS.keys()))

    descripcion = AUDIOS[nombre]

    hilo = threading.Thread(target=enviar_audio, args=(channel_id, nombre, descripcion))
    hilo.start()

    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)