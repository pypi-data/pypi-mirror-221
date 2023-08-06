# mypy: ignore-errors
import multiprocessing
from typing import Optional, List, Tuple, Dict
from multiprocessing import Process

import multiprocess
import tensorflow as tf

from code_loader.bla import _process_func
from code_loader.leap_loader_parallelized_base import LeapLoaderParallelizedBase

class MetricCalculatorParallelized(LeapLoaderParallelizedBase):
    def __init__(self, code_path: str, code_entry_name: str, n_workers: Optional[int] = 2,
                 max_samples_in_queue: int = 128) -> None:
        super().__init__(code_path, code_entry_name, n_workers, max_samples_in_queue)

    def _create_and_start_process(self) -> Process:
        # multiprocessing.set_start_method('fork', force=True)
        process = Process(
            target=_process_func,
            args=(self.code_path, self.code_entry_name, self._inputs_waiting_to_be_process,
                  self._ready_processed_results))
        process.daemon = True
        process.start()
        return process

    def calculate_metrics(self, input_arg_name_to_tensor_list: List[Tuple[str, str, Dict[str, tf.Tensor]]]):
        return self.start_process_inputs(input_arg_name_to_tensor_list)
