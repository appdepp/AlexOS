class GraphMemory:
    """
    Stores relationships between entities.

    First implementation uses an in-memory graph.
    Later this can be replaced by a real graph database.
    """

    def __init__(self):
        self._relationships: list[dict] = []

    def add_relationship(self, source: str, relation: str, target: str) -> None:
        self._relationships.append(
            {
                "source": source,
                "relation": relation,
                "target": target,
            }
        )

    def relationships(self) -> list[dict]:
        return list(self._relationships)

    def find_by_source(self, source: str) -> list[dict]:
        return [
            relationship
            for relationship in self._relationships
            if relationship["source"] == source
        ]

    def clear(self) -> None:
        self._relationships.clear()
