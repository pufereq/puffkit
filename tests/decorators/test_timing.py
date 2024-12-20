import pytest
import time as t
from unittest import mock
from puffkit.decorators.timing import measure_execution_time, Timer


@measure_execution_time
def sample_function(duration: float) -> None:
    """Sample function to test the decorator."""
    t.sleep(duration)


@pytest.mark.parametrize("duration", [0.05, 0.1, 0.15])
def test_measure_execution_time(duration: float) -> None:
    """Test measure_execution_time decorator with different durations."""
    # no way to test the logger output, so we just check if the function runs
    # without errors
    sample_function(duration)


def test_timer_context() -> None:
    """Test Timer context manager."""
    with Timer() as timer:
        t.sleep(0.1)
    assert timer.elapsed >= 0.1


def test_timer_context_edge_case() -> None:
    """Test Timer context manager with zero duration."""
    with Timer() as timer:
        pass
    assert timer.elapsed < 0.01
