from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class MemoryItem:
    item_type: str
    content: str
    topic: str = "general"
    importance: int = 1
    confidence: float = 0.5
    source: str = "conversation"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


class MemoryExtractor:
    def extract(self, user_text: str, assistant_text: str = "") -> list[MemoryItem]:
        memories = []

        text = user_text.strip()

        if not text:
            return memories

        lowered = text.lower()

        if "согласен" in lowered or "давай" in lowered:
            memories.append(
                MemoryItem(
                    item_type="decision",
                    content=text,
                    topic="project",
                    importance=3,
                    confidence=0.8,
                )
            )

        if "мне важно" in lowered or "для меня важно" in lowered:
            memories.append(
                MemoryItem(
                    item_type="preference",
                    content=text,
                    topic="personal",
                    importance=4,
                    confidence=0.9,
                )
            )

        if "цель" in lowered or "конечная цель" in lowered:
            memories.append(
                MemoryItem(
                    item_type="goal",
                    content=text,
                    topic="vision",
                    importance=5,
                    confidence=0.9,
                )
            )

        return memories