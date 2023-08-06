"""
Schema declarations used for validating the data structure of metadata.
"""

schema_source_data = {
    "type": "object",
    "properties": {
        "assetName": {"type": "string"},
        "Source": {"type": "string"},
        "Caption": {"type": "string"},
        "Title of Work": {"type": "string"},
        "Shelfmark": {"type": "string"},
        "Place and date of production": {"type": "string"},
        "Credit": {"type": "string"},
        "downloadUrl": {"type": "string"},
        "Artist/creator": {"type": "string"},
        "Author": {"type": "string"},
    },
    "required": ["assetName", "downloadUrl"],
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
