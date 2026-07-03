from app.core.cognitive_event import CognitiveEvent
from app.services.chroma_memory import ChromaMemory


def test_store_event():
    memory = ChromaMemory()

    event = CognitiveEvent(user_message="AlexOS")

    memory.store(event)

    assert memory.search("AlexOS")[0] == event


def test_search_returns_matching_events():
    memory = ChromaMemory()

    memory.store(CognitiveEvent(user_message="I love AlexOS"))
    memory.store(CognitiveEvent(user_message="Weather today"))

    results = memory.search("AlexOS")

    assert len(results) == 1
    assert results[0].user_message == "I love AlexOS"


def test_clear_memory():
    memory = ChromaMemory()

    memory.store(CognitiveEvent(user_message="Test"))

    memory.clear()

    assert memory.search("Test") == []
