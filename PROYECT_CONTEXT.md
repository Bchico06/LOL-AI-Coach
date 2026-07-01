# LOL AI Coach - Project Context

## Objetivo

Desarrollar un coach de IA para League of Legends que funcione completamente en local.

El programa debe:

- Detectar automáticamente cuando se inicia League of Legends.
- Esperar una partida.
- Capturar únicamente la ventana del juego.
- Analizar el estado de la partida utilizando:
  - League Client API
  - Captura de pantalla
  - Qwen2.5-VL ejecutándose en llama.cpp
- Generar recomendaciones estratégicas.
- Reproducirlas mediante Piper TTS.
- Mostrar información mediante un overlay.

Este proyecto debe tener calidad profesional y servir como portfolio.

---

# Estado actual

La estructura del proyecto ya fue creada.

Se utiliza:

- Python
- venv
- requirements.txt
- Git
- GitHub

Repositorio:

https://github.com/Bchico06/LOL-AI-Coach

---

# Filosofía del proyecto

NO es un script.

NO es un prototipo.

Debe desarrollarse como una aplicación profesional.

Toda decisión de arquitectura debe priorizar:

- Escalabilidad
- Mantenibilidad
- Bajo acoplamiento
- Separación de responsabilidades

No deben proponerse cambios grandes de arquitectura salvo que exista una razón técnica muy fuerte.

---

# Arquitectura

Actualmente la arquitectura objetivo es:

```
Application
        │
        ▼
StateMachine
        │
        ▼
ApplicationContext
        │
 ┌──────┼─────────────┐
 │      │             │
 ▼      ▼             ▼
League  Capture    Voice
Watcher Service    Service
 │
 ▼
Vision
 │
 ▼
Coach
 │
 ▼
Overlay
```

Toda la aplicación será orquestada por Application.

---

# main.py

Debe permanecer extremadamente pequeño.

Debe contener únicamente:

```python
from backend.app.application import Application

def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()
```

No debe contener lógica.

---

# Application

Es el orquestador principal.

Responsabilidades:

- cargar configuración
- crear logger
- crear ApplicationContext
- crear servicios
- iniciar servicios
- detener servicios

No debe contener lógica específica de League of Legends.

---

# StateMachine

La máquina de estados controla el estado global del programa.

Estados actuales:

- BOOTING
- WAITING_CLIENT
- CLIENT_READY
- IN_QUEUE
- CHAMP_SELECT
- LOADING
- IN_GAME
- POST_GAME
- SHUTDOWN

No debe conocer detalles de implementación.

---

# ApplicationContext

Debe centralizar dependencias compartidas.

Ejemplo:

```python
context.settings
context.logger
context.event_bus
context.state_machine
```

Los servicios deben recibir únicamente:

```python
context
```

No múltiples parámetros.

---

# BackgroundService

Todos los servicios deben heredar de BackgroundService.

Ejemplos:

- LeagueWatcher
- CaptureService
- VisionService
- VoiceService
- OverlayService

Cada servicio debe ejecutarse en su propio hilo.

No debe haber múltiples while True repartidos por el proyecto.

---

# LeagueWatcher

Responsabilidad:

Detectar el estado de League of Legends.

No captura imágenes.

No analiza IA.

No reproduce voz.

No muestra overlay.

Únicamente informa eventos.

---

# WindowService

Responsabilidad:

Obtener:

- HWND
- resolución
- posición
- ventana activa
- minimizada

No debe detectar estados del juego.

---

# CaptureService

Responsabilidad:

Capturar imágenes únicamente durante una partida.

No debe guardar estado del juego.

No debe conocer Qwen.

---

# Vision

Toda interacción con modelos de IA debe pasar por una interfaz.

Nunca acceder directamente a llama.cpp desde el resto del proyecto.

Ejemplo:

```
VisionProvider

↓

QwenProvider

↓

llama.cpp
```

Así será posible reemplazar Qwen por GPT, Gemini u otro modelo.

---

# CoachEngine

Responsabilidad:

Transformar:

- datos de League API
- datos visuales
- memoria

en recomendaciones.

Nunca acceder directamente al overlay.

Nunca acceder directamente al TTS.

---

# Event Bus

Debe implementarse antes de conectar módulos.

Los servicios no deben llamarse entre sí.

Ejemplo:

LeagueWatcher

↓

MATCH_STARTED

↓

CaptureService

↓

FRAME_CAPTURED

↓

Vision

↓

ADVICE_READY

↓

Voice

↓

Overlay

---

# League Client API

Debe ser la fuente principal de verdad.

No depender únicamente del análisis visual.

Utilizar visión únicamente para obtener información que la API no proporciona.

Ejemplos:

- minimapa
- posiciones visibles
- wards
- teamfights
- contexto visual

---

# IA

Modelo objetivo:

Qwen2.5-VL

Ejecutándose mediante:

llama.cpp

No utilizar APIs externas.

Todo debe funcionar localmente.

---

# TTS

Motor:

Piper

No depender de ElevenLabs.

No depender de OpenAI.

---

# Overlay

Será implementado con:

PySide6

No debe bloquear la aplicación.

---

# Objetivo inmediato (Sprint actual)

Implementar la infraestructura.

Orden:

1. Config
2. Logger
3. Application
4. StateMachine
5. ApplicationContext
6. BackgroundService
7. LeagueWatcher
8. EventBus
9. WindowService
10. CaptureService

NO comenzar todavía con:

- IA
- Overlay
- Coach
- Voice

---

# Estilo de código

Siempre:

- Type hints
- Docstrings
- Clases pequeñas
- Una responsabilidad por clase
- Sin print()
- Todo mediante logger
- Sin variables globales

---

# Qué NO hacer

No cambiar la arquitectura.

No simplificar el proyecto.

No volver a una arquitectura basada en scripts.

No colocar lógica importante en main.py.

No utilizar while True fuera de BackgroundService.

No conectar módulos directamente.

No eliminar capas de abstracción.

---

# Próximo paso

El siguiente archivo a implementar es:

backend/app/application_context.py

Luego:

backend/services/event_bus.py

Después:

LeagueWatcher utilizando ApplicationContext.