from rich.console import Console

from app.core.llm import LLMManager
from app.core.prompts import SYSTEM_PROMPT


class TerminalInterface:
    def __init__(self):
        self.console = Console()
        self.llm = LLMManager()
        self.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    def run(self):
        self.console.print("[bold green]AlexOS запущен. Выход: /exit[/bold green]")

        while True:
            try:
                user_text = input("\nТы: ").strip()

                if user_text.lower() in ["/exit", "exit", "q", "quit"]:
                    self.console.print("[yellow]AlexOS остановлен.[/yellow]")
                    break

                self.messages.append({"role": "user", "content": user_text})

                answer = self.llm.chat(self.messages)

                self.messages.append({"role": "assistant", "content": answer})

                self.console.print("\n[bold cyan]AlexOS:[/bold cyan]")
                self.console.print(answer)

            except KeyboardInterrupt:
                self.console.print("\n[yellow]AlexOS остановлен.[/yellow]")
                break
            except Exception as error:
                self.console.print(f"[bold red]Ошибка:[/bold red] {error}")
