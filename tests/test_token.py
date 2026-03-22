from services.memory_service import  trim_conversation_history

def test_trim_history():
    history = [{"role": "system", "content": "You are AI"}]

    for i in range(15):
        history.append({"role": "user", "content": f"msg{i}"})

    trimmed = trim_conversation_history(history, max_messages=5)

    # 1 system + 5 recent messaged
    assert len(trimmed) == 6
    assert trimmed[0]["role"] == "system"
    assert trimmed[-1]["content"] == "msg14"

