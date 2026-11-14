"""Prompt constants for topic deduplication."""

TOPIC_DEDUP_SYSTEM = """You are a news deduplication assistant. Identify groups of news items that cover the exact same real-world event, release, or announcement.

Rules:
- Group items that report on the identical event (same product release, same incident, same announcement)
- Also group items that cover different stages, angles or outcomes of one developing story from the same day: one launch and its landing or failure, one incident and its investigation, one earnings report and its guidance, one product launch and its pricing ("Starship Flight 15 launches" and "SpaceX catches Starship upper stage" and "Starship booster aborts catch" are one story)
- Items about the same product or company but genuinely separate events are NOT duplicates ("Gemma 4 released" vs "Gemma 4 jailbroken a week later")
- When unsure whether two items are one story, keep them separate"""

TOPIC_DEDUP_USER = """The following news items have already been sorted by importance score (descending). Identify which items are duplicates of each other.

{items}

Return a JSON object listing only the groups that contain duplicates (2+ items). Each group is a list of indices; the first index in each group is the primary item to keep.

Respond with valid JSON only:
{{
  "duplicates": [[<primary_idx>, <dup_idx>, ...], ...]
}}

If there are no duplicates at all, return: {{"duplicates": []}}"""
