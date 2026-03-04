import time
import re

def score_response(text: str, response_time: float) -> int:
    """
    Returns a score where higher = "more likely human" (very crude heuristics).
    """
    score = 0
    t = text.strip()

    # Timing heuristic: humans usually don't reply instantly
    if response_time < 0.7:
        score -= 2
    elif response_time < 2.0:
        score += 1
    else:
        score += 2

    # Length heuristic
    if len(t) < 3:
        score -= 2
    elif len(t) < 10:
        score += 0
    else:
        score += 1

    # Variety heuristic: humans use punctuation and mixed casing more often
    if any(p in t for p in ".!?"):
        score += 1
    if re.search(r"[A-Z]", t) and re.search(r"[a-z]", t):
        score += 1

    # "Bot-ish" patterns (very simplistic)
    if re.fullmatch(r"(yes|no|ok|okay|sure|idk|i don't know)\.?", t.lower()):
        score -= 1
    if "as an ai" in t.lower():
        score -= 3

    # Emoji / slang often appears in casual human chat (not always)
    if re.search(r"[:;][)D]|😂|😭|😅|🔥|💀", t):
        score += 1

    return score


def simple_turing_test():
    print("=== Simple Turing-Test-Style Chat ===")
    print("Answer like normal. At the end, I'll guess if you're human or a bot.\n")

    questions = [
        "Quick warm-up: what's something you did today?",
        "Explain a meme or joke you like (in your own words).",
        "What’s your opinion on pineapple on pizza? (No wrong answers.)",
        "Tell me something mildly annoying about real life."
    ]

    total_score = 0

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q}")
        start = time.time()
        ans = input("You: ")
        end = time.time()

        rt = end - start
        s = score_response(ans, rt)
        total_score += s

        # Small "judge" acknowledgement
        print("(noted)\n")

    print("=== Verdict ===")
    print(f"Total score: {total_score}")

    # Thresholds are arbitrary; tweak as you like.
    if total_score >= 4:
        print("My guess: HUMAN ✅")
    elif total_score <= 0:
        print("My guess: BOT 🤖")
    else:
        print("My guess: UNSURE (could be either) 🤔")

    print("\n(Reality check: this is a toy demo, not a real Turing Test.)")


if __name__ == "__main__":
    simple_turing_test()