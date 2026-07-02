from app.core.cognitive_event import CognitiveEvent
from app.core.cognitive_loop import CognitiveLoop


def test_cognitive_loop_returns_event():
    loop = CognitiveLoop()

    event = loop.process("Я хочу построить AlexOS.")

    assert isinstance(event, CognitiveEvent)
    assert event.user_message == "Я хочу построить AlexOS."


def test_cognitive_loop_extracts_preference():
    loop = CognitiveLoop()

    event = loop.process("Для меня важно, чтобы AlexOS использовал граф памяти.")

    assert len(event.preferences) == 1
    assert "граф памяти" in event.preferences[0].lower()
    assert event.importance >= 4
    assert event.confidence >= 0.9


def test_cognitive_loop_saves_event_to_working_memory():
    loop = CognitiveLoop()

    event = loop.process("Для меня важно построить AlexOS.")

    assert len(loop.working_memory) == 1
    assert loop.working_memory.last() == event


def test_cognitive_loop_builds_context():
    loop = CognitiveLoop()

    loop.process("Первое сообщение")
    event = loop.process("Для меня важно построить AlexOS.")

    assert event.context["current_message"] == "Для меня важно построить AlexOS."
    assert "Первое сообщение" in event.context["recent_context"]
    assert len(event.context["preferences"]) == 1


def test_cognitive_loop_adds_reflection():
    loop = CognitiveLoop()

    event = loop.process("Для меня важно использовать граф памяти.")

    assert "Preference detected." in event.reflection
    assert "High importance event." in event.reflection


def test_cognitive_loop_generates_assistant_response():
    loop = CognitiveLoop()

    event = loop.process("Привет")

    assert event.assistant_response != ""
