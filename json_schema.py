CURRICULUM_MAP_SCHEMA = """
Return ONLY valid JSON.

Do not include markdown.
Do not include explanations.

Return EXACTLY this JSON structure.

The JSON MUST contain ALL of these top-level keys:

- content_standard
- performance_standard
- formation_standard
- topics

Do NOT omit any key.

If no Formation Standard is provided by the curriculum, generate an appropriate Formation Standard that aligns with the Content Standard and Performance Standard.

NEVER omit "formation_standard".

If the source curriculum does not explicitly provide one, infer an appropriate Formation Standard from the Content Standard and Performance Standard.

{
  "content_standard": "",
  "performance_standard": "",
  "formation_standard": "",

  "topics": [
    {
      "topic": "",

      "resources": [
        ""
      ],

      "integration": {
        "skill_21st": "",
        "vertical_alignment": "",
        "horizontal_alignment": ""
      },

      "rows": [
        {
          "level": "Acquisition",

          "competency": "",

          "enduring_understanding": "",

          "essential_question": "",

          "assessment": [
            ""
          ],

          "activities": [
            ""
          ],

          "core_value": {
            "value": "",
            "reason": ""
          }
        }
      ]
    }
  ]
}
"""