"""
Schema declarations used for validating the data structure of metadata.
"""

schema_source_data = {
    "type": "object",
    "properties": {
        "mainAuthor": {"type": ["null", "string"]},
        "titleDescription": {"type": "string"},
        "publicationInfo": {"type": "string"},
        "date": {"type": "string"},
        "scale": {"type": "string"},
        "originalSource": {"type": "string"},
        "viewUrl": {"type": "string"},
        "downloadUrl": {"type": "string"},
    },
    "required": [
        "date",
        "downloadUrl",
        "mainAuthor",
        "originalSource",
        "publicationInfo",
        "scale",
        "titleDescription",
        "viewUrl",
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
