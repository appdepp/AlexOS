from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CognitiveEvent:
    """
    The central object that moves through the AlexOS Cognitive Loop.
    """

    # Raw input
    user_message: str

    # Understanding
    intent: str = ""
    topic: str = ""

    # Knowledge
    entities: list[str] = field(default_factory=list)
    facts: list[str] = field(default_factory=list)
    goals: list[str] = field(default_factory=list)
    decisions: list[str] = field(default_factory=list)
    preferences: list[str] = field(default_factory=list)
    relationships: list[dict] = field(default_factory=list)

    # Metadata
    importance: int = 1
    confidence: float = 0.5

    # Context
    context: dict = field(default_factory=dict)

    # Result
    assistant_response: str = ""

    # Reflection
    reflection: str = ""

    # Meta
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
