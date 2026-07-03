from app.core.cognitive_event import CognitiveEvent
from app.services.storage import StorageManager


def test_storage_saves_event():
    storage = StorageManager()
    event = CognitiveEvent(user_message="Привет")

    storage.save_event(event)

    assert storage.count() == 1
    assert storage.all_events()[0] == event


def test_storage_clear():
    storage = StorageManager()
    storage.save_event(CognitiveEvent(user_message="Привет"))

    storage.clear()

    assert storage.count() == 0
