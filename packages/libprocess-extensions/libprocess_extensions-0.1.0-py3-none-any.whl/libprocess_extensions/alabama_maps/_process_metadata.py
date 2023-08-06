"""
Process metadata.

TODO: check if the following data attributes can be used
- sourceData: publicationInfo, scale, originalSource
"""

import re
from datetime import datetime
from typing import List, Union

from libprocess.typing import (
    ProcessedMetadataEntry,
    TimePoint,
)
from libprocess._utils.image import (
    get_md5_by_uuid,
    get_phash_by_uuid,
    get_shape_by_uuid,
    get_storage_size_by_uuid,
)
from libprocess._utils.language import detect_iso6393
from libquery.utils.jsonl import load_jl
from libquery_extensions.alabama_maps._typing import MetadataEntry, SourceData
from tqdm import tqdm


def get_authors(source_data: SourceData) -> Union[List[str], None]:
    main_author = source_data["mainAuthor"]
    if main_author is None:
        return None

    main_author = main_author.replace("\xa0", " ").rstrip(" ")
    authors = main_author.split(" and ")
    return authors


def get_publish_date(date_str: str) -> Union[TimePoint, None]:
    """Parse the publish date from a string."""

    if len(re.findall(r"\d+", date_str)) == 0:
        return None

    if "," in date_str:
        try:
            date = datetime.strptime(date_str, "%b %d, %Y")
            return {
                "year": int(date.year),
                "month": int(date.month),
                "day": int(date.day),
            }
        except ValueError:
            return {"year": int(date_str.split(" ")[-1])}

    if "." in date_str:
        try:
            date_str = date_str.replace(".", ",")
            date = datetime.strptime(date_str, "%b, %Y")
            return {
                "year": int(date.year),
                "month": int(date.month),
            }
        except ValueError:
            return {"year": int(date_str.split(" ")[-1])}

    return {"year": int(re.findall(r"\d+", date_str)[0])}


def get_languages(source_data: SourceData) -> List[str]:
    language = detect_iso6393(source_data["titleDescription"])
    return None if language is None else [language]


def process(entry: MetadataEntry, img_dir: Union[str, None]) -> ProcessedMetadataEntry:
    """
    Process a metadata entry.
    """

    source_data = entry["sourceData"]

    image_properties = (
        {}
        if img_dir is None
        else {
            "md5": get_md5_by_uuid(entry["uuid"], img_dir),
            "phash": get_phash_by_uuid(entry["uuid"], img_dir),
            "resolution": get_shape_by_uuid(entry["uuid"], img_dir),
            "fileSize": get_storage_size_by_uuid(entry["uuid"], img_dir),
        }
    )

    return {
        "uuid": entry["uuid"],
        "authors": get_authors(source_data),
        "displayName": source_data["titleDescription"],
        "publishDate": get_publish_date(source_data["date"]),
        "viewUrl": source_data["viewUrl"],
        "downloadUrl": source_data["downloadUrl"],
        **image_properties,
        "languages": get_languages(source_data),
        "tags": [],
        "abstract": None,
        "rights": "unknown",
        "source": {
            "name": entry["source"],
            "url": entry["url"],
            "accessDate": entry["accessDate"],
        },
    }


def process_batch(
    metadata_path: str,
    img_dir: Union[str, None],
    uuids: Union[List[str], None] = None,
) -> List[ProcessedMetadataEntry]:
    """
    Process a batch of metadata entries.
    """

    metadata = load_jl(metadata_path)
    processed_metadata = [
        process(d, img_dir)
        for d in tqdm(metadata, desc="Process Metadata Progress")
        if (uuids is None) or (d["uuid"] in uuids)
    ]

    if img_dir is None:
        return processed_metadata
    # Ignore the entries where the phash computation failed,
    # meaning that the corresponding image has not been fetched
    # or the fetched image is corrupted.
    return [d for d in processed_metadata if d["phash"] is not None]
