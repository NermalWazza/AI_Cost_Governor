import os
import sys
from datetime import datetime
import csv

from dotenv import load_dotenv
from openai import OpenAI

DAILY_LIMIT = 1.0
MODEL = "gpt-5.4-nano"
LOG_FILE = "cost_log.csv"

INPUT_COST_PER_1M = 0.20
OUTPUT_COST_PER_1M = 1.25

load_dotenv()


def get_today_spend():
    if not os.path.exists(LOG_FILE):
        return 0.0

    total = 0.0
    today = datetime.now().date()

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts = datetime.fromisoformat(row["timestamp"])
            if ts.date() == today:
                total += float(row["cost"])

    return total


def log_cost(cost):
    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "cost"])

        writer.writerow([datetime.now().isoformat(), cost])


def estimate_cost(input_tokens, output_tokens):
    return (
        (input_tokens / 1_000_000) * INPUT_COST_PER_1M
        + (output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
    )


def main():
    if len(sys.argv) < 2:
        print('Usage: python main.py "your prompt"')
        return

    prompt = " ".join(sys.argv[1:]).strip()
    if not prompt:
        print("Prompt cannot be empty.")
        return

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Missing OPENAI_API_KEY in .env")
        return

    if get_today_spend() >= DAILY_LIMIT:
        print("Daily budget exceeded. Refusing to run.")
        return

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
    model=MODEL,
    input=f"Be concise. {prompt}",
    max_output_tokens=30,
)

    usage = response.usage
    input_tokens = usage.input_tokens or 0
    output_tokens = usage.output_tokens or 0
    cost = estimate_cost(input_tokens, output_tokens)

    log_cost(cost)

    print(response.output_text)
    print(f"\nInput tokens: {input_tokens}")
    print(f"Output tokens: {output_tokens}")
    print(f"Cost: ${cost:.6f}")
    print(f"Total today: ${get_today_spend():.6f}")


if __name__ == "__main__":
    main()