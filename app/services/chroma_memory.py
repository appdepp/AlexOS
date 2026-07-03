from app.core.cognitive_event import CognitiveEvent
from app.services.vector_memory import VectorMemory


class ChromaMemory(VectorMemory):
    """
    Temporary in-memory implementation.

    Later this class will use ChromaDB.
    """

    def __init__(self):
        self._events: list[CognitiveEvent] = []

    def store(self, event: CognitiveEvent) -> None:
        self._events.append(event)

    def search(self, query: str, limit: int = 5) -> list[CognitiveEvent]:
        query = query.lower()

        matches = [
            event
            for event in self._events
            if query in event.user_message.lower()
        ]

        return matches[:limit]

    def clear(self) -> None:
        self._events.clear()
