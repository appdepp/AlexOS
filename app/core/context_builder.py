from app.core.cognitive_event import CognitiveEvent
from app.core.recall import RecallEngine


class ContextBuilder:
    """
    Builds focused context for the LLM.
    First version uses current event + recent working memory.
    """

    def __init__(self, recall_engine: RecallEngine):
        self.recall_engine = recall_engine

    def build(self, event: CognitiveEvent) -> dict:
        return {
            "current_message": event.user_message,
            "recent_context": self.recall_engine.recent_context(limit=5),
            "preferences": event.preferences,
            "goals": event.goals,
            "decisions": event.decisions,
        }
