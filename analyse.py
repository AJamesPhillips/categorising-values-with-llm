import requests
from typing import Optional

input_file = "demo.csv"


possible_fields = [
    "first_name",
    "last_name",
    "email",
    "phone_number",
    "address",
    "latitude",
    "longitude",
    "date",
    "year",
    "day_of_week"
]


def analyse():
    start_from_line = 0
    for row in factory_data(start_from_line):
        print(row)
        predictions = []
        for value in row:
            predictions.append(ask_llama3p1_to_categorise_field_value(value))
        print(predictions)
        print()


def read_input_file():
    with open(input_file, "r") as f:
        lines = f.readlines()
    return [line.strip().split(",") for line in lines]


def factory_data(from_line: int):
    data = read_input_file()
    max_rows = len(data)
    start_index = from_line % max_rows
    current_index = start_index

    while True:
        yield data[current_index]
        current_index = (current_index + 1) % max_rows
        if current_index == start_index:
            break


def ask_llama3p1_to_categorise_field_value(field_value: str):
    message = (
        f"Categorise the following field value: {field_value}. " +
        "Please respond with the most likely category from the following list of options: " +
        ", ".join(possible_fields) +
        " You MUST NOT reply with anything other than the category."
    )
    return call_llama3p1(message)


# Global session for connection reuse
_session: Optional[requests.Session] = None


def get_session() -> requests.Session:
    """Get or create a persistent requests session for connection pooling."""
    global _session
    if _session is None:
        _session = requests.Session()
    return _session


def call_llama3p1(message: str, keep_alive: str = "5m"):
    """
    Call llama3.1 via Ollama.

    Args:
        message: The message to send to the model
        keep_alive: How long to keep the model loaded in memory (default "5m")
                   Set to "0s" for immediate unload, or "-1" to never unload
        clear_history: If True, sends only the current message (fresh session).
                      If False, could be extended to maintain history (not yet implemented).

    Returns:
        The model's response text
    """
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llama3.1",
        "messages": [{"role": "user", "content": message}],
        "stream": False,
        "keep_alive": keep_alive  # Keep model in memory for better performance
    }

    session = get_session()
    response = session.post(url, json=payload)
    response.raise_for_status()
    result = response.json()
    return result.get("message", {}).get("content", "")


if __name__ == "__main__":
    analyse()
