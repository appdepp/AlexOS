from app.core.cognitive_event import CognitiveEvent


class StorageManager:
    """
    Unified entry point for long-term memory storage.

    First version stores events in memory only.
    Later versions will connect Vector Memory and Graph Memory.
    """

    def __init__(self):
        self._events: list[CognitiveEvent] = []

    def save_event(self, event: CognitiveEvent) -> None:
        self._events.append(event)

    def all_events(self) -> list[CognitiveEvent]:
        return list(self._events)

    def count(self) -> int:
        return len(self._events)

    def clear(self) -> None:
        self._events.clear()
