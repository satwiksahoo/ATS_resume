from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir : Path
    data_source : Path


@dataclass
class DataTransformationConfig:
    root_dir : Path
    train_path : Path
    test_path : Path
    transformed_train_path : Path
    transformed_test_path : Path
    model_name  : Path
    tokenizer_name : Path

@dataclass
class ModelTrainerConfig:
    root_dir: str
    transformed_train_path: str
    transformed_test_path: str
    trained_model_artifact_path: str
    output_dir: str
    eval_strategy: str
    save_strategy: str
    learning_rate: float
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    num_train_epochs: int
    weight_decay: float
    logging_dir: str
    logging_steps: int
    save_total_limit: int
    load_best_model_at_end: bool
    metric_for_best_model: str
    greater_is_better: bool
    warmup_ratio: float
    lr_scheduler_type: str
    gradient_accumulation_steps: int
    fp16: bool
    seed: int
    model_name : str
    model_pusher : str
    artifact_root : str
