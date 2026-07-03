# AlexOS

> **Understand. Remember. Reason. Evolve.**

A personal cognitive operating system.

---

## Official Boot Command

```
AlexOS! Hola Amigo!
```

This command starts an AlexOS engineering session.

It instructs any AI assistant or developer to synchronize with the project before continuing development.

See:

- docs/BOOT_PROTOCOL.md
- docs/ROADMAP.md
- docs/DEVELOPER_GUIDE.md

---

## Current Status

Current Stable Release:

**v1.8.0**

Current Development Stage:

**v1.9 — Identity Model**

---

## Philosophy

AlexOS is not just another AI assistant.

AlexOS is a Cognitive Operating System designed to:

- Understand
- Remember
- Reason
- Evolve

through continuous interaction with its user.
# Основные принципы

- Local First
- Privacy First
- Open Architecture
- Modular Design
- Git First Development
- Documentation Before Code

---

# Философия разработки

Перед написанием нового кода мы всегда отвечаем на три вопроса:

1. Зачем нужен этот модуль?
2. Как он взаимодействует с остальной системой?
3. Можно ли заменить его в будущем без переписывания проекта?

Сначала архитектура — потом код.

---

# Архитектура

## Core

Отвечает за работу всей системы.

Содержит:

- Config
- LLM
- Prompt Engine
- Memory
- Logger
- Module Manager

---

## Modules

Любая новая возможность подключается как отдельный модуль.

Планируемые модули:

- RAG
- Telegram
- GitHub
- Python Tools
- Browser
- Voice
- Crypto
- Boats
- Calendar
- Gmail

---

## Interfaces

AlexOS не зависит от способа общения.

Интерфейсы:

- Terminal
- Telegram
- Web
- Mobile
- API

---

# LLM

Ядро не должно зависеть от конкретной модели.

Поддерживаемые движки:

- Ollama
- OpenAI
- Anthropic
- LM Studio
- другие совместимые модели

Сегодня используется Ollama.

---

# Roadmap

## v0.1

- [x] Git
- [x] Структура проекта
- [x] Ollama
- [x] Первый локальный чат

## v0.2

- [ ] Core
- [ ] Config
- [ ] LLM Client

## v0.3

- [ ] Memory

## v0.4

- [ ] RAG

## v0.5

- [ ] Python Tools

## v0.6

- [ ] GitHub

## v0.7

- [ ] Telegram

## v0.8

- [ ] Voice

## v0.9

- [ ] Web Interface

## v1.0

- [ ] AlexOS

---

# Долгосрочная цель

Через несколько версий AlexOS должен уметь самостоятельно:

- обновлять себя из Git;
- устанавливать необходимые зависимости;
- запускать тесты;
- выполнять миграции;
- перезапускаться после обновления;
- сообщать владельцу об успешном обновлении.

То есть AlexOS должен постепенно стать системой, которая помогает развивать саму себя.

---

# Структура проекта

```
app/
data/
docs/
logs/
tests/
```

---

---

## Development

Run tests:

```bash
pytest


# Автор

Alex