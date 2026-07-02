from app.core.llm_manager import LLMManager


def test_prompt_contains_current_message():
    manager = LLMManager()

    context = {
        "current_message": "Привет",
        "recent_context": [],
        "preferences": [],
        "goals": [],
        "decisions": [],
    }

    prompt = manager.build_prompt(context)

    assert "Привет" in prompt
