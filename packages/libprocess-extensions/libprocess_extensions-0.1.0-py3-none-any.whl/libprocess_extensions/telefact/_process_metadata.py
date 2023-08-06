"""
Process metadata.
"""

from typing import List, Union

from libprocess.typing import ProcessedMetadataEntry
from libprocess._utils.image import (
    get_md5_by_uuid,
    get_phash_by_uuid,
    get_shape_by_uuid,
    get_storage_size_by_uuid,
)
from libquery.utils.jsonl import load_jl
from libquery_extensions.telefact._typing import MetadataEntry
from tqdm import tqdm


def process(entry: MetadataEntry, img_dir: Union[str, None]) -> ProcessedMetadataEntry:
    """
    Process a metadata entry.
    """

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
        "authors": entry["sourceData"]["authors"],
        "displayName": f'Telefact-{entry["idInSource"]}',
        "publishDate": entry["sourceData"]["publishDate"],
        "viewUrl": entry["url"],
        "downloadUrl": entry["sourceData"]["downloadUrl"],
        **image_properties,
        "languages": entry["sourceData"]["languages"],
        # 'tags': ['ISOTYPE'],
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
