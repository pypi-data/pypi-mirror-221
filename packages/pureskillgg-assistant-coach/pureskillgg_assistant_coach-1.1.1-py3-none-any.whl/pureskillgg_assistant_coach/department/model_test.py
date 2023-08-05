# pylint: disable=missing-docstring
# pylint: disable=unused-import

import os

import pytest
from structlog import get_logger

from .reader_fs import DepartmentReaderFs
from .model import Department


def test_load():
    model = create_test_model()
    model.load()


def test_load_ds_models():
    model = create_test_model()
    model.load()
    model.load_ds_models()


def test_get_ds_model(snapshot):
    model = create_test_model()
    model.load()
    model.load_ds_models()
    snapshot.assert_match(model.get_ds_model("dexter_model_1"))


def test_is_assessment_should_be_true():
    model = create_test_model()
    model.load()
    assert model.is_assignment("dexter_assignment_1")


def test_is_assessment_should_be_false():
    model = create_test_model()
    model.load()
    assert not model.is_assignment("not_an_assessment")


def test_meta(snapshot):
    model = create_test_model()
    model.load()
    snapshot.assert_match(model.meta)


def test_department_name():
    model = create_test_model()
    assert model.department_name == "dexter"


def test_get_title(snapshot):
    model = create_test_model()
    model.load()
    snapshot.assert_match(model.get_title("dexter_assignment_1").get())


def test_get_body(snapshot):
    model = create_test_model()
    model.load()
    snapshot.assert_match(model.get_body("dexter_assignment_1").get())


def test_get_breakdowns(snapshot):
    model = create_test_model()
    model.load()
    data = {
        "dexter_breakdown1": {},
        "dexter_breakdown4": {"round_nums": [1, 2, 3]},
        "dexter_breakdown5": {"var1": "a", "var2": "b"},
    }
    breakdowns = model.get_breakdowns("dexter_assignment_1", data)
    snapshot.assert_match([breakdown.get() for breakdown in breakdowns])


def test_get_resources(snapshot):
    model = create_test_model()
    model.load()
    resources = model.get_resources("dexter_assignment_1")
    snapshot.assert_match([resource.get() for resource in resources])


def test_get_single_resource(snapshot):
    model = create_test_model()
    model.load()
    resource = model.get_single_resource("dexter_resource1")
    snapshot.assert_match(resource.get())


def test_single_resource_with_tags(snapshot):
    model = create_test_model()
    model.load()
    resource = model.get_single_resource("dexter_resource_with_tag")
    matched = resource.tags_match({"tag1": {}, "tag2": {}})
    assert matched is True
    snapshot.assert_match(resource.get())


def test_get_facets(snapshot):
    model = create_test_model()
    model.load()
    facets = model.get_facets("dexter_assignment_1")
    snapshot.assert_match(facets)


def create_test_id():
    return "test-id"


def create_test_model():
    root = os.path.join("fixtures", "assessment")
    return Department(
        department_name="dexter",
        reader=DepartmentReaderFs(root=root),
        create_ds_models=create_ds_models,
        create_id=create_test_id,
        log=get_logger(),
    )


# pylint: disable=unused-argument
def create_ds_models(models, log):
    return DsModels(models)


class DsModels:
    def __init__(self, models):
        self._models = models

    def get_ds_model(self, name):
        return self._models.get(name)
