from app.core.cognitive_loop import CognitiveLoop
from app.core.cognitive_event import CognitiveEvent


def test_cognitive_loop_returns_event():
    loop = CognitiveLoop()

    event = loop.process("Я хочу построить AlexOS.")

    assert isinstance(event, CognitiveEvent)
    assert event.user_message == "Я хочу построить AlexOS."
