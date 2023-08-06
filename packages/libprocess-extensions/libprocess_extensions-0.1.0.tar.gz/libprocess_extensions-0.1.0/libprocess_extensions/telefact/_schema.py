"""
Schema declarations used for validating the data structure of metadata.
"""

schema_time_point = {
    "type": "object",
    "properties": {
        "year": {"type": "integer"},
        "month": {"type": "integer"},
        "day": {"type": "integer"},
    },
    "required": ["day", "month", "year"],
    "additionalProperties": False,
}

schema_source_data = {
    "type": "object",
    "properties": {
        "authors": {"type": "array", "items": {"type": "string"}},
        "publishDate": schema_time_point,
        "viewUrl": {"type": "string"},
        "downloadUrl": {"type": "string"},
        "languages": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["authors", "viewUrl", "downloadUrl", "languages", "publishDate"],
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
