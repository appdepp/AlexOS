from app.core.cognitive_event import CognitiveEvent
from app.core.working_memory import WorkingMemory
from app.core.recall import RecallEngine


def test_recall_returns_recent_context():
    memory = WorkingMemory()

    memory.add(CognitiveEvent(user_message="Первое сообщение"))
    memory.add(CognitiveEvent(user_message="Второе сообщение"))

    recall = RecallEngine(memory)

    context = recall.recent_context()

    assert context == ["Первое сообщение", "Второе сообщение"]


def test_recall_respects_limit():
    memory = WorkingMemory()

    for i in range(10):
        memory.add(CognitiveEvent(user_message=str(i)))

    recall = RecallEngine(memory)

    context = recall.recent_context(limit=3)

    assert context == ["7", "8", "9"]
