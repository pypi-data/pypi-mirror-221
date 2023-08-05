import os
import rapidjson

from .attach_content_to_assignment import attach_content_to_assignment


class DepartmentReaderFs:
    def __init__(self, *, root):
        self._root = root
        self._resources = {}

    def get_assessments(self, department_name, /):
        assignments = self._get_data(department_name, "assignments")
        resources = self._get_resources(department_name)
        breakdowns = self._get_data(department_name, "breakdowns")
        facets = self._get_data(department_name, "facets")

        return {
            k: attach_content_to_assignment(v, resources, breakdowns, facets)
            for k, v in assignments.items()
        }

    def get_resource(self, department_name, resource_label):
        return self._get_resources(department_name).get(resource_label)

    def get_models(self, department_name, /):
        return self._get_data(department_name, "models")

    def get_meta(self):
        name = os.path.join(self._root, "meta")
        key = f"{name}.json"
        return get_json(key)

    def _get_data(self, department_name, data_name, /):
        name = os.path.join(self._root, "department", department_name, data_name)
        key = f"{name}.json"
        return get_json(key)

    def _get_resources(self, department_name):
        if self._resources.get(department_name) is None:
            self._resources[department_name] = self._get_data(
                department_name, "resources"
            )
        return self._resources.get(department_name)


def get_json(key):
    with open(key, "r", encoding="utf-8") as file:
        data = rapidjson.load(file)
    return data
