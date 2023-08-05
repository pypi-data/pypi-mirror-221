from uuid import uuid4

from .translation import Translation


class Breakdown:
    def __init__(self, properties, data=None, *, create_id=uuid4):
        self.resource_labels = properties.pop("resources", [])
        self.features = Translation(properties, data)
        self._create_id = create_id
        self.breakdown = properties.get("breakdown")
        self.sentiment = properties.get("sentiment")

    def get(self):
        return {
            "id": str(self._create_id()),
            **self.features.get(),
        }


def create_breakdown(breakdown, data=None, /, *, create_id=uuid4):
    return Breakdown(breakdown, data, create_id=create_id)
