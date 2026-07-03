from app.core.cognitive_event import CognitiveEvent
from app.services.chroma_memory import ChromaMemory
from app.services.graph_memory import GraphMemory


class LongTermMemory:
    """
    Unified interface for AlexOS long-term memory.

    Combines:

    - semantic memory (vector)
    - relationship memory (graph)
    """

    def __init__(self):
        self.vector = ChromaMemory()
        self.graph = GraphMemory()

    def store(self, event: CognitiveEvent) -> None:
        self.vector.store(event)

    def search(self, query: str, limit: int = 5) -> list[CognitiveEvent]:
        return self.vector.search(query, limit)

    def clear(self) -> None:
        self.vector.clear()
        self.graph.clear()
