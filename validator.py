def validate_curriculum(data):

    if not isinstance(data, dict):
        return False, "Root object must be a dictionary."

    required = [
        "content_standard",
        "performance_standard",
        "formation_standard",
        "topics",
    ]

    for field in required:
        if field not in data:
            return False, f"Missing '{field}'."

    if not isinstance(data["topics"], list):
        return False, "'topics' must be a list."

    for topic in data["topics"]:

        if "topic" not in topic:
            return False, "Topic name missing."

        if "rows" not in topic:
            return False, f"Rows missing for topic {topic.get('topic')}."

        if "resources" not in topic:
            return False, f"Resources missing for topic {topic.get('topic')}."

        if "integration" not in topic:
            return False, f"Integration missing for topic {topic.get('topic')}."

    return True, "Valid"