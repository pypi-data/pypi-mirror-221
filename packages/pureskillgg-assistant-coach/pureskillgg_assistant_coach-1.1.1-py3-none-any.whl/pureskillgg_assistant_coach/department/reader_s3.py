import boto3
import rapidjson

from .attach_content_to_assignment import attach_content_to_assignment


class DepartmentReaderS3:
    def __init__(self, *, version, bucket, log):
        self._log = log.bind(client="department_reader_s3", bucket=bucket)
        self._bucket = bucket
        self._s3_client = boto3.client("s3")
        self._prefix = "/".join(["csgo", version])
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
        key = f'{"/".join([self._prefix, "meta"])}.json'
        return self._get_json(key)

    def _get_data(self, department_name, data_name, /):
        key = (
            f'{"/".join([self._prefix, "department", department_name, data_name])}.json'
        )
        return self._get_json(key)

    def _get_json(self, key):
        res = self._s3_client.get_object(Bucket=self._bucket, Key=key)
        body = res["Body"].read().decode("utf-8")
        return rapidjson.loads(body)

    def _get_resources(self, department_name):
        if self._resources.get(department_name) is None:
            self._resources[department_name] = self._get_data(
                department_name, "resources"
            )
        return self._resources.get(department_name)
