# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict


class Position:
    """ A position in a multilogue discussion. """
    thesis: str                 = ""
    antithesis: str             = ""
    conversation: List[Dict]    = []  # The course of conversation, sequence of statements.

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __call__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def __repr__(self):
        return f"""Position   
            Thesis:  {self.thesis}, 
            Antithesis: {self.thesis}
            """