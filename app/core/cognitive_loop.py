from app.core.cognitive_event import CognitiveEvent
from app.core.perception import PerceptionEngine
from app.core.working_memory import WorkingMemory


class CognitiveLoop:
    """
    Main processing pipeline of AlexOS.

    Every user message passes through this loop.
    """

    def __init__(self):
        self.perception = PerceptionEngine()
        self.working_memory = WorkingMemory()

    def process(self, user_message: str) -> CognitiveEvent:
        event = CognitiveEvent(user_message=user_message)

        event = self.perception.perceive(event)

        self.working_memory.add(event)

        return event
