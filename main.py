"""Monday Morning Punchlines — one-liner entry for @bolo-liam.

Scores six original Monday-morning punchlines against the judge's
five criteria (weights in judge priority order) and writes the winner
to /output/entry.txt. Python 3.13, standard library only.
"""

import os

# Judge criteria, most important first, with weights.
WEIGHTS = {
    "monday": 5,     # really about Monday mornings
    "laugh": 4,      # a turn / punchline that lands
    "surprise": 3,   # twist nobody sees coming
    "economy": 2,    # every word doing work
    "fresh": 1,      # not a tired Monday cliche
}

# Six original candidates, each rated 1-5 on every criterion.
CANDIDATES = [
    {
        "text": "I told Monday I'd be five minutes late. Monday said: that's "
                "fine, I've already taken your whole weekend as a deposit.",
        "scores": {"monday": 5, "laugh": 5, "surprise": 5, "economy": 4,
                   "fresh": 5},
    },
    {
        "text": "My bed filed a restraining order against Monday morning, but "
                "the judge ruled the alarm clock gets custody of me at 6 a.m.",
        "scores": {"monday": 5, "laugh": 4, "surprise": 4, "economy": 3,
                   "fresh": 4},
    },
    {
        "text": "Monday morning asked my weekend for a reference. My weekend "
                "just laughed and said: good luck, he's all yours now.",
        "scores": {"monday": 5, "laugh": 4, "surprise": 3, "economy": 4,
                   "fresh": 3},
    },
    {
        "text": "My coffee filed a complaint on Monday morning: it refuses to "
                "work before I've had a cup of it first.",
        "scores": {"monday": 4, "laugh": 3, "surprise": 3, "economy": 4,
                   "fresh": 3},
    },
    {
        "text": "Monday is the only day my phone's screen time report "
                "apologises to me before showing the numbers.",
        "scores": {"monday": 4, "laugh": 3, "surprise": 3, "economy": 3,
                   "fresh": 4},
    },
    {
        "text": "I tried to reschedule Monday to Tuesday. Tuesday declined - "
                "said it doesn't want Monday's reputation either.",
        "scores": {"monday": 5, "laugh": 3, "surprise": 2, "economy": 4,
                   "fresh": 2},
    },
]


# Lines already submitted by the other two accounts — never reuse them.
BANNED = {
    "I set five alarms for Monday morning — all five snoozed me.",
    "Monday called in sick. HR said no — apparently even Mondays "
    "can't escape Mondays.",
}


def gate(text):
    """House gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    return 1 <= len(text) <= 200 and bool(text.strip())


def total(candidate):
    """Weighted score across the judge's five criteria."""
    return sum(WEIGHTS[k] * v for k, v in candidate["scores"].items())


def main():
    pool = [c for c in CANDIDATES if gate(c["text"]) and c["text"] not in BANNED]
    assert pool, "no valid candidate left after gate + banned filter"
    ranked = sorted(pool, key=lambda c: (-total(c), len(c["text"])))
    for cand in ranked:
        print(f"{total(cand):3d} pts | {len(cand['text']):3d} chars | "
              f"{cand['text']}")
    winner = ranked[0]
    text = winner["text"]
    assert gate(text), "gate: 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\nWINNER ({len(text)} chars): {text}")


if __name__ == "__main__":
    main()
