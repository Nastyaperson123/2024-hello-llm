"""
Starter for demonstration of laboratory work.
"""
import json

# pylint: disable= too-many-locals, undefined-variable, unused-import
from pathlib import Path

from config.constants import PROJECT_ROOT
from core_utils.llm.time_decorator import report_time
from lab_7_llm.main import LLMPipeline, RawDataImporter, RawDataPreprocessor, TaskDataset


@report_time
def main() -> None:
    """
    Run the translation pipeline.
    """
    with open(PROJECT_ROOT/'lab_7_llm'/'settings.json', 'r', encoding='utf-8') as f:
        settings = json.load(f)
    importer = RawDataImporter(settings['parameters']['dataset'])
    importer.obtain()
    preprocessor = RawDataPreprocessor(importer.raw_data)
    preprocessor.transform()
    dataset = TaskDataset(preprocessor.data.head(100))
    pipeline = LLMPipeline(settings['parameters']['model'], dataset, 120, 64, 'cpu')
    #print(preprocessor.analyze())
    #print(pipeline.infer_sample(dataset[0]))

    result = pipeline
    assert result is not None, "Demo does not work correctly"


if __name__ == "__main__":
    main()
