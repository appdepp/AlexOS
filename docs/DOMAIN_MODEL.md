# AlexOS Domain Model

## Purpose

This document defines the core domain language of AlexOS.

All core components should use the same concepts when working with memory, context, reasoning and learning.

---

## Core Entities

### Owner

The human user of AlexOS.

Main role:

- source of goals;
- source of preferences;
- source of decisions;
- final decision maker.

---

### CognitiveEvent

The central object that moves through the AlexOS cognitive cycle.

It represents one meaningful interaction or event.

Contains:

- raw user message;
- detected intent;
- active topic;
- entities;
- facts;
- goals;
- decisions;
- preferences;
- relationships;
- importance;
- confidence;
- context;
- timestamp;
- source.

---

### Episode

A conversation or meaningful session.

Contains:

- messages;
- topic;
- purpose;
- decisions;
- extracted memories;
- related projects;
- timestamp.

---

### Project

A long-term area of work.

Examples:

- AlexOS;
- MeditationApp;
- Crypto Terminal;
- yacht research;
- data analytics portfolio.

---

### Goal

A desired future state.

Examples:

- build a local AI system;
- create contextual memory;
- connect Telegram;
- add vector memory;
- add graph memory.

---

### Decision

A conclusion that changes project direction.

A decision must store:

- what was decided;
- why it was decided;
- alternatives;
- consequences;
- timestamp;
- related entities.

---

### MemoryItem

A single stored memory unit.

Types:

- fact;
- preference;
- goal;
- decision;
- task;
- idea;
- relationship;
- pattern;
- correction.

---

### Relationship

A connection between entities.

Examples:

- AlexOS uses Ollama;
- Context Engine depends on Cognitive Core;
- Vector Memory supports Recall;
- Graph Memory stores relationships.

---

### ContextKernel

The focused context sent to the LLM.

Includes only information relevant to the current request.

---

### IdentityModel

The evolving model of the owner.

Contains:

- preferences;
- thinking style;
- goals;
- habits;
- repeated patterns;
- strengths;
- weaknesses;
- long-term direction.

---

### Capability

A concrete ability of AlexOS.

Examples:

- call Ollama;
- search memory;
- query GitHub;
- send Telegram messages;
- read files;
- run Python tools.

---

## Core Flow

```text
User Message
    ↓
CognitiveEvent
    ↓
Perception
    ↓
Understanding
    ↓
Memory Classification
    ↓
Recall
    ↓
ContextKernel
    ↓
LLM
    ↓
Reflection
    ↓
Memory Update
