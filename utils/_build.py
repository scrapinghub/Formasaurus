from pathlib import Path

from formasaurus.classifiers import (
    DEFAULT_DATA_PATH,
    FormFieldClassifier,
    _default_model_file_name,
)

output_path = (
    Path(__file__).parent.parent / "formasaurus" / "data" / _default_model_file_name()
)
ex = FormFieldClassifier.trained_on(DEFAULT_DATA_PATH)
ex.save(output_path)
