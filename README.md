# 🎙️ RajoyBot para Slack

> *"Somos sentimientos y tenemos seres humanos"*

Bot de Slack que envía audios de nuestro querido expresidente Mariano Rajoy Brey directamente en tus canales.

---

## Comandos

| Comando | Descripción |
|---|---|
| `/rajoy` | Envía un audio aleatorio de Rajoy |
| `/rajoy <palabra>` | Busca audios por palabra clave (ej: `/rajoy vino`) |
| `/rajoy lista` | Muestra todos los audios disponibles |

Si la búsqueda no encuentra nada, envía uno aleatorio igualmente.

---

## Audios disponibles

| Clave | Descripción |
|---|---|
| `cuanto_peor` | Cuanto peor mejor para todos |
| `es_el_vecino` | Es el alcalde |
| `y_la_europea` | Pues... eh... Y la europea? |
| `la_segunda_ya_tal` | La segunda ya tal |
| `me_gusta_cataluna` | Me gusta Cataluna |
| `hoy_estoy_aqui` | Me ha pasado una cosa |
| `somos_sentimientos` | Somos sentimientos |
| `muy_espanoles` | Los espanoles muy espanoles |
| `lo_que_hemos_hecho` | Lo que nosotros hemos hecho |
| `viva_el_vino` | Viva el vino |
| `ceramica_talavera_v2` | La ceramica de Talavera |
| `no_es_cierto` | No es cierto |
| `ser_serio` | Lo unico serio |
| `solidario` | Ser solidario |
| `maquinas` | Maquina-inception |
| `300_anos` | Dentro de 300 anos |
| `agua_cae_cielo` | Agua que cae del cielo |
| `no_mas_iva` | No mas IVA |
| `bajar_los_impuestos` | Bajar los impuestos |
| `hilitos` | Hilitos de na |
| `proximo_ano_2016` | Lo mejor para el proximo ano 2016 |
| `lo_imposible` | Lo imposible |
| `que_se_puede_hacer` | Que se puede hacer |
| `eta_gran_nacion` | ETA es una gran nacion |
| `chuches` | Chuches |
| `un_vaso_es_un_vaso` | Vaso |
| `piensan_antes_hablar` | Piensan antes de hablar? |
| `its_very_difficult` | It's very difficult todo esto |
| `galileo` | Como decia Galileo... |
| `75_millones` | 75 millones de espanoles |
| `fin_de_la_cita` | Fin de la cita |
| `no_he_dormido_nada` | No he dormido nada, no me pregunten demasiado |
| `domo_arigato_gozaimasu` | Domo arigato gozaimasu |
| `te_dejo_mi_tractor` | Te dejo mi tractor |
| `toma_democracia` | Toma democracia |
| `por_las_carreteras` | Por las carreteras tienen que ir coches |
| `ha_estado_muy_bien` | Ha estado muy bien |
| `aroma_de_lo_absurdo` | Percibe el aroma de lo absurdo? |
| `no_entiendo_mi_letra` | Hoy estoy aqui |
| `dentro_de_un_orden` | Estoy dentro de un orden y por tanto en equilibrio gracias |

---

## Stack

- **Python 3.11** + **Flask** — servidor web
- **slack-sdk** — integración con la API de Slack
- **ffmpeg** — conversión de audio ogg a mp3
- **Docker** — contenedor para despliegue
- **Render** — hosting gratuito
- **UptimeRobot** — ping cada 5 minutos para evitar que el servidor se duerma

---

## Despliegue propio

### Requisitos

- Cuenta en [Slack API](https://api.slack.com/apps)
- Cuenta en [Render](https://render.com)
- Cuenta en [UptimeRobot](https://uptimerobot.com)

### Variables de entorno

| Variable | Descripción |
|---|---|
| `SLACK_BOT_TOKEN` | Token del bot de Slack (`xoxb-...`) |

### Scopes necesarios en Slack

- `commands`
- `files:write`
- `chat:write`

### Slash Command

Crear un comando `/rajoy` apuntando a `https://TU_URL/rajoy`.

---

## Créditos

Audios originales del repo [elraro/rajoybot](https://github.com/elraro/rajoybot).
