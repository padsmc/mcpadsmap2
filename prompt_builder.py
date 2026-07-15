from prompts import SYSTEM_PROMPT


def build_prompt(data):

    prompt = SYSTEM_PROMPT

    prompt += "\n\nUSER INPUT\n\n"

    prompt += "Content Standard:\n"
    prompt += data["content_standard"]
    prompt += "\n\n"

    prompt += "Performance Standard:\n"
    prompt += data["performance_standard"]
    prompt += "\n\n"

    for index, topic in enumerate(data["topics"], start=1):

        prompt += f"TOPIC {index}\n"
        prompt += f"{topic['topic']}\n\n"

        prompt += "Acquisition Competencies:\n"

        for competency in topic["acquisition"]:
            if competency.strip():
                prompt += f"- {competency}\n"

        prompt += "\n"

        prompt += "Make Meaning Competencies:\n"

        for competency in topic["meaning"]:
            if competency.strip():
                prompt += f"- {competency}\n"

        prompt += "\n"

        prompt += "Transfer Competencies:\n"

        for competency in topic["transfer"]:
            if competency.strip():
                prompt += f"- {competency}\n"

        prompt += "\n"

    return prompt