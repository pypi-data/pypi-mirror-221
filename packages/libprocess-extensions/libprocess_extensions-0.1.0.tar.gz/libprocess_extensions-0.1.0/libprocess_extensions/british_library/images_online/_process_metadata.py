"""
Process metadata.

TODO: check if the following data attributes can be used
- SourceData: Shelfmark, Source
"""

import re
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
from libquery.utils.jsonl import load_jl
from libquery_extensions.british_library.images_online._typing import (
    MetadataEntry,
    SourceData,
)
from tqdm import tqdm


def get_authors(source_data: SourceData) -> Union[List[str], None]:
    if "Author" in source_data:
        return source_data["Author"].split("; ")
    if "Artist/creator" in source_data:
        return source_data["Artist/creator"].split("; ")
    return None


def get_title(source_data: SourceData) -> Union[str, None]:
    if "Title of Work" in source_data:
        return source_data["Title of Work"]
    if "Caption" in source_data:
        return source_data["Caption"]
    return None


def get_publish_date(
    source_data: SourceData,
) -> Union[TimePoint, List[TimePoint], None]:
    if "Place and date of production" not in source_data:
        return None

    place_and_date = source_data["Place and date of production"]

    # Handle cases like '1844 (1846 '
    m = re.findall(r"\d{1,4}\s*[-()[]\s*\d{1,4}", place_and_date)
    if len(m) == 1:
        left, right = re.findall(r"\d{1,4}", m[0])
        return [{"year": int(left)}, {"year": int(right)}]

    m = re.findall(r"between \d{1,4} and \d{1,4}", place_and_date)
    if len(m) == 1:
        left, right = re.findall(r"\d{1,4}", m[0])
        return [{"year": int(left)}, {"year": int(right)}]

    # Handle cases like '18th century'
    m = re.findall(r"(\d{1,2})th[- ]cent", place_and_date)
    if len(m) == 1:
        century = int(m[0])
        return [{"year": (century - 1) * 100}, {"year": century * 100 - 1}]

    m = re.findall(r"\d{4}", place_and_date)
    if len(m) == 1:
        return {"year": int(m[0])}
    if len(m) == 2:
        # Handle cases like 'xxxxxx1846xxxxxxx1844'
        if int(m[0]) > int(m[1]):
            return [{"year": int(m[1])}, {"year": int(m[0])}]
        return [{"year": int(m[0])}, {"year": int(m[1])}]

    m = re.findall(r"\[\d{1,4}[.]*\]", place_and_date)
    if len(m) == 1:
        year = int(re.findall(r"\d{1,4}", m[0])[0])
        return {"year": year}

    return None


def get_rights(source_data: SourceData) -> str:
    if "Shelfmark" in source_data:
        return (
            f'Copyright British Library Board (Shelfmark: {source_data["Shelfmark"]})'
        )
    return "Copyright British Library Board"


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
        "displayName": get_title(source_data),
        "publishDate": get_publish_date(source_data),
        "viewUrl": entry["url"],
        "downloadUrl": entry["sourceData"]["downloadUrl"],
        **image_properties,
        "languages": None,
        "tags": [],
        "abstract": source_data.get("Caption", None),
        "rights": get_rights(source_data),
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
