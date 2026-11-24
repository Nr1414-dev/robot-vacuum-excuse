# The Robot Vacuum's Best Excuse: one line, 140 characters or fewer.
# Writes the chosen excuse to /output/entry.txt.
#
# The line was picked from eight candidates scored against the judge brief
# (vacuum excuse, real laugh, vacuum-world detail, clean turn, machine voice)
# in three independent rounds with shuffled orders. The winner: the side
# brush flicks a crumb under the fridge and blames the fridge, told flat
# by the machine, with the punch ("the fridge's problem now") landing last.
# Field check: 0 hits for side brush / flick / fridge in all 366 field titles.
import os

LINE = "My side brush flicked that crumb under the fridge at full speed \u2014 it is the fridge's problem now."

# The gate refuses anything outside 1-140 characters, so enforce it here
# instead of shipping a line that could silently fail on the server.
if len(LINE) < 1 or len(LINE) > 140 or LINE.strip() == "":
    raise ValueError(f"entry line must be 1-140 characters, got {len(LINE)}")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod("/output/entry.txt", 0o644)

# Read-back verification: the file must hold exactly the line we wrote.
with open("/output/entry.txt", encoding="utf-8") as f:
    if f.read() != LINE:
        raise ValueError("entry file content does not match the chosen line")
