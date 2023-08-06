#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Normalize the Extracted OWL Query Data """


from baseblock import BaseObject
from rdflib import Graph


class OwlQueryNormalize(BaseObject):
    """ Normalize the Extracted OWL Query Data """

    def __init__(self,
                 graph: Graph):
        """ Change Log

        Created:
            13-Oct-2021
            craigtrim@gmail.com
            *   refactored out of 'owl-data-extract'
                Build Owl2PY dictionary for backwardCompatibilityTypes
        Updated:
            25-May-2022
            craigtrim@gmail.com
            *   refactor into 'askowl' repo
                https://github.com/craigtrim/askowl/issues/1

        Args:
            graph (Graph): an instantiated RDF graph
        """
        BaseObject.__init__(self, __name__)
        self._graph = graph

    def process(self,
                d_results: dict,
                all_subjects: bool = True) -> dict:

        d_normalized = {}

        # Represent all Subjects
        if all_subjects:
            for subject, _, _ in self._graph:
                subject = subject.title().split('#')[-1].strip().lower()
                if subject.startswith('http'):
                    continue  # this is the root entity
                d_normalized[subject] = set()

        # Add Query Results
        for k in d_results:
            d_normalized[k] = d_results[k]

        # # Sort Values
        d_normalized = {k: d_normalized[k] for k in d_normalized
                        if len(d_normalized[k])}

        return d_normalized
