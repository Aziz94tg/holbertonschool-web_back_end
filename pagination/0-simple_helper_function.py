#!/usr/bin/env python3
"""
Simple helper function for pagination.

This module provides a utility function to calculate index ranges
for pagination purposes.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The page number (1-indexed)
        page_size (int): The number of items per page
 
    Returns:
        tuple: A tuple containing the start index and end index
               for the given pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
