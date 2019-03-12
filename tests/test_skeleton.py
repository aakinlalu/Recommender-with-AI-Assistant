#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from recommender_with_ai_assistant.skeleton import fib

__author__ = "Adebayo Akinlalu"
__copyright__ = "Adebayo Akinlalu"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
