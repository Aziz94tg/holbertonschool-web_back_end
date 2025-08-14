#!/usr/bin/env python3
"""
Pagination helper utilities.
This module provides small helper functions used to compute index ranges for paginated datasets.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute start and end indices for pagination.
    
    Given a page number (1-indexed) and a page size, return a tuple of the
    form (start_index, end_index) suitable for slicing a list or sequence.
    
    Args:
        page: The current page number.
        page_size: The number of items per page.
    
    Returns:
        A tuple (start_index, end_index) where:
            - start_index is the index of the first item to include.
            - end_index is the index one past the last item to include.
    
    
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
