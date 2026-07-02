from app.core.memory_extractor import MemoryExtractor


def test_memory_extractor_extracts_preference():
    extractor = MemoryExtractor()

    items = extractor.extract("Для меня важно использовать граф памяти.")

    assert len(items) == 1
    assert items[0].item_type == "preference"
    assert items[0].importance == 4


def test_memory_extractor_extracts_goal():
    extractor = MemoryExtractor()

    items = extractor.extract("Моя конечная цель — чтобы AlexOS понимал меня лучше.")

    assert len(items) == 1
    assert items[0].item_type == "goal"
    assert items[0].importance == 5


def test_memory_extractor_returns_empty_for_empty_text():
    extractor = MemoryExtractor()

    items = extractor.extract("")

    assert items == []
