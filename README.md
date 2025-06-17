# 🔍 S1_net-scanner | Escáner Avanzado de Red Local en Python

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Estado](https://img.shields.io/badge/Estado-Activo-yellow)]()
[![OS](https://img.shields.io/badge/Sistema-macOS-lightgrey?logo=apple)]

> 🚀 Herramienta práctica de ciberseguridad para detectar dispositivos conectados a una red local, identificar fabricantes y registrar resultados en CSV. Ideal para análisis de red, auditoría básica o aprendizaje técnico.

---

## ✨ Características

- ⚡ Escaneo ARP en tiempo real con Scapy
- 🧠 Detección de IP, dirección MAC y fabricante (vendor)
- 🧾 Exportación automática a archivos `.csv`
- 📊 Visualización en consola con formato de tabla (`tabulate`)
- 🔐 Aplicable en escenarios reales de red: reconocimiento, defensa, auditoría

---

## 📋 Requisitos del sistema

- ✅ macOS (probado)
- ✅ Python 3.11+
- ✅ Permisos de administrador para ejecutar Scapy (`sudo`)
- ✅ Conexión a una red local (Wi-Fi o Ethernet)

---

## 📦 Librerías utilizadas

```bash
scapy==2.5.0
mac-vendor-lookup
tabulate

Instálalas con:
pip install scapy mac-vendor-lookup tabulate

O si tienes un requirements.txt:
pip install -r requirements.txt

Instrucciones de uso
# 1. Clona el repositorio
git clone https://github.com/TU_USUARIO/cyber-jaime.git
cd cyber-jaime/S1_net-scanner

# 2. Crea y activa entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Ejecuta el escáner (usa sudo en macOS)
sudo venv/bin/python scanner.py

📂 Estructura del proyecto

S1_net-scanner/
├── scanner.py               ← Script principal
├── resultado_*.csv          ← Escaneos guardados por fecha
├── requirements.txt         ← Dependencias del entorno
├── README.md                ← Documentación
└── venv/                    ← Entorno virtual local (ignorado por Git)


Ejemplo de salida en consola
[*] Escaneando red local...

╒═════════════════╤══════════════════════╤════════════════════════════════╕
│ IP              │ MAC                  │ Fabricante                     │
╞═════════════════╪══════════════════════╪════════════════════════════════╡
│ 192.168.0.1     │ b8:27:eb:de:ad:be    │ Raspberry Pi Foundation        │
│ 192.168.0.105   │ f0:18:98:12:34:56    │ Apple, Inc.                    │
╘═════════════════╧══════════════════════╧════════════════════════════════╛

[*] Resultados guardados en: resultado_escaneo_20250617_1830.csv

🧠 Bitácora técnica (resumen real de trabajo)
🗓️ Semana 1 – Desarrollo del escáner de red

✅ Día 1:
- Instalación de Python, Wireshark, Scapy, Nmap
- Escaneo manual con Nmap, verificación de IP local

✅ Día 2:
- Captura de paquetes en Wireshark (HTTP, ARP, DNS)
- Estudio de protocolos y comportamiento en red

✅ Día 3:
- Creación de script de escaneo con Scapy (IP y MAC)
- Ejecución exitosa en red local, ajustes de timeout

✅ Día 4:
- Integración de `mac-vendor-lookup` para obtener fabricante
- Uso de `tabulate` para formateo profesional de la salida

✅ Día 5:
- Exportación automática a CSV
- Documentación del proyecto en `README.md`
- Preparación para portafolio profesional

🔐 Aplicación práctica en ciberseguridad

Técnica
Uso Defensivo (Blue Team)
Uso Ofensivo (Red Team)
Escaneo ARP
Inventario de red
Reconocimiento previo al ataque
Detección de fabricantes
Identificar dispositivos no autorizados
Filtrado de objetivos vulnerables
Registro histórico
Seguimiento de cambios en la red


🚧 Próximas mejoras
	•	🔄 Comparación automática entre escaneos (ver cambios)
	•	📩 Notificaciones por Telegram o correo si aparece un dispositivo nuevo
	•	🕓 Escaneo automatizado con cron jobs
	•	🌐 Interfaz web para visualizar dispositivos en tiempo real (Flask/Streamlit)

👨‍💻 Autor

Jaime Crow
📍 Melbourne, Australia
🎓 Estudiante de ciberseguridad con enfoque práctico y autodidacta
🔗 GitHub: https://github.com/TU_USUARIO
🔗 LinkedIn: https://linkedin.com/in/TU_PERFIL

🤝 Contribuciones
¿Quieres aportar al proyecto o adaptarlo a otros entornos?
Puedes abrir un issue, proponer una mejora o enviar un pull request.
¡Todo aporte es bienvenido! 💬

📜 Licencia
Este proyecto se distribuye bajo la Licencia MIT.
Puedes usarlo, modificarlo y compartirlo libremente con fines académicos o profesionales.
