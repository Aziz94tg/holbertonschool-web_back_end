#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
Builds an index -> row mapping so that if rows are deleted between requests,
clients can keep paginating without skipping items.
"""

import csv
import math
from typing import List, Dict, Optional, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize dataset caches for raw and indexed representations."""
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset.

        Loads the CSV once and caches the list of rows (header removed).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # drop header row
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by original position, starting at 0.

        Returns a dictionary mapping row index -> row content. This allows us
        to tolerate deletions: if a key is missing, we skip it when paginating.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()

            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(
            self,
            index: int = None,
            page_size: int = 10) -> Dict[str, Any]:
        """Return a deletion-resilient page starting at a given index.

        Args:
            index: The target starting index (0-based) in the indexed dataset.
            page_size: The number of items to include in the returned page.

        Returns:
            A dictionary with:
                - index: the provided starting index
                - next_index: the index to use for the next page
                - page_size: the count of items actually returned
                - data: the list of rows for this page


        """
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(index, int) and index >= 0

        indexed = self.indexed_dataset()
        if not indexed:

            return {
                "index": index,
                "next_index": index,
                "page_size": 0,
                "data": []}

        max_index = max(indexed.keys())

        assert index <= max_index

        data: List[List[str]] = []
        pointer = index

        while len(data) < page_size and pointer <= max_index:
            if pointer in indexed:
                data.append(indexed[pointer])
            pointer += 1

        result = {
            "index": index,
            "next_index": pointer,
            "page_size": len(data),
            "data": data,
        }
        return result
