# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_get_body 1"] = {
    "text": {
        "en": "Elementum eu facilisis sed odio. Suscipit tellus mauris a diam. Sit amet mattis vulputate enim nulla. Facilisi morbi tempus iaculis urna id. Odio ut enim blandit volutpat maecenas volutpat. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus. Turpis egestas integer eget aliquet nibh praesent tristique magna sit. Commodo elit at imperdiet dui. Pellentesque eu"
    }
}

snapshots["test_get_breakdowns 1"] = [
    {
        "body": {
            "text": {
                "en": "Elementum eu facilisis sed odio. Suscipit tellus mauris a diam. Sit amet mattis vulputate enim nulla. Facilisi morbi tempus iaculis urna id. Odio ut enim blandit volutpat maecenas volutpat. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus. Turpis egestas integer eget aliquet nibh praesent tristique magna sit. Commodo elit at imperdiet dui. Pellentesque eu"
            }
        },
        "breakdown": "dexter_breakdown1",
        "format": "text",
        "id": "test-id",
        "sentiment": "positive",
        "title": {"text": {"en": "Template Breakdown Title Positive"}},
    },
    {
        "body": {"text": {"en": "Elementum 1, 2 & 3"}},
        "breakdown": "dexter_breakdown4",
        "format": "text",
        "id": "test-id",
        "sentiment": "positive",
        "title": {"text": {"en": "Template Breakdown Title Positive var"}},
    },
    {
        "body": {"text": {"en": "Lorem ipsum dolor a and b"}},
        "breakdown": "dexter_breakdown5",
        "format": "text",
        "id": "test-id",
        "sentiment": "negative",
        "title": {"text": {"en": "Dexter Breakdown Title - negative var"}},
    },
]

snapshots["test_get_ds_model 1"] = [{"model_name": "bar", "type": "foo"}]

snapshots["test_get_facets 1"] = {
    "dexter_facet_b1": {"shape": "bool", "unit": "boolean"},
    "dexter_facet_b2": {"shape": "bool", "unit": "boolean"},
    "dexter_facet_bl": {"shape": "bool_list", "unit": "boolean"},
    "dexter_facet_eh": {"shape": "enum", "unit": "hit_box"},
    "dexter_facet_ehl": {"shape": "enum_list", "unit": "hit_box"},
    "dexter_facet_es": {"shape": "enum", "unit": "sentiment"},
    "dexter_facet_et": {"shape": "enum", "unit": "team"},
    "dexter_facet_etl": {"shape": "enum_list", "unit": "team"},
    "dexter_facet_ew": {"shape": "enum", "unit": "weapon"},
    "dexter_facet_ewl": {"shape": "enum_list", "unit": "weapon"},
    "dexter_facet_f": {"shape": "float", "unit": "percent"},
    "dexter_facet_fl": {"shape": "float_list", "unit": "percent"},
    "dexter_facet_ia": {"shape": "int", "unit": "armor"},
    "dexter_facet_ial": {"shape": "int_list", "unit": "armor"},
    "dexter_facet_ic": {"shape": "int", "unit": "count"},
    "dexter_facet_icl": {"shape": "int_list", "unit": "count"},
    "dexter_facet_ih": {"shape": "int", "unit": "health"},
    "dexter_facet_ihl": {"shape": "int_list", "unit": "health"},
    "dexter_facet_im": {"shape": "int", "unit": "money"},
    "dexter_facet_iml": {"shape": "int_list", "unit": "money"},
    "dexter_facet_p": {"shape": "player", "unit": "steam_id"},
    "dexter_facet_pl": {"shape": "player_list", "unit": "steam_id"},
}

snapshots["test_get_resources 1"] = [
    {
        "body": {
            "text": {
                "en": "Tellus orci ac auctor augue. Commodo viverra maecenas accumsan lacus vel facilisis. Faucibus turpis in eu mi bibendum. Nullam vehicula ipsum a arcu cursus vitae. Mollis nunc sed id semper risus in hendrerit gravida. Sit amet commodo nulla facilisi nullam vehicula ipsum a. Tortor id aliquet lectus proin nibh nisl condimentum id venenatis. Quisque egestas diam in arcu cursus euismod quis viverra. Nec nam aliquam sem et tortor consequat. In aliquam sem fringilla ut. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. Ligula ullamcorper malesuada proin libero nunc consequat interdum varius sit. Eget mauris pharetra et ultrices neque ornare. Sed cras ornare arcu dui vivamus arcu felis. Ac feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper. Eu volutpat odio facilisis mauris sit amet."
            }
        },
        "format": "text",
        "id": "test-id",
        "label": "dexter-resource1",
        "resource": "dexter_resource1",
        "tags": [],
        "title": {
            "text": {
                "en": "Dexter text title",
                "jp": "Japanese Dexter text title",
                "sp": "Spanish Dexter text title",
            }
        },
    },
    {
        "format": "youtube",
        "id": "test-id",
        "resource": "dexter_resource2",
        "tags": [],
        "title": {"text": {"en": "Dexter youtube video"}},
        "video": {
            "externalId": {"en": "dQw4w9WgXcQ"},
            "text": {"en": "Single video and stuff"},
        },
    },
    {
        "format": "youtube_list",
        "id": "test-id",
        "resource": "dexter_resource3",
        "tags": [],
        "title": {"text": {"en": "Dexter video list"}},
        "videos": [
            {"externalId": {"en": "4kuzBOsuyTY"}, "text": {"en": "Cool video"}},
            {"externalId": {"en": "pfNGYkH7LgU"}, "text": {"en": "More cool video"}},
            {"externalId": {"en": "mBSWIC9Cx_M"}, "text": {"en": "The coolest video"}},
        ],
    },
    {
        "format": "link",
        "id": "test-id",
        "resource": "dexter_resource4",
        "tags": [],
        "title": {"text": {"en": "Dexter link"}},
        "url": {
            "href": {
                "en": "https://blog.counter-strike.net/index.php/category/updates/"
            },
            "text": {"en": "Cool link"},
        },
    },
    {
        "format": "link_list",
        "id": "test-id",
        "resource": "dexter_resource5",
        "tags": [],
        "title": {"text": {"en": "Dexter link"}},
        "urls": [
            {
                "href": {
                    "en": "https://blog.counter-strike.net/index.php/category/updates/"
                },
                "text": {"en": "Cool link"},
            },
            {
                "href": {"en": "http://facebook.com/profile.php?=73322363"},
                "text": {"en": "Your facebook"},
            },
        ],
    },
]

snapshots["test_get_single_resource 1"] = {
    "body": {
        "text": {
            "en": "Tellus orci ac auctor augue. Commodo viverra maecenas accumsan lacus vel facilisis. Faucibus turpis in eu mi bibendum. Nullam vehicula ipsum a arcu cursus vitae. Mollis nunc sed id semper risus in hendrerit gravida. Sit amet commodo nulla facilisi nullam vehicula ipsum a. Tortor id aliquet lectus proin nibh nisl condimentum id venenatis. Quisque egestas diam in arcu cursus euismod quis viverra. Nec nam aliquam sem et tortor consequat. In aliquam sem fringilla ut. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. Ligula ullamcorper malesuada proin libero nunc consequat interdum varius sit. Eget mauris pharetra et ultrices neque ornare. Sed cras ornare arcu dui vivamus arcu felis. Ac feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper. Eu volutpat odio facilisis mauris sit amet."
        }
    },
    "format": "text",
    "id": "test-id",
    "label": "dexter-resource1",
    "resource": "dexter_resource1",
    "tags": [],
    "title": {
        "text": {
            "en": "Dexter text title",
            "jp": "Japanese Dexter text title",
            "sp": "Spanish Dexter text title",
        }
    },
}

snapshots["test_get_title 1"] = {"text": {"en": "Dexter Assignment Title"}}

snapshots["test_meta 1"] = {
    "hash": "09d078e3d6eb92f455bd0ec054dcb77aa8b0983c",
    "version": "v1",
}

snapshots["test_single_resource_with_tags 1"] = {
    "body": {"text": {"en": "ok then"}},
    "format": "text",
    "id": "test-id",
    "resource": "dexter_resource_with_tag",
    "tags": ["tag1", "tag2"],
    "title": {"text": {"en": "testing tags"}},
}
