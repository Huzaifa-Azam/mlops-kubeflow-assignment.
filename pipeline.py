import kfp
from kfp import dsl
from kfp.components import load_component_from_file

# Load components
data_extraction_op = load_component_from_file('components/data_extraction.yaml')
data_preprocessing_op = load_component_from_file('components/data_preprocessing.yaml')
model_training_op = load_component_from_file('components/model_training.yaml')
model_evaluation_op = load_component_from_file('components/model_evaluation.yaml')

@dsl.pipeline(
    name='Boston Housing Pipeline',
    description='A pipeline to train and evaluate a model on the Boston housing dataset.'
)
def mlops_pipeline(
    data_url: str = 'https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz' # Dummy URL, component fetches California housing
):
    # Step 1: Data Extraction
    extraction_task = data_extraction_op(
        data_url=data_url
    )
    
    # Step 2: Data Preprocessing
    preprocessing_task = data_preprocessing_op(
        input_csv=extraction_task.outputs['output_csv']
    )
    
    # Step 3: Model Training
    training_task = model_training_op(
        train_csv=preprocessing_task.outputs['train_csv']
    )
    
    # Step 4: Model Evaluation
    evaluation_task = model_evaluation_op(
        test_csv=preprocessing_task.outputs['test_csv'],
        model_pkl=training_task.outputs['model_pkl']
    )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(mlops_pipeline, 'pipeline.yaml')
    print("Pipeline compiled to pipeline.yaml")
