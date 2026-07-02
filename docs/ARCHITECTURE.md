# AlexOS Architecture

## Memory Architecture

AlexOS uses three memory layers:

### 1. Vector Memory

Stores semantic representations of documents, conversations, notes and project context.

Purpose:

- semantic search;
- RAG;
- finding related documents;
- retrieving past discussions;
- retrieving project context.

Possible backend:

- ChromaDB

---

### 2. Graph Memory

Stores relationships between entities.

Examples of entities:

- projects;
- people;
- ideas;
- decisions;
- documents;
- tasks;
- technologies;
- vehicles;
- yachts;
- crypto assets.

Examples of relations:

- belongs_to;
- related_to;
- depends_on;
- decided_in;
- discussed_in;
- created_by;
- uses;
- compared_with.

Purpose:

- long-term structured memory;
- understanding relationships;
- project knowledge graph;
- contextual reasoning.

Possible backend:

- SQLite at first;
- Neo4j later if needed.

---

### 3. Context Memory

Builds the final working context for the LLM before every answer.

It combines:

- current user message;
- recent conversation;
- relevant vector search results;
- relevant graph relationships;
- system instructions;
- active project state.

Purpose:

- give the model the right information at the right moment;
- avoid overloading context;
- make AlexOS feel like it remembers what matters.

---

## Memory Flow

```text
User Message
    ↓
Context Builder
    ↓
Vector Memory Search
    ↓
Graph Memory Search
    ↓
Relevant Context
    ↓
LLM
    ↓
Answer
    ↓
Memory Update

---

## Personal Model

AlexOS must maintain a personal model of the owner.

This model is not a single prompt.

It is built from:

- working memory;
- vector memory;
- graph memory;
- knowledge memory;
- decisions;
- projects;
- repeated patterns;
- long-term goals.

The personal model is used by the Context Builder to select the right context before every answer.

Principle:

AlexOS should not store everything equally.

It should learn what matters.

---

## Context-First Architecture

AlexOS is not primarily a multi-agent system.

The core of AlexOS is the Context Engine.

The main task of the system is to understand the current situation, extract the right information from previous conversations, and build a focused context kernel before every LLM call.

A specialized agent is optional.

A correct context is mandatory.

---

## Context Kernel

For every user request, AlexOS must build a context kernel.

The context kernel includes:

- current user message;
- active topic;
- user intent;
- relevant facts;
- relevant past conversations;
- related projects;
- known decisions;
- related graph nodes;
- semantically similar memories;
- stable personal knowledge;
- temporary working memory.

The LLM should receive not all available memory, but only the context that matters for the current task.

---

## Memory Extraction

Every conversation should be analyzed after or during the dialogue.

AlexOS should extract:

- facts;
- goals;
- preferences;
- decisions;
- tasks;
- ideas;
- doubts;
- repeated patterns;
- relationships between entities;
- context in which the information appeared.

Memory without context is dangerous.

A fact should be stored together with:

- source;
- timestamp;
- topic;
- confidence;
- related entities;
- reason why it matters.

---

## Principle

The goal is not to create many agents.

The goal is to create one system that can build the right context for any situation.