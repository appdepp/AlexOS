from collections import deque

from app.core.cognitive_event import CognitiveEvent


class WorkingMemory:
    """
    Short-term memory of AlexOS.

    Stores the latest CognitiveEvents.
    """

    def __init__(self, max_events: int = 20):
        self._events = deque(maxlen=max_events)

    def add(self, event: CognitiveEvent):
        self._events.append(event)

    def recent(self):
        return list(self._events)

    def last(self):
        if not self._events:
            return None
        return self._events[-1]

    def clear(self):
        self._events.clear()

    def __len__(self):
        return len(self._events)
