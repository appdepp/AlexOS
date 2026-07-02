from app.core.cognitive_event import CognitiveEvent
from app.core.perception import PerceptionEngine


def test_perception_detects_preference():
    engine = PerceptionEngine()
    event = CognitiveEvent(user_message="Для меня важно использовать граф памяти.")

    result = engine.perceive(event)

    assert len(result.preferences) == 1
    assert "граф памяти" in result.preferences[0].lower()
    assert result.importance >= 4
    assert result.confidence >= 0.9


def test_perception_detects_goal():
    engine = PerceptionEngine()
    event = CognitiveEvent(user_message="Моя конечная цель — построить AlexOS.")

    result = engine.perceive(event)

    assert len(result.goals) == 1
    assert result.importance >= 5


def test_perception_detects_decision():
    engine = PerceptionEngine()
    event = CognitiveEvent(user_message="Согласен, делаем Context First.")

    result = engine.perceive(event)

    assert len(result.decisions) == 1
    assert result.importance >= 3
