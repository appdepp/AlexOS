from app.core.cognitive_event import CognitiveEvent
from app.core.memory_extractor import MemoryExtractor


class CognitiveLoop:
    """
    Main processing pipeline of AlexOS.

    Every user message passes through this loop.
    """

    def __init__(self):
        self.memory_extractor = MemoryExtractor()

    def process(self, user_message: str) -> CognitiveEvent:
        event = CognitiveEvent(user_message=user_message)

        memory_items = self.memory_extractor.extract(user_message)

        for item in memory_items:
            if item.item_type == "goal":
                event.goals.append(item.content)

            elif item.item_type == "decision":
                event.decisions.append(item.content)

            elif item.item_type == "preference":
                event.preferences.append(item.content)

            elif item.item_type == "fact":
                event.facts.append(item.content)

            event.importance = max(event.importance, item.importance)
            event.confidence = max(event.confidence, item.confidence)

        return event
