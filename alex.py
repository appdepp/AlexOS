import requests
from rich.console import Console

console = Console()

MODEL = "qwen3:4b"
URL = "http://127.0.0.1:11434/api/chat"

messages = [
    {
        "role": "system",
        "content": "Ты Alex AI. Отвечай на русском. Кратко, практично, с конкретными шагами."
    }
]

console.print("[green]Alex AI запущен. Выход: /exit[/green]")

while True:
    text = input("\nТы: ").strip()

    if text.lower() in ["/exit", "exit", "q"]:
        break

    messages.append({"role": "user", "content": text})

    response = requests.post(
        URL,
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=300
    )

    response.raise_for_status()
    answer = response.json()["message"]["content"]

    messages.append({"role": "assistant", "content": answer})

    console.print("\n[cyan]Alex AI:[/cyan]")
    console.print(answer)