"""Basic tests for ai_frontier package."""

import pytest
from src.ai_frontier import __version__


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_imports():
    """Test that basic imports work."""
    import src.ai_frontier
    import src.ai_frontier.models
    import src.ai_frontier.utils

    assert src.ai_frontier is not None