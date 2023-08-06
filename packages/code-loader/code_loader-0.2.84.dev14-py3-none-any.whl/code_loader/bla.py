# mypy: ignore-errors
import traceback
from dataclasses import dataclass
from multiprocessing import Queue
import tensorflow as tf

from code_loader.leaploader import LeapLoader


@dataclass
class MetricSerializableError:
    metric_id: str
    metric_name: str
    leap_script_trace: str
    exception_as_str: str


def _process_func(code_path: str, code_entry_name: str,
                  metrics_to_process: Queue, ready_samples: Queue) -> None:
    import os
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    leap_loader = LeapLoader(code_path, code_entry_name)
    while True:
        metric_id, metric_name, input_arg_name_to_tensor = metrics_to_process.get(block=True)
        try:
            with tf.device('/cpu:0'):
                metric_result = leap_loader.metric_by_name()[metric_name].function(**input_arg_name_to_tensor)
        except Exception as e:
            leap_script_trace = traceback.format_exc().split('File "<string>"')[-1]
            ready_samples.put(MetricSerializableError(metric_id, metric_name, leap_script_trace, str(e)))
            continue

        ready_samples.put((metric_id, metric_result))