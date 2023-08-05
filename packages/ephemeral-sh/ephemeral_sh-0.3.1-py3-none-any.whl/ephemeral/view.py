import datetime

from rich import print

from ephemeral.model import Task, Tracker


def show_current_task(tracker: Tracker) -> None:
    if tracker.current_task is not None:
        dt = _convert_to_datetime(tracker.current_task.start_ts)
        print(
            f":heavy_check_mark-emoji:   {tracker.current_task.task} [bold black](since {dt:%Y-%m-%d})[/bold black]"
        )
    else:
        print(":x-emoji:  [bold red]No active task found![/bold red]")


def show_history(tracker: Tracker) -> None:
    if not tracker.history:
        print(":x-emoji:  [bold red]No tasks have been completed![/bold red]")
    for task in tracker.history:
        show_completed_task(task)


def show_completed_task(task: Task) -> None:
    start_dt = _convert_to_datetime(task.start_ts)
    end_dt = _convert_to_datetime(task.end_ts)
    print(f"    {task.task} [bold black]({start_dt:%Y-%m-%d} to {end_dt:%Y-%m-%d})[/bold black]")


def _convert_to_datetime(timestamp: int) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(timestamp)
