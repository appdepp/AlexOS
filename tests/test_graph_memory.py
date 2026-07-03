from app.services.graph_memory import GraphMemory


def test_add_relationship():
    graph = GraphMemory()

    graph.add_relationship("AlexOS", "uses", "Ollama")

    relationships = graph.relationships()

    assert len(relationships) == 1
    assert relationships[0]["source"] == "AlexOS"
    assert relationships[0]["relation"] == "uses"
    assert relationships[0]["target"] == "Ollama"


def test_find_by_source():
    graph = GraphMemory()

    graph.add_relationship("AlexOS", "uses", "Ollama")
    graph.add_relationship("AlexOS", "uses", "ChromaDB")
    graph.add_relationship("MeditationApp", "uses", "Supabase")

    results = graph.find_by_source("AlexOS")

    assert len(results) == 2


def test_clear_graph():
    graph = GraphMemory()

    graph.add_relationship("AlexOS", "uses", "Ollama")
    graph.clear()

    assert graph.relationships() == []
