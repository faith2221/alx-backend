#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dataset."""
        assert type(index) is int and index >= 0
        assert type(page_size) is int and page_size > 0

        indexed_data = self.indexed_dataset()
        total_items = len(indexed_data)

        if index >= total_items:
            raise AssertionError("Index out of range")

        end_index = index + page_size
        if end_index > total_items:
            end_index = total_items

        data_page = [indexed_data[i] for i in range(index, end_index)]

        next_index = end_index
        if next_index >= total_items:
            next_index = None

        return {
            'index': index,
            'data': data_page,
            'page_size': page_size,
            'next_index': next_index
        }
