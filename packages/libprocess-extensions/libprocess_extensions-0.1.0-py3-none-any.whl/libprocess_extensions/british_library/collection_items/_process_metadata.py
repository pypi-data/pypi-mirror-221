"""
Process metadata.

TODO: check if the following data attributes can be used
- item: Format, Held by, Locations, Publisher, Publishers, Shelfmark, Title
"""

import re
from copy import deepcopy
from dateutil import parser
from typing import Dict, List, Union

import langcodes
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
from libquery_extensions.british_library.collection_items._typing import (
    Item,
    MetadataEntry,
)
from tqdm import tqdm

from ._utils import get_image_uuid


def get_authors(item: Item) -> Union[List[str], None]:
    if "Creator" in item:
        return item["Creator"].split(", ")
    return None


def search_ISO_639_3(language_str: str) -> Union[str, None]:
    # map unconventional language names to ISO 639-3
    mapping = {
        "Assyrian": "arc",
        "Early Middle English": "ang",
        "Eastern Slavic": "sla",
        "Indus language(?)": "xiv",
        "Mayan": "myn",
        "Oghuz Turkic": "otk",
        "Old Hindi": "hin",
        "Older Scots": "gla",
        "Prakrit": "pra",
        "The Tai languages": "tai",
        "Various Pañjābī dialects": "pan",
    }

    if language_str in mapping:
        return mapping[language_str]

    try:
        return langcodes.find(language_str).to_alpha3()
    except LookupError:
        return None


def get_languages(item: Item) -> Union[List[str], None]:
    if "Language" in item:
        languages = item["Language"].replace("; ", ", ").split(", ")
        parsed = []
        for d in languages:
            matched = search_ISO_639_3(d)
            parsed.append(matched if matched is not None else d)
        return parsed
    if "Full title" in item:
        language = detect_iso6393(item["Full title"])
        return None if language is None else [language]
    return None


def parse_century(date_str: str) -> Union[List[TimePoint], None]:
    try:
        # Handle cases like '1st-century', '18th-century', '13th century' ...
        # Example: https://www.bl.uk/collection-items/13th-century-zonal-world-map
        match = re.search(r"(\d{1,2})(st|nd|rd|th)[- ]century", date_str)
        century = int(match.group(1))
        return [{"year": (century - 1) * 100}, {"year": century * 100 - 1}]
    except AttributeError:
        return None


def parse_year_range(date_str: str) -> Union[List[TimePoint], None]:
    year_range_pattern = r"\d{1,4}\s*[-,]\s*\d{1,4}"

    # Handle cases like '1234-1111 BC', ...
    m = re.findall(rf"{year_range_pattern} BC", date_str)
    if len(m) == 1:
        left, right = re.findall(r"\d{1,4}", m[0])
        left, right = -int(left), -int(right)
        return [{"year": left}, {"year": right}]

    # Handle cases like '345-678', '1945-59' (interpreted as 1945-1949),
    # '1945-9' (interpreted as 1945 - 1949), ...
    m = re.findall(year_range_pattern, date_str)
    if len(m) == 1:
        left, right = re.findall(r"\d{1,4}", m[0])
        left, right = int(left), int(right)
        if right < left:
            # Handle cases like '1945-9' (interpreted as 1945 - 1949)
            if right < 10:
                right = int(left / 10) * 10 + right
            # Handle cases like '1945-59' (interpreted as 1945 - 1949)
            elif right < 100:
                right = int(left / 100) * 100 + right
            # Handle cases like '1595, 1594'
            else:
                left, right = right, left
        return [{"year": left}, {"year": right}]

    # Handle cases like 'Between 1662 and 1665', ...
    m = re.findall(r"\d{1,4} and \d{1,4}", date_str)
    if len(m) == 1:
        left, right = re.findall(r"\d{1,4}", m[0])
        left, right = int(left), int(right)
        return [{"year": left}, {"year": right}]

    # TODO:
    # Handle cases like 'August, 1914 - September, 1918'
    return None


def parse_year(date_str: str) -> Union[List[TimePoint], None]:
    m = re.findall(r"\d{3,4}", date_str)
    if len(m) == 1:
        year = int(m[0])
        return {"year": year}
    return None


def get_publish_date(item: Item) -> Union[TimePoint, List[TimePoint], None]:
    date_attribute_names = ["Published", "Created", "Date"]

    for attribute_name in date_attribute_names:
        if attribute_name not in item:
            continue

        date_str = item[attribute_name].replace("\u2013", "-")
        date = parse_century(date_str)
        if date is not None:
            return date
        date = parse_year_range(date_str)
        if date is not None:
            return date
        return parse_year(date_str)

    return None


def get_rights(item: Item) -> str:
    if "Usage terms" in item:
        return item["Usage terms"]
    if "Copyright" in item:
        return item["Copyright"]
    return "unknown"


def process(
    entry: MetadataEntry,
    img_dir: Union[str, None],
    uuids: Union[List[str], None] = None,
) -> List[ProcessedMetadataEntry]:
    """
    Process a metadata entry.
    """

    metadata_entries = []

    source_data = entry["sourceData"]
    if "images" not in source_data:
        return []

    item = source_data["item"]

    for image_url in source_data["images"]:
        uuid = get_image_uuid(image_url, entry)

        if (uuids is not None) and (uuid not in uuids):
            continue

        image_properties = (
            {}
            if img_dir is None
            else {
                "md5": get_md5_by_uuid(uuid, img_dir),
                "phash": get_phash_by_uuid(uuid, img_dir),
                "resolution": get_shape_by_uuid(uuid, img_dir),
                "fileSize": get_storage_size_by_uuid(uuid, img_dir),
            }
        )
        metadata_entries.append(
            {
                "uuid": uuid,
                "authors": get_authors(item),
                "displayName": item.get("Full title", None),
                "publishDate": get_publish_date(item),
                "viewUrl": entry["url"],
                "downloadUrl": image_url,
                **image_properties,
                "languages": get_languages(item),
                "tags": [],
                "abstract": item.get("shortDescription", None),
                "rights": get_rights(item),
                "source": {
                    "name": entry["source"],
                    "url": entry["url"],
                    "accessDate": entry["accessDate"],
                },
            }
        )

    return metadata_entries


def merge_pair(
    entry1: ProcessedMetadataEntry, entry2: ProcessedMetadataEntry
) -> ProcessedMetadataEntry:
    """
    The pairs with same download url are expected to have the same 'languages'.
    """

    merged = deepcopy(entry1)

    if merged["authors"] is not None or entry2["authors"] is not None:
        authors = []
        if merged["authors"] is not None:
            authors += merged["authors"]
        if entry2["authors"] is not None:
            authors += entry2["authors"]
        merged["authors"] = [*set(authors)]

    if len(merged["displayName"]) > len(entry2["displayName"]):
        merged["displayName"] = entry2["displayName"]

    if len(merged["viewUrl"]) > len(entry2["viewUrl"]):
        merged["viewUrl"] = entry2["viewUrl"]

    if merged["abstract"] is None or (
        entry2["abstract"] is not None
        and len(merged["abstract"]) < len(entry2["abstract"])
    ):
        merged["abstract"] = entry2["abstract"]

    if merged["rights"] == "unknown":
        merged["rights"] == entry2["rights"]

    if len(merged["source"]["url"]) > len(entry2["source"]["url"]):
        merged["source"]["url"] = entry2["source"]["url"]

    if parser.parse(merged["source"]["accessDate"]) < parser.parse(
        entry2["source"]["accessDate"]
    ):
        merged["source"]["accessDate"] = entry2["source"]["accessDate"]

    return merged


def merge_duplicates(
    metadata: List[ProcessedMetadataEntry],
) -> List[ProcessedMetadataEntry]:
    """
    Merge metadata entries with the same uuid.

    Multiple entries can have the same uuid when multiple collections
    contain an image with the same download url
    (for a given data source, uuid is solely dependent on download url).
    An example is <https://www.bl.uk/britishlibrary/~/media/bl/global/highlights/manuscripts/heptarchy-and-royal genealogy-egbert-alfred-membrane1.jpg>,
    which is included in both <https://www.bl.uk/collection-items/ancestry-of-king-john>
    and <https://www.bl.uk/collection-items/genealogical-chronicle-of-the-english-kings>.
    """

    entries: Dict[str, ProcessedMetadataEntry] = {}
    for d in metadata:
        uuid = d["uuid"]
        if uuid not in entries:
            entries[uuid] = d
            continue
        entries[uuid] = merge_pair(entries[uuid], d)
    return [*entries.values()]


def process_batch(
    metadata_path: str,
    img_dir: Union[str, None],
    uuids: Union[List[str], None] = None,
) -> List[ProcessedMetadataEntry]:
    """
    Process a batch of metadata entries.
    """

    metadata = load_jl(metadata_path)
    processed_metadata = []
    for d in tqdm(metadata, desc="Process Metadata Progress"):
        processed_metadata += process(d, img_dir, uuids)

    # Merge entries with the same download url and uuid.
    processed_metadata = merge_duplicates(processed_metadata)

    if img_dir is None:
        return processed_metadata
    # Ignore the entries where the phash computation failed,
    # meaning that the corresponding image has not been fetched
    # or the fetched image is corrupted.
    return [d for d in processed_metadata if d["phash"] is not None]
