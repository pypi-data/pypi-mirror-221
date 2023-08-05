from uuid import uuid4

from .translation import Translation


class Resource:
    def __init__(self, properties, *, create_id=uuid4):
        self._tags = properties.pop("tags", [])
        self._flat_tags = []
        self.features = Translation(properties)
        self._create_id = create_id
        self.resource = properties.get("resource")
        self.format = properties.get("format")

        # DEPRECATED
        self.label = properties.get("resource")

    def tags_match(self, assessment_tags):
        matched, flat_tags = tag_matcher(assessment_tags, self._tags)
        if matched:
            self._flat_tags = flat_tags
        return matched

    def get(self):

        return {
            "id": str(self._create_id()),
            **self.features.get(),
            "tags": self._flat_tags,
        }


def create_resource(resource, /, *, create_id=uuid4):
    return Resource(resource, create_id=create_id)


def is_negated_tag(tag):
    return tag.startswith("~")


def tag_matcher(flat_tags: dict, grouped_tags: list) -> (bool, list):
    if len(grouped_tags) == 0:
        return True, []
    tags_that_match = set()
    is_match = False
    for tag_group in grouped_tags:
        is_match = False
        for tag in tag_group:
            if not is_negated_tag(tag):
                if tag in flat_tags:
                    is_match = True
                    tags_that_match.add(tag)
            else:
                if tag[1:] not in flat_tags:
                    is_match = True
                    tags_that_match.add(tag)
        if not is_match:
            return is_match, []
    tags_that_match = list(tags_that_match)
    tags_that_match.sort()
    return is_match, tags_that_match
