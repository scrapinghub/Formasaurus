from pathlib import Path

from formasaurus.classifiers import DEFAULT_DATA_PATH, FormFieldClassifier

output_path = Path(__file__).parent.parent / "formasaurus" / "data" / "model"
ex = FormFieldClassifier.trained_on(DEFAULT_DATA_PATH)
ex.save(output_path)
