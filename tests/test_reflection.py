from app.core.cognitive_event import CognitiveEvent
from app.core.reflection import ReflectionEngine


def test_reflection_detects_preference():
    engine = ReflectionEngine()

    event = CognitiveEvent(user_message="Для меня важно использовать граф памяти.")
    event.preferences.append("Для меня важно использовать граф памяти.")
    event.importance = 4

    result = engine.reflect(event)

    assert "Preference detected." in result.reflection
    assert "High importance event." in result.reflection
