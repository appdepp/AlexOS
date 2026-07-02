# Architecture Decision Records

## ADR-001: Hybrid Memory Architecture

### Decision

AlexOS will use a hybrid memory architecture:

- Vector Memory
- Graph Memory
- Context Memory

### Reason

A simple chat history is not enough for a long-term personal AI system.

AlexOS must remember:

- facts;
- projects;
- decisions;
- relationships;
- documents;
- previous conversations;
- user preferences;
- active goals.

Vector memory is good for semantic similarity.

Graph memory is good for relationships and structured knowledge.

Context memory combines both into a working context for the LLM.

### Consequences

AlexOS memory will be more complex than a simple chatbot memory.

However, it will be much more powerful and closer to how a real personal assistant should work.

### Initial implementation

- ChromaDB for vector memory.
- SQLite for graph memory.
- Python Context Builder for context memory.

### Future options

- Neo4j or KuzuDB for graph memory.
- More advanced summarization.
- Automatic entity extraction.
- Automatic relationship extraction.