from app.core.working_memory import WorkingMemory


class RecallEngine:
    """
    Retrieves relevant context from available memory sources.
    First version uses only WorkingMemory.
    """

    def __init__(self, working_memory: WorkingMemory):
        self.working_memory = working_memory

    def recent_context(self, limit: int = 5) -> list[str]:
        events = self.working_memory.recent()
        recent_events = events[-limit:]

        return [event.user_message for event in recent_events]
