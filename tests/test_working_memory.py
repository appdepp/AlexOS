from app.core.cognitive_event import CognitiveEvent
from app.core.working_memory import WorkingMemory


def test_add_event():
    memory = WorkingMemory()

    memory.add(CognitiveEvent(user_message="A"))

    assert len(memory) == 1


def test_last_event():
    memory = WorkingMemory()

    memory.add(CognitiveEvent(user_message="First"))
    memory.add(CognitiveEvent(user_message="Second"))

    assert memory.last().user_message == "Second"


def test_recent_events():
    memory = WorkingMemory()

    for i in range(5):
        memory.add(CognitiveEvent(user_message=str(i)))

    assert len(memory.recent()) == 5


def test_clear():
    memory = WorkingMemory()

    memory.add(CognitiveEvent(user_message="Hello"))
    memory.clear()

    assert len(memory) == 0


def test_max_size():
    memory = WorkingMemory(max_events=3)

    for i in range(10):
        memory.add(CognitiveEvent(user_message=str(i)))

    assert len(memory) == 3
    assert memory.last().user_message == "9"
