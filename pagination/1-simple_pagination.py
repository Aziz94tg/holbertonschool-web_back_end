#!/usr/bin/env python3
"""
Simple pagination over a CSV dataset of baby names.
This module defines an index_range helper and a Server class that loads the
CSV once (cached) and returns the correct slice for a requested page.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indices for the given page.

    Given a 1-indexed page number and a page size, compute the zero-based
    start index and the exclusive end index for slicing a sequence.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty dataset cache."""
        self.__dataset: List[List[str]] | None = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset, loading it from CSV on first access."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # skip header row
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return a page of the dataset.

        Args:
            page: 1-indexed page number.
            page_size: number of items per page.

        Returns:
            A list of rows (each row is a list of strings) corresponding to the
            requested page. Returns an empty list if the start index is out of
            range for the dataset.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]
