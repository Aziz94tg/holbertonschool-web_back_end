#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

This module provides a Server class that can handle pagination
even when items are deleted from the dataset between requests.
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
        """Cached dataset
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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hypermedia pagination information with deletion resilience.

        Args:
            index (int): The current start index, default is None
            page_size (int): The number of items per page, default is 10

        Returns:
            Dict: A dictionary containing:
                - index: the current start index of the return page
                - next_index: the next index to query with
                - page_size: the current page size
                - data: the actual page of the dataset

        Raises:
            AssertionError: If index is out of valid range
        """
        indexed_dataset = self.indexed_dataset()

        assert index is None or (isinstance(index, int) and
                                 0 <= index < len(indexed_dataset)), \
            "Index out of range"

        if index is None:
            index = 0

        data = []
        current_index = index
        collected = 0

        # Collect page_size items starting from index, skipping deleted items
        max_index = max(indexed_dataset.keys()) + 1
        while collected < page_size and current_index < max_index:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
                collected += 1
            current_index += 1

        # Find next valid index
        next_index = current_index
        while (next_index < max_index and
               next_index not in indexed_dataset):
            next_index += 1

        # If we've reached the end, next_index should be None equivalent
        if next_index >= max_index:
            next_index = None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
