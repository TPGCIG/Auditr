import sys
import tiktoken # type: ignore

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)

def main():
    paragraph = input("Paragraph: ")
    token_count = count_tokens(paragraph)

    print(f"Token count: {token_count}")

if __name__ == "__main__":
    main()
