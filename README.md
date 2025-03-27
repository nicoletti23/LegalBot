
# LegalBot 🤖⚖️

Generador de documentos legales automatizado para Colombia usando DeepSeek-V3.

## Estructura del Proyecto
LegalBot/
│── backend/                   # Servidor con FastAPI + Scraping + Firma DIAN
│   ├── main.py                # API principal con FastAPI
│   ├── scraping.py            # Web Scraping de leyes DIAN + Congreso
│   ├── firma_dian.py          # Firma Electrónica DIAN
│   ├── pagos.py               # Monetización con Stripe
│   ├── database.py            # Conexión a la base de datos
│   ├── models.py              # Modelos de datos con SQLAlchemy
│   ├── requirements.txt       # Dependencias
│
│── frontend/                   # Interfaz Web con React
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chatbot.js     # Chatbot Legal
│   │   │   ├── Pagos.js       # Página de pagos
│   │   │   ├── Dashboard.js   # Estadísticas y alertas
│   │   ├── App.js             # Enrutamiento de la App
│   ├── package.json           # Dependencias frontend
│
│── mobile/                     # Aplicación Móvil con React Native
│   ├── src/
│   │   ├── ChatScreen.js      # Pantalla del chatbot
│   │   ├── HomeScreen.js      # Pantalla principal
│   ├── App.js                 # Configuración inicial
│   ├── package.json           # Dependencias móviles
│
│── README.md                   # Documentación del proyecto
│── .gitignore                   # Archivos a ignorar en GitHub
│── deploy.md                   # Guía de despliegue en VPS gratuito
