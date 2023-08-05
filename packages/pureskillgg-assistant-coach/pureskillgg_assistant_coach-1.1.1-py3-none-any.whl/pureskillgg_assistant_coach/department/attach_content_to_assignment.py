from datetime import datetime
import dateutil.parser
from dateutil import tz


def attach_content_to_assignment(assignment, resources, breakdowns, facets):

    return {
        **assignment,
        "breakdowns": [
            {"breakdown": k, **breakdowns[k]} for k in assignment["breakdowns"]
        ],
        "resources": [
            {"resource": k, **resources[k]}
            for k in assignment["resources"]
            if resource_is_current(resources[k])
        ],
        "facets": {k: facets[k] for k in assignment["facets"]},
    }


def resource_is_current(resource):
    if "createdAt" not in resource:
        return True
    return dateutil.parser.isoparse(resource["createdAt"]) < datetime.now(
        tz.gettz("UTC")
    )
