CURRICULUM_MAP_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "content_standard": {
            "type": "STRING"
        },
        "performance_standard": {
            "type": "STRING"
        },
        "formation_standard": {
            "type": "STRING"
        },
        "topics": {
            "type": "ARRAY"
        }
    },
    "required": [
        "content_standard",
        "performance_standard",
        "formation_standard",
        "topics"
    ]
}