# LOL AI Coach - Roadmap

Estado: En desarrollo

Versión objetivo: v1.0.0

---

# Filosofía

Cada sprint debe terminar con una aplicación funcional.

Nunca desarrollar funcionalidades sin una infraestructura sólida.

No saltar etapas.

---

# Sprint 1 - Infraestructura

Estado: 🟡 En progreso

## Objetivo

Construir la arquitectura base del proyecto.

## Tareas

- [x] Crear repositorio
- [x] Crear estructura de carpetas
- [x] Configuración mediante YAML
- [x] Loader de configuración
- [x] Logger
- [x] StateMachine
- [x] BackgroundService
- [ ] ApplicationContext
- [ ] EventBus
- [ ] Application
- [ ] Documentación inicial

Resultado esperado:

La aplicación inicia correctamente y mantiene sus servicios en segundo plano.

---

# Sprint 2 - League Detection

Estado: ⬜ Pendiente

## Objetivo

Detectar automáticamente el estado del cliente de League.

## Tareas

- [ ] League Client API
- [ ] Detectar cliente abierto
- [ ] Detectar lobby
- [ ] Detectar cola
- [ ] Detectar Champion Select
- [ ] Detectar Loading Screen
- [ ] Detectar partida
- [ ] Detectar fin de partida

Resultado esperado

La aplicación conoce en todo momento el estado de League.

---

# Sprint 3 - Window Service

Estado: ⬜ Pendiente

## Objetivo

Administrar la ventana del juego.

## Tareas

- [ ] Obtener HWND
- [ ] Resolución
- [ ] Posición
- [ ] Monitor
- [ ] Fullscreen
- [ ] Borderless
- [ ] Minimized
- [ ] Foreground

Resultado esperado

Obtener toda la información de la ventana sin capturar imágenes.

---

# Sprint 4 - Capture Service

Estado: ⬜ Pendiente

## Objetivo

Capturar imágenes.

## Tareas

- [ ] MSS
- [ ] Captura completa
- [ ] Captura parcial
- [ ] Captura del minimapa
- [ ] HUD
- [ ] Scoreboard
- [ ] Guardado opcional

Resultado esperado

Captura estable a 1 FPS.

---

# Sprint 5 - Vision

Estado: ⬜ Pendiente

## Objetivo

Integrar Qwen.

## Tareas

- [ ] VisionProvider
- [ ] QwenProvider
- [ ] Cliente llama.cpp
- [ ] PromptBuilder
- [ ] Respuesta JSON
- [ ] Parser

Resultado esperado

Enviar imágenes al modelo.

Recibir JSON estructurado.

---

# Sprint 6 - League Data

Estado: ⬜ Pendiente

## Objetivo

Construir el GameState.

## Datos

- [ ] Campeón
- [ ] Nivel
- [ ] Oro
- [ ] CS
- [ ] Objetos
- [ ] Hechizos
- [ ] Cooldowns
- [ ] Dragones
- [ ] Barón
- [ ] Torres
- [ ] Tiempo
- [ ] KDA

Resultado esperado

Objeto GameState completamente poblado.

---

# Sprint 7 - Decision Engine

Estado: ⬜ Pendiente

## Objetivo

Tomar decisiones.

## Tareas

- [ ] Motor de reglas
- [ ] Priorización
- [ ] Cooldowns
- [ ] Objetivos
- [ ] Rotaciones
- [ ] Teamfights
- [ ] Recall
- [ ] Alertas

Resultado esperado

Generación de consejos sin necesidad del LLM cuando sea posible.

---

# Sprint 8 - Coach Engine

Estado: ⬜ Pendiente

## Objetivo

Fusionar reglas e IA.

Entradas

- League API
- Vision
- Memory

Salida

Consejo único.

Resultado esperado

Coach completamente funcional.

---

# Sprint 9 - Piper

Estado: ⬜ Pendiente

## Objetivo

Síntesis de voz.

## Tareas

- [ ] Cola
- [ ] Prioridades
- [ ] Evitar repetición
- [ ] Cancelación
- [ ] Cooldown

Resultado esperado

El coach habla únicamente cuando corresponde.

---

# Sprint 10 - Overlay

Estado: ⬜ Pendiente

## Objetivo

Interfaz gráfica.

## Tareas

- [ ] Overlay transparente
- [ ] Click-through
- [ ] Alertas
- [ ] Minimap Alerts
- [ ] Indicadores
- [ ] Estado del coach

Resultado esperado

Overlay profesional.

---

# Sprint 11 - Memory

Estado: ⬜ Pendiente

## Objetivo

Dar memoria al coach.

## Tareas

- [ ] Últimos consejos
- [ ] Cooldowns
- [ ] Eventos recientes
- [ ] Historial

Resultado esperado

Evitar recomendaciones repetidas.

---

# Sprint 12 - Optimización

Estado: ⬜ Pendiente

## Objetivo

Reducir latencia.

## Tareas

- [ ] Caché
- [ ] Threads
- [ ] Queue
- [ ] Benchmark
- [ ] Profiling

Objetivo

<300 ms por ciclo.

---

# Sprint 13 - Configuración

Estado: ⬜ Pendiente

## Tareas

- [ ] Profiles
- [ ] Idioma
- [ ] Volumen
- [ ] FPS
- [ ] Modelo
- [ ] Voz

Resultado esperado

Configuración completa desde YAML.

---

# Sprint 14 - Testing

Estado: ⬜ Pendiente

## Objetivo

Cobertura superior al 80%.

---

# Sprint 15 - Packaging

Estado: ⬜ Pendiente

## Objetivo

Distribución.

## Tareas

- [ ] PyInstaller
- [ ] Instalador
- [ ] Setup
- [ ] Auto Update

---

# v1.0

Objetivo

Coach completamente funcional.

Características

- Detección automática de League
- Espera en segundo plano
- Captura inteligente
- Qwen2.5-VL
- Piper
- Overlay
- League Client API
- Motor de reglas
- Memoria
- Configuración
- Logging
- Arquitectura desacoplada

---

# Futuro (v2)

- [ ] Soporte para TFT
- [ ] Soporte para Valorant
- [ ] Soporte para CS2
- [ ] Plugin System
- [ ] Dashboard Web
- [ ] Estadísticas
- [ ] Replay Analysis
- [ ] Entrenamiento personalizado
- [ ] Multi-model AI
- [ ] Auto Updater