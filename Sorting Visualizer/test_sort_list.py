"""Test module for my sorting algo visualizer


test module
"""

# NOTE Pytest is telling me that "delete" is not working on the canvas, but it is.


import pytest
from tkinter import Tk
from sort_list import SortList


# this makes a test case with None values
@pytest.fixture
def sort_list():
    root = Tk()
    vis_canvas = None
    current_speed = None
    bar_count = None
    return SortList(root, vis_canvas, current_speed, bar_count)


def test_create_new_list(sort_list):
    """see if create_new_list creates a new list"""
    sort_list.create_new_list()
    # check that it is not none
    assert sort_list.bar_list is not None
    # check that the list is of equal length (bar_list to list_length)
    assert len(sort_list.bar_list) == sort_list.list_length


def test_select_sort(sort_list):
    """see if select_sort works"""
    sort_list.bar_list = [4, 2, 5, 1, 3]
    # call select_sort
    sort_list.select_sort()
    # assert correct one
    assert sort_list.bar_list == [1, 2, 3, 4, 5]


def test_bubble_sort(sort_list):
    """see if bubble_sort method works"""
    sort_list.bar_list = [4, 2, 5, 1, 3]
    sort_list.bubble_sort()
    assert sort_list.bar_list == [1, 2, 3, 4, 5]


def test_merge_sort(sort_list):
    """see if merge_sort works"""
    sort_list.bar_list = [4, 2, 7, 1, 5]
    # call merge_sort 
    sort_list.merge_sort()
    # check if the bar_list is sorted correctly
    assert sort_list.bar_list == [1, 2, 4, 5, 7]