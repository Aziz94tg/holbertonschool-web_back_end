#!/usr/bin/env python3
"""
Hypermedia pagination over a CSV dataset of baby names.
Builds on simple pagination by returning a dictionary with page metadata.
"""
import csv
import math
from typing import List, Tuple, Optional, Dict, Any


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
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset, loading it from CSV on first access."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]

            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return a page of the dataset.

        Args:
            page: 1-indexed page number.
            page_size: number of items per page .

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return hypermedia-style pagination metadata and data.

        The returned dictionary contains:
            - page_size: length of the returned page (0 if page is empty)
            - page: current page number (1-indexed)
            - data: the list of rows for this page
            - next_page: next page number, or None if no next page
            - prev_page: previous page number, or None if no previous page
            - total_pages: total number of pages in the dataset

        This method reuses get_page for slicing the data.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        total = len(data)
        total_pages = math.ceil(total / page_size) if total else 0

        page_data = self.get_page(page, page_size)
        current_page_size = len(page_data)

        start, end = index_range(page, page_size)
        next_page: Optional[int] = page + 1 if end < total else None
        prev_page: Optional[int] = page - 1 if page > 1 else None

        return {
            "page_size": current_page_size,
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
