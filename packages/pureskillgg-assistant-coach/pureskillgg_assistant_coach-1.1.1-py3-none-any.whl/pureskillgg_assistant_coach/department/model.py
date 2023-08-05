from uuid import uuid4

from .breakdown import create_breakdown
from .resource import create_resource
from .translation import Translation


class Department:
    def __init__(
        self, *, department_name, reader, create_ds_models, log, create_id=uuid4
    ):
        self.department_name = department_name
        self.meta = {}
        self._create_ds_models = create_ds_models
        self._assessments = None
        self._assignments = None
        self._ds_models = None
        self._reader = reader
        self._create_id = create_id
        self._log = log.bind(model="department", department=department_name)

    def load(self):
        self._assessments = self._reader.get_assessments(self.department_name)
        self._assignments = self._assessments.keys()
        self.meta = self._reader.get_meta()

    def load_ds_models(self):
        models = self._reader.get_models(self.department_name)
        self._ds_models = self._create_ds_models(models=models, log=self._log)

    def get_ds_model(self, model_name, /):
        return self._ds_models.get_ds_model(model_name)

    def is_assignment(self, name, /):
        return name in self._assessments

    def get_title(self, name, /):
        title = self._assessments.get(name, {}).get("title")
        return Translation(title)

    def get_body(self, name, /):
        body = self._assessments.get(name, {}).get("body")
        return Translation(body)

    def get_breakdowns(self, name, data, /):
        breakdowns = self._assessments.get(name, {}).get("breakdowns")
        labels = [breakdown["breakdown"] for breakdown in breakdowns]
        for label in data:
            if label not in labels:
                raise RuntimeError(f'No breakdown called "{label}" in "{name}"')
        return [
            self._create_breakdown(breakdown, data.get(breakdown["breakdown"]))
            for breakdown in breakdowns
            if breakdown["breakdown"] in data
        ]

    def get_resources(self, name, /):
        resources = self._assessments.get(name, {}).get("resources")
        return [self._create_resource(resource) for resource in resources]

    def get_single_resource(self, resource_label):
        return self._create_resource(
            {
                "resource": resource_label,
                **self._reader.get_resource(self.department_name, resource_label),
            }
        )

    def get_facets(self, name, /):
        return self._assessments.get(name, {}).get("facets")

    def _create_resource(self, properties, /):
        return create_resource(properties, create_id=self._create_id)

    def _create_breakdown(self, properties, data, /):
        return create_breakdown(properties, data, create_id=self._create_id)
