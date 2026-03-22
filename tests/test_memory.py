from services.token_service import count_tokens

def test_token_count():
    messages = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"}
    ]

    tokens = count_tokens(messages)

    assert tokens > 0