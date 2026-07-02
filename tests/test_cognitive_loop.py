from app.core.cognitive_loop import CognitiveLoop
from app.core.cognitive_event import CognitiveEvent


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

