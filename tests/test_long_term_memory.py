from app.core.cognitive_event import CognitiveEvent
from app.services.long_term_memory import LongTermMemory


def test_store_event():
    memory = LongTermMemory()

    event = CognitiveEvent(user_message="AlexOS")

    memory.store(event)

    assert len(memory.search("AlexOS")) == 1


def test_clear_memory():
    memory = LongTermMemory()

    memory.store(CognitiveEvent(user_message="Test"))

    memory.clear()

    assert memory.search("Test") == []


def test_graph_is_available():
    memory = LongTermMemory()

    memory.graph.add_relationship(
        "AlexOS",
        "uses",
        "ChromaDB",
    )

    assert len(memory.graph.relationships()) == 1
