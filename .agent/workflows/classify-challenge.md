---
description: Run the challenge classification pipeline without starting the full solving cycle. Useful for quick triage or self-assessment.
---

# /classify-challenge — Classify a CTF Challenge

$ARGUMENTS

---

## Task

This command runs the classification pipeline on a challenge independently. It does NOT start the full Learning Cycle.

### Steps:

1. **Intake**: Collect all provided inputs (description, files, screenshots).
   - If no inputs provided, ask the user: "Descreva o desafio ou anexe os arquivos." / "Describe the challenge or attach the files."

2. **Classify**: Invoke the `challenge-classifier` agent.
   - Analyze text, files (magic bytes, extensions), and images (visible text).
   - Produce the 3-tier classification block (CTF Type / Category / Class / Difficulty / Artifacts / Hypothesis / Confidence).

3. **Present**: Display the classification block to the user.

4. **Stop**: Do NOT proceed to triage or exploitation. If the user wants to continue, suggest using `/start-ctf`.

---

## Usage Examples

```
/classify-challenge
/classify-challenge File attached: mysterious.bin
/classify-challenge Desafio de 200 pontos, categoria não informada
/classify-challenge [screenshot of challenge page]
```

---

## Rules

- **Classification only.** This workflow does not trigger the Learning Cycle.
- **Language follows the user.**
