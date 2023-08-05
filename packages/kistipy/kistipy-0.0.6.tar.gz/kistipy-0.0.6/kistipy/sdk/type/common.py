from datasets import load_dataset
import multiprocessing
import pandas as pd
from typing import Callable, Dict

from kistipy.sdk.metadata.store import *

class Data(dict):

    def __init__(self, name: str='', split:str='train'):
        if name in metadata_store:
            metadata = metadata_store[name]
            self.dataset = load_dataset(metadata['extension'], data_files=metadata['data_files'])[split]
        else:
            self.dataset = load_dataset(name)[split]

    def __getitem__(self, k) -> Dict:
        return self.dataset[k]

    def map(self, function: Callable, num_proc: int=multiprocessing.cpu_count(), load_from_cache_file: bool=False):
        self.dataset = self.dataset.map(function=function, num_proc=num_proc, load_from_cache_file=load_from_cache_file)

    def to_pandas(self) -> pd.DataFrame:
        return self.dataset.to_pandas()
