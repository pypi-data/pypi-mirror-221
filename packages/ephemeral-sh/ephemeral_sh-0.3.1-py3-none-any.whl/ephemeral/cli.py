from typing import Optional

from rich import print
import typer
from typing_extensions import Annotated

from ephemeral import __version__
from ephemeral.model import Task, Tracker
from ephemeral.view import show_current_task, show_history

app = typer.Typer()
tracker = Tracker.load()


def version_callback(value: bool):
    if value:
        print(f"[white not bold]{__package__} {__version__}[/white not bold]")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Annotated[
        Optional[bool],
        typer.Option("--version", callback=version_callback, is_eager=True),
    ] = None,
) -> None:
    """A simple task tracker with a forgetful history"""
    if ctx.invoked_subcommand is not None:
        return

    show_current_task(tracker)
    if tracker.current_task is None:
        print(":information-emoji:   Start tracking with [bold green]ephemeral track[/bold green]")


@app.command()
def track() -> None:
    """start tracking a new task, or replace your current task"""
    if tracker.current_task is not None:
        show_current_task(tracker)
        _ = typer.confirm("    Would you like to complete your current task?", abort=True)
        complete()

    _ = typer.confirm("    Would you like to start tracking a new task?")
    new_task = typer.prompt("    What would you like to track?")
    tracker.update(Task(new_task))
    print(f":heavy_check_mark-emoji:   Now tracking [bold blue]{new_task}[/bold blue]...")
    tracker.save()


@app.command()
def complete() -> None:
    """finish a task and save it in the history"""
    if tracker.current_task is not None:
        print(
            f":tada-emoji:   Completing [bold blue]{tracker.current_task.task}[/bold blue]  :tada-emoji:"
        )
    tracker.update(new_task=None)
    tracker.save()


@app.command()
def history() -> None:
    """display record of completed tasks"""
    show_history(tracker)


@app.command()
def clear() -> None:
    """delete all persisted state"""
    show_current_task(tracker)
    print(
        ":exclamation-emoji:  [bold red]You are about to reset ephemeral to a clean slate[/bold red]"
    )
    _ = typer.confirm("    Would you like to continue?", abort=True)
    tracker.clear()
    print("\n:sparkles-emoji:  [bold blue]Ephemeral has forgotten[/bold blue]  :sparkles-emoji:\n")
    tracker.save()


if __name__ == "__main__":
    app()
