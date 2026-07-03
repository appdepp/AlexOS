from abc import ABC, abstractmethod

from app.core.cognitive_event import CognitiveEvent


class VectorMemory(ABC):
    """
    Semantic long-term memory interface.

    Implementations may use ChromaDB, FAISS,
    Qdrant or another vector database.
    """

    @abstractmethod
    def store(self, event: CognitiveEvent) -> None:
        """
        Store a CognitiveEvent.
        """
        ...

    @abstractmethod
    def search(self, query: str, limit: int = 5) -> list[CognitiveEvent]:
        """
        Return semantically similar events.
        """
        ...

    @abstractmethod
    def clear(self) -> None:
        """
        Remove all stored events.
        """
        ...
