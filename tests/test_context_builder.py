from app.core.cognitive_event import CognitiveEvent
from app.core.working_memory import WorkingMemory
from app.core.recall import RecallEngine
from app.core.context_builder import ContextBuilder


def test_context_builder_builds_context():
    memory = WorkingMemory()
    memory.add(CognitiveEvent(user_message="Первое сообщение"))

    recall = RecallEngine(memory)
    builder = ContextBuilder(recall)

    event = CognitiveEvent(user_message="Текущее сообщение")
    event.preferences.append("Любит локальные AI-системы")

    context = builder.build(event)

    assert context["current_message"] == "Текущее сообщение"
    assert context["recent_context"] == ["Первое сообщение"]
    assert context["preferences"] == ["Любит локальные AI-системы"]
