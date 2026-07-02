from app.core.cognitive_event import CognitiveEvent


class CognitiveLoop:
    """
    Main processing pipeline of AlexOS.

    Every user message passes through this loop.
    """

    def process(self, user_message: str) -> CognitiveEvent:

        event = CognitiveEvent(user_message=user_message)

        #
        # Future stages
        #

        # Perception
        # Understanding
        # Memory Classification
        # Recall
        # Context Builder
        # LLM
        # Reflection

        return event
