from app.core.cognitive_event import CognitiveEvent


class PerceptionEngine:
    """
    First stage of the Cognitive Loop.

    It analyzes the raw user message and enriches CognitiveEvent.
    """

    def perceive(self, event: CognitiveEvent) -> CognitiveEvent:
        text = event.user_message.strip()
        lowered = text.lower()

        if not text:
            return event

        if "для меня важно" in lowered or "мне важно" in lowered:
            event.preferences.append(text)
            event.importance = max(event.importance, 4)
            event.confidence = max(event.confidence, 0.9)

        if "цель" in lowered or "конечная цель" in lowered:
            event.goals.append(text)
            event.importance = max(event.importance, 5)
            event.confidence = max(event.confidence, 0.9)

        if "согласен" in lowered or "давай" in lowered:
            event.decisions.append(text)
            event.importance = max(event.importance, 3)
            event.confidence = max(event.confidence, 0.8)

        return event
