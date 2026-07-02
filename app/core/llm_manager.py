class LLMManager:
    """
    Builds prompts from cognitive context.
    The real model call will be connected in the next step.
    """

    def generate(self, context: dict) -> str:
        prompt = self.build_prompt(context)
        return prompt

    def build_prompt(self, context: dict) -> str:
        return f"""
Ты — AlexOS.

Текущее сообщение:
{context["current_message"]}

Недавний контекст:
{context["recent_context"]}

Предпочтения:
{context["preferences"]}

Цели:
{context["goals"]}

Решения:
{context["decisions"]}

Ответь как AlexOS.
"""
