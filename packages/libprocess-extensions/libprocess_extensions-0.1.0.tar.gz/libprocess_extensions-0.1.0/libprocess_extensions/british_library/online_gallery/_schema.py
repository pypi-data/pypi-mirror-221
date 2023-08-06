"""
Schema declarations used for validating the data structure of metadata.
"""

schema_source_data = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "Publisher": {"type": "string"},
        "Medium": {"type": "string"},
        "Date": {"type": "string"},
        "Length": {"type": "string"},
        "Width": {"type": "string"},
        "Scale": {"type": "string"},
        "Shelfmark": {"type": "string"},
        "Genre": {"type": "string"},
        "Map scale ratio": {"type": "string"},
        "downloadUrl": {"type": "string"},
    },
    "required": [
        "Date",
        "Genre",
        "Medium",
        "Scale",
        "Shelfmark",
        "downloadUrl",
        "title",
    ],
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
