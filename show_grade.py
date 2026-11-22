"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "ce052e24525d44e3a27f32a0ea7fc6f4"
GRADE_HASH = "5416944066f5d3fb007fbea3ebbaf9f608e0e6aa6015c16bd7b6f2e85df0b8a3"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
