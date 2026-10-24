#!/usr/bin/env python3
"""Check the registries against their schemas.

    python3 scripts/validate_registries.py

Exits 1 if a decision or release record breaks its schema (including an
unknown field or an empty required string), if an id is used twice, if a YAML
mapping repeats a key, or if a release record lacks a field in the registry's
required_fields. Needs the versions in scripts/requirements.txt.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


class UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader that refuses a mapping with a repeated key.

    PyYAML otherwise keeps the last value, so a second `status:` in a record
    would pass silently.
    """


def _mapping_without_duplicates(loader, node, deep=False):
    keys = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in keys:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        keys.add(key)
    return loader.construct_mapping(node, deep)


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping_without_duplicates
)


def load(path: str):
    text = (ROOT / path).read_text()
    return json.loads(text) if path.endswith(".json") else yaml.load(text, Loader=UniqueKeyLoader)


def check(records: list[dict], schema: dict, key: str, kind: str) -> list[str]:
    errors = []
    validator = Draft202012Validator(schema)
    for record in records:
        for err in validator.iter_errors(record):
            errors.append(f"{kind} {record.get(key, '?')}: {err.message}")
    for rid, n in Counter(r.get(key) for r in records).items():
        if n > 1:
            errors.append(f"{kind} id {rid} is used {n} times")
    return errors


def main() -> int:
    try:
        return run()
    except yaml.YAMLError as err:
        print(err, file=sys.stderr)
        return 1


def run() -> int:
    decisions = load("registries/DECISION_REGISTRY.yaml")["decisions"]
    releases = load("registries/RELEASE_REGISTRY.yaml")
    errors = check(decisions, load("schemas/decision-record.schema.json"), "id", "decision")
    errors += check(releases["records"], load("schemas/release-record.schema.json"), "release_id", "release")
    for record in releases["records"]:
        missing = [f for f in releases["required_fields"] if f not in record]
        if missing:
            errors.append(f"release {record.get('release_id', '?')}: missing {', '.join(missing)}")
    for line in errors:
        print(line, file=sys.stderr)
    print(f"{len(decisions)} decisions, {len(releases['records'])} releases, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
