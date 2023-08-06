# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict


class Position(object):
    """ A position in a multilogue discussion. """

    thesis: str                 = ""
    antithesis: str             = ""
    facts: List[str]            = []
    presuppositions: List[str]  = []

    conversation: List[Dict]    = []  # The course of conversation, sequence of statements.

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            super(Position, self).__init__()

    def __call__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def __repr__(self):
        return f"""Position   
            Thesis:  {self.thesis}, 
            Antithesis: {self.thesis},
            Facts: {self.facts},
            Presuppositions: {self.presuppositions}
            """
