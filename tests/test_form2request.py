import lxml.html
import pytest
from parsel import Selector

from formasaurus import build_submission


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        # html input types: bytes, str, HtmlElement, Selector, SelectorList
        (
            {
                "html": b"""<form id="a"></form>""",
                "form_type": "search",
            },
            {
                "form_id": "a",
            },
        ),
        (
            {
                "html": """<form id="a"></form>""",
                "form_type": "search",
            },
            {
                "form_id": "a",
            },
        ),
        (
            {
                "html": lxml.html.fromstring("""<form id="a"></form>"""),
                "form_type": "search",
            },
            {
                "form_id": "a",
            },
        ),
        (
            {
                "html": Selector(text="""<form id="a"></form>"""),
                "form_type": "search",
            },
            {
                "form_id": "a",
            },
        ),
        (
            {
                "html": Selector(text="""<form id="a"></form>""").css("form"),
                "form_type": "search",
            },
            {
                "form_id": "a",
            },
        ),
        # An empty SelectorList triggers a ValueError.
        (
            {
                "html": Selector(text="""<form id="a"></form>""").css("#b"),
                "form_type": "search",
            },
            {
                "exception": ValueError,
            },
        ),
        # No form
        (
            {
                "html": """<html></html>""",
                "form_type": "search",
            },
            {
                "exception": ValueError,
            },
        ),
        # No form matching min_proba
        (
            {
                "html": """<form id="a"></form>""",
                "form_type": "search",
                "min_proba": 1,
            },
            {
                "exception": ValueError,
            },
        ),
        # No form of the specified type
        (
            {
                "html": """<form id="a"></form>""",
                "form_type": "login",
            },
            {
                "exception": ValueError,
            },
        ),
        # Fields without a match are silently dropped.
        (
            {
                "html": """<form id="a"></form>""",
                "form_type": "search",
                "fields": {"search query": "foo"},
            },
            {
                "form_id": "a",
            },
        ),
        # Fields with a match are mapped.
        (
            {
                "html": """<form id="a"><input name="foo"></form>""",
                "form_type": "search",
                "fields": {"search query": "bar"},
            },
            {
                "form_id": "a",
                "data": {"foo": "bar"},
            },
        ),
        # Given 2 matching fields with different probability, the one with the
        # highest probability is mapped.
        (
            {
                "html": """<form id="a"><input name="foo"><input type="text" name="query"></form>""",
                "form_type": "search",
                "fields": {"search query": "bar"},
            },
            {
                "form_id": "a",
                "data": {"query": "bar"},
            },
        ),
        # Submit buttons with a match are returned.
        (
            {
                "html": """<form id="a"><input id="b" type="button" name="submit"></form>""",
                "form_type": "search",
            },
            {
                "form_id": "a",
                "submit_button_id": "b",
            },
        ),
        # Given 2 matching submit buttons with different probability, the one
        # with the highest probability is returned.
        (
            {
                "html": """<form id="a"><input id="b" type="button" name="reset"><input id="c" type="button" name="submit"></form>""",
                "form_type": "search",
            },
            {
                "form_id": "a",
                "submit_button_id": "c",
            },
        ),
    ),
)
def test_build_submission(input, expected):
    if "exception" in expected:
        with pytest.raises(expected["exception"]):
            build_submission(**input)
        return

    form, data, submit_button = build_submission(**input)
    assert expected["form_id"] == form.attrib.get("id")
    assert expected.get("data", {}) == data
    if "submit_button_id" in expected:
        assert expected["submit_button_id"] == submit_button.attrib.get("id")
    else:
        assert submit_button is None
