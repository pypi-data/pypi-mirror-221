# pylint: disable=missing-docstring
# pylint: disable=unused-import

import os

import pytest

from .resource import tag_matcher


def standard_assert(
    output_matched, output_flat_tags, target_matched, target_tag_len, tag_contents=None
):
    assert output_matched is target_matched
    assert len(output_flat_tags) == target_tag_len
    if tag_contents is not None:
        tag_contents = list(tag_contents)
        tag_contents.sort()
        assert tag_contents == output_flat_tags


def test_no_grouped_tags():
    flat_tags = {
        "tag1": {},
        "tag2": {},
        "tag3": {},
    }
    grouped_tags = []
    matched, flat_tags = tag_matcher(flat_tags, grouped_tags)
    standard_assert(matched, flat_tags, True, 0)


def test_no_tag_match():
    flat_tags = {
        "tag1": {},
        "tag2": {},
        "tag3": {},
    }
    grouped_tags = [
        ["tag4"],
    ]
    matched, flat_tags = tag_matcher(flat_tags, grouped_tags)
    standard_assert(matched, flat_tags, False, 0)


def test_single_tag_match():
    flat_tags = {
        "tag1": {},
        "tag2": {},
        "tag3": {},
    }
    grouped_tags = [
        ["tag1"],
    ]
    matched, flat_tags = tag_matcher(flat_tags, grouped_tags)
    standard_assert(matched, flat_tags, True, 1)


def test_multi_group_tag_match():
    flat_tags = {
        "tag1": {},
        "tag2": {},
        "tag3": {},
    }
    grouped_tags = [
        ["tag1", "tag2", "tag3"],
    ]
    matched, flat_tags = tag_matcher(flat_tags, grouped_tags)
    standard_assert(matched, flat_tags, True, 3, tag_contents={"tag1", "tag2", "tag3"})


def test_anti_tag_match():
    flat_tags = {
        "tag1": {},
        "tag2": {},
        "tag3": {},
    }
    grouped_tags = [
        ["~tag4"],
    ]
    matched, flat_tags = tag_matcher(flat_tags, grouped_tags)
    standard_assert(matched, flat_tags, True, 1, tag_contents={"~tag4"})


def test_anti_tag_group_match():
    flat_tags = {
        "tag1": {},
        "tag2": {},
        "tag3": {},
    }
    grouped_tags = [
        ["~tag3", "tag2"],
    ]
    matched, flat_tags = tag_matcher(flat_tags, grouped_tags)
    standard_assert(matched, flat_tags, True, 1, tag_contents={"tag2"})


def test_anti_tag_group_no_match():
    flat_tags = {
        "tag1": {},
        "tag2": {},
        "tag3": {},
    }
    grouped_tags = [
        ["~tag3", "~tag2"],
    ]
    matched, flat_tags = tag_matcher(flat_tags, grouped_tags)
    standard_assert(matched, flat_tags, False, 0)


def test_multiple_groups():
    flat_tags = {
        "tag1": {},
        "tag2": {},
        "tag3": {},
    }
    grouped_tags = [
        ["tag1", "tag2"],
        ["tag2", "tag3"],
        ["tag3", "tag4"],
    ]
    matched, flat_tags = tag_matcher(flat_tags, grouped_tags)
    standard_assert(matched, flat_tags, True, 3, tag_contents={"tag1", "tag2", "tag3"})
