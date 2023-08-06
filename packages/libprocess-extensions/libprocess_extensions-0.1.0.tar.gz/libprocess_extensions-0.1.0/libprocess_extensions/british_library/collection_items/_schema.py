"""
Schema declarations used for validating the data structure of metadata.
"""

schema_source_data = {
    "type": "object",
    "properties": {
        "item": {
            "type": "object",
            "properties": {
                "Full title": {"type": "string"},
                "Published": {"type": "string"},
                "Locations": {"type": "string"},
                "Created": {"type": "string"},
                "Format": {"type": "string"},
                "Language": {"type": "string"},
                "Creator": {"type": "string"},
                "Usage terms": {"type": "string"},
                "Held by": {"type": "string"},
                "Shelfmark": {"type": "string"},
                "shortDescription": {"type": "string"},
                "Copyright": {"type": "string"},
                "Title": {"type": "string"},
                "Date": {"type": "string"},
                "Duration": {"type": "string"},
                "Publisher": {"type": "string"},
                "Publishers": {"type": "string"},
                "Track/Part": {"type": "string"},
            },
            "required": [],
            "additionalProperties": False,
        },
        "images": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["item"],
    "additionalProperties": False,
}

schema_metadata_entry = {
    "type": "object",
    "properties": {
        "uuid": {"type": "string"},
        "url": {"type": "string"},
        "source": {"type": "string"},
        "idInSource": {"type": "string"},
        "accessDate": {"type": "string"},
        "sourceData": schema_source_data,
    },
    "required": ["accessDate", "idInSource", "source", "sourceData", "url", "uuid"],
    "additionalProperties": False,
}

schema_metadata = {"type": "array", "items": schema_metadata_entry}
