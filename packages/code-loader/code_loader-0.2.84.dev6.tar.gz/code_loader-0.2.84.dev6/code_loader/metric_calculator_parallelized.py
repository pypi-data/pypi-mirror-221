# mypy: ignore-errors

import traceback
from dataclasses import dataclass
from typing import Optional, List, Tuple, Dict
from multiprocessing import Process, Queue
import tensorflow as tf

from code_loader.leap_loader_parallelized_base import LeapLoaderParallelizedBase
from code_loader.leaploader import LeapLoader


@dataclass
class MetricSerializableError:
    metric_id: str
    metric_name: str
    leap_script_trace: str
    exception_as_str: str


class MetricCalculatorParallelized(LeapLoaderParallelizedBase):
    def __init__(self, code_path: str, code_entry_name: str, n_workers: Optional[int] = 2,
                 max_samples_in_queue: int = 128) -> None:
        super().__init__(code_path, code_entry_name, n_workers, max_samples_in_queue)

    def _create_and_start_process(self) -> Process:
        process = Process(
            target=MetricCalculatorParallelized._process_func,
            args=(self.code_path, self.code_entry_name, self._inputs_waiting_to_be_process,
                  self._ready_processed_results))
        process.daemon = False
        process.start()
        return process

    @staticmethod
    def _process_func(code_path: str, code_entry_name: str,
                      samples_to_process: Queue, ready_samples: Queue) -> None:
        leap_loader = LeapLoader(code_path, code_entry_name)
        while True:
            metric_id, metric_name, input_arg_name_to_tensor = samples_to_process.get(block=True)
            try:
                with tf.device('/cpu:0'):
                    metric_result = leap_loader.metric_by_name()[metric_name].function(**input_arg_name_to_tensor)
            except Exception as e:
                leap_script_trace = traceback.format_exc().split('File "<string>"')[-1]
                ready_samples.put(MetricSerializableError(metric_id, metric_name, leap_script_trace, str(e)))
                continue

            ready_samples.put((metric_id, metric_result))

    def calculate_metrics(self, input_arg_name_to_tensor_list: List[Tuple[str, str, Dict[str, tf.Tensor]]]):
        return self.start_process_inputs(input_arg_name_to_tensor_list)
