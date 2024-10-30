import json
import os
from time import process_time

import pytest

import formasaurus
from formasaurus.classifiers import FormFieldClassifier, _default_model_file_name

FILENAME = _default_model_file_name()


def test_non_existing_model(tmpdir):
    model_path = os.path.join(str(tmpdir), FILENAME)
    field_path = FormFieldClassifier._field_filename(model_path)
    form_path = FormFieldClassifier._form_filename(model_path)

    assert not os.path.exists(model_path)
    assert not os.path.exists(field_path)
    assert not os.path.exists(form_path)

    with pytest.raises(IOError):
        formasaurus.FormFieldClassifier.load(model_path, autocreate=False)

    assert not os.path.exists(model_path)
    assert not os.path.exists(field_path)
    assert not os.path.exists(form_path)


def test_autocreate_model(tmpdir):
    model_path = os.path.join(str(tmpdir), FILENAME)
    field_path = FormFieldClassifier._field_filename(model_path)
    form_path = FormFieldClassifier._form_filename(model_path)

    assert not os.path.exists(model_path)
    assert not os.path.exists(field_path)
    assert not os.path.exists(form_path)

    formasaurus.FormFieldClassifier.load(model_path)

    assert not os.path.exists(model_path)
    assert os.path.exists(field_path)
    assert os.path.exists(form_path)


def test_rebuild_model(tmpdir):
    model_path = os.path.join(str(tmpdir), FILENAME)
    field_path = FormFieldClassifier._field_filename(model_path)
    form_path = FormFieldClassifier._form_filename(model_path)

    formasaurus.FormFieldClassifier.load(model_path)
    field_mtime1 = os.path.getmtime(field_path)
    form_mtime1 = os.path.getmtime(form_path)

    formasaurus.FormFieldClassifier.load(model_path)
    field_mtime2 = os.path.getmtime(field_path)
    form_mtime2 = os.path.getmtime(form_path)

    formasaurus.FormFieldClassifier.load(model_path, rebuild=True)
    field_mtime3 = os.path.getmtime(field_path)
    form_mtime3 = os.path.getmtime(form_path)

    assert field_mtime2 == field_mtime1
    assert field_mtime3 > field_mtime1
    assert form_mtime2 == form_mtime1
    assert form_mtime3 > form_mtime1


def test_save_and_load(tmpdir):
    """Reloading a model from disk should not change the model."""
    model_path = os.path.join(str(tmpdir), FILENAME)

    a_start_time = process_time()

    # Since model_path does not exist yet, this line trains a new model on the
    # spot and saves it into model_path.
    model_a = formasaurus.FormFieldClassifier.load(model_path)

    b_start_time = process_time()
    a_time = b_start_time - a_start_time

    # Loads the model generated and saved above.
    model_b = formasaurus.FormFieldClassifier.load(model_path)

    b_time = process_time() - b_start_time
    assert (
        b_time / a_time < 0.01
    ), "Unserializing takes too long, over 1% of the training time"

    # Make sure both models work, and work the same.
    html = """<form id="a"><input id="b" type="button" name="reset"><input id="c" type="button" name="submit"></form>"""
    forms_a = model_a.extract_forms(html, proba=True)
    forms_b = model_b.extract_forms(html, proba=True)

    def serialize_forms(forms):
        # Exclude unserializable FormElement instances
        forms = [form[1] for form in forms]
        return json.dumps(forms, sort_keys=True)

    assert serialize_forms(forms_a) == serialize_forms(forms_b)

    # Compare some data from the models that might not impact the outcome of
    # extract_forms() above.
    assert (
        model_a.form_classifier.full_type_names
        == model_b.form_classifier.full_type_names
    )
