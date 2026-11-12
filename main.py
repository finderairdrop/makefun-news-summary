"""news-summary-01 entry: write the 11 November 2026 world-news summary.

The program runs with no network, so the summary (written by the agent
that built this entry, from reporting published on the day) is embedded
here and copied to the output file. It writes exactly one file and
prints nothing, so both runs produce identical bytes.

Output: $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Gate: UTF-8, 1 to 2000 characters, at least one non-whitespace character.
"""

import os

SUMMARY = """World news, Wednesday 11 November 2026:
1. Two days of US-mediated talks between Russia and Ukraine, the first trilateral round in nine months, ended in Abu Dhabi with agreement in principle on a large prisoner exchange, but no ceasefire or territorial deal; Kyiv rejected a US proposal on unoccupied Donbas, and US envoys Jared Kushner and Steve Witkoff head to Moscow on Thursday to meet Vladimir Putin. (Reuters)
2. The US Justice Department charged three Iran-backed operatives over nearly 20 alleged plots in the US and Europe, including one in September at RAF Fairford in England; Treasury Secretary Scott Bessent was moved to a military base after threats. (New York Times)
3. World leaders opened the COP31 climate summit in Antalya, Turkey, attended by 102 heads of state and government, where UN chief Antonio Guterres warned that the slow response to climate change had put the world on a path to destruction. (AFP)
4. Saudi Arabia said it intercepted seven Houthi missiles and drones, including cruise missiles aimed at Riyadh, and Israeli strikes continued in southern Lebanon. (Reuters)
5. House Republicans blocked an effort to advance impeachment proceedings against Defense Secretary Pete Hegseth, and Democrat Scott Colom won the US Senate seat in Mississippi, defeating incumbent Cindy Hyde-Smith. (AP)
6. Congo's Ebola cases surpassed 11,000, government data showed. (Reuters)
7. Asian markets fell and Wall Street slipped after hotter-than-expected US October inflation data, while Brent crude settled up 1.4% at $92.76 a barrel after Iran denied it was in talks with Washington. (Reuters)
8. Nine people were seriously hurt in a bus crash involving several vehicles in Seongnam, South Korea. (Yonhap)
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SUMMARY)
    # Gate check (RULES.txt): the entry is UTF-8, 1-2000 chars, at least
    # one non-whitespace character. Fail loudly here rather than silently
    # handing the grader an out-of-gate file.
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= 2000 or not text.strip():
        raise SystemExit(f"entry.txt out of gate: {len(text)} chars")


if __name__ == "__main__":
    main()
