import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o-mini")

def count_tokens(messages: list) -> int:
    total = 0
    for msg in messages:
        total += len(encoding.encode(msg["content"]))
    return total