"""
Example tests using xlib-pillars mock provider.

The mock provider allows testing without real API keys.
"""

import pytest
from xlibrary.ai import AIManager


def test_ai_manager_initialization():
    """Test AI Manager can be initialized with mock provider."""
    ai = AIManager(provider="mock", model="latest")
    assert ai.provider == "mock"


def test_mock_ai_request():
    """Test mock AI provider returns responses."""
    ai = AIManager(provider="mock", model="latest")
    response = ai.request("Test message").send()

    assert response is not None
    assert response.content is not None
    assert len(response.content) > 0


def test_mock_conversation():
    """Test mock provider maintains conversation context."""
    ai = AIManager(provider="mock", model="latest")
    conversation = ai.start_conversation()

    response1 = conversation.request("First message").send()
    response2 = conversation.request("Second message").send()

    assert response1 is not None
    assert response2 is not None


# Add your own tests here
