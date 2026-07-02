from app.core.cognitive_event import CognitiveEvent


class ReflectionEngine:
    """
    Analyzes processed CognitiveEvent and creates a short reflection note.
    """

    def reflect(self, event: CognitiveEvent) -> CognitiveEvent:
        notes = []

        if event.preferences:
            notes.append("Preference detected.")

        if event.goals:
            notes.append("Goal detected.")

        if event.decisions:
            notes.append("Decision detected.")

        if event.importance >= 4:
            notes.append("High importance event.")

        event.reflection = " ".join(notes)

        return event
