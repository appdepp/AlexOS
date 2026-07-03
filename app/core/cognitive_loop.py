from app.core.cognitive_event import CognitiveEvent
from app.core.perception import PerceptionEngine
from app.core.working_memory import WorkingMemory
from app.core.recall import RecallEngine
from app.core.context_builder import ContextBuilder
from app.core.reflection import ReflectionEngine
from app.core.llm_manager import LLMManager
from app.services.long_term_memory import LongTermMemory


class CognitiveLoop:
    """
    Main processing pipeline of AlexOS.

    Every user message passes through this loop.
    """

    def __init__(self):
        self.perception = PerceptionEngine()
        self.working_memory = WorkingMemory()
        self.recall = RecallEngine(self.working_memory)
        self.context_builder = ContextBuilder(self.recall)
        self.llm = LLMManager()
        self.reflection = ReflectionEngine()
        self.long_term_memory = LongTermMemory()

    def process(self, user_message: str) -> CognitiveEvent:
        event = CognitiveEvent(user_message=user_message)

        event = self.perception.perceive(event)

        event.context = self.context_builder.build(event)

        event.assistant_response = self.llm.generate(event.context)

        event = self.reflection.reflect(event)

        self.working_memory.add(event)

        self.long_term_memory.store(event)

        return event

