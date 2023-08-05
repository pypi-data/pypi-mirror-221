from rich import print
import typer

from ephemeral.model import Task

app = typer.Typer()
tracker = Task.load()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """A simple task tracker with a forgetful history"""
    if ctx.invoked_subcommand is not None:
        return

    if tracker.task is None:
        print(
            ":x-emoji:  [bold red]No active task found![/bold red]",
            ":information-emoji:   Start tracking with [bold green]ephemeral track[/bold green]",
            sep="\n",
        )
        return
    show_current_task()


@app.command()
def track() -> None:
    """start tracking a new task, or replace your current task"""
    if tracker.task is not None:
        show_current_task()
        _ = typer.confirm("Would you like to clear your current task?", abort=True)
    new_task = typer.prompt("What would you like to track?")
    tracker.update(new_task)
    print(f":heavy_check_mark-emoji: Now tracking [bold blue]{new_task}[/bold blue]...")


@app.command()
def clear() -> None:
    """delete all persisted satet"""
    show_current_task()
    print(
        ":exclamation-emoji:  [bold red]You are about to reset ephemeral to a clean slate[/bold red]"
    )
    _ = typer.confirm("    Would you like to continue?", abort=True)
    tracker.delete()
    print("\n:sparkles-emoji:  [bold blue]Ephemeral has forgotten[/bold blue]  :sparkles-emoji:\n")


def show_current_task() -> None:
    if tracker.task is not None:
        print(
            f":heavy_check_mark-emoji:   {tracker.task} [bold black](since {tracker.dt:%Y-%m-%d})[/bold black]",
        )


if __name__ == "__main__":
    app()
