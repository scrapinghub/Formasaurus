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
