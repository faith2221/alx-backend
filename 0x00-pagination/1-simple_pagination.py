#!/usr/bin/env python3
"""
Pagination dealing with indexes.
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    takes 2 int arguments and returns a tuple of size two containing
    the start and end index corresponding to range of indexes
    to return in a list foor those pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def__init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA-FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns dataset with regard to page number
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data = self.dataset()

        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []
