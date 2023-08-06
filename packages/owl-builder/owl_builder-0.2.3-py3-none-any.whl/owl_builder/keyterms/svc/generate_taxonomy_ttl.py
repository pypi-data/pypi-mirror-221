#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate Taxonomy Suitable for use in an OWL file """


from collections import defaultdict

from baseblock import BaseObject
from pandas import DataFrame


class GenerateTaxonomyTTL(BaseObject):
    """ Generate Taxonomy Suitable for use in an OWL file """

    def __init__(self):
        """ Change Log

        Created:
            16-Apr-2022
            craigtrim@gmail.com
            *   refactored out of jupyter notebook:
                    GRAFFL-286 Textacy Textrank
                    http://localhost:8888/notebooks/grafflbox/GRAFFL-286%20Textacy%20Textrank.ipynb
                https://github.com/grafflr/graffl-core/issues/286
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                df: DataFrame) -> list:

        def to_entity(some_value: str) -> str:
            return some_value.replace(' ', '_').lower().strip()

        def to_label(some_value: str) -> str:
            tokens = some_value.split(' ')
            tokens = [f"{x[0].upper()}{x[1:]}" for x in tokens]
            return ' '.join(tokens).strip()

        def template_1() -> str:
            return """
            ###  http://graffl.ai/pathology#ChildEntity
            :ChildEntity rdf:type owl:Class ;
            rdfs:label "ChildLabel" ;
            rdfs:subClassOf :ParentEntity .
            """.strip()

        def template_2() -> str:
            return """
            ###  http://graffl.ai/pathology#ChildEntity
            :ChildEntity rdf:type owl:Class ;
            rdfs:label "ChildLabel" .
            """.strip()

        def is_valid(value: str) -> bool:
            temp = value.replace(' ', '').replace('_', '').strip()
            total_chars = sum([x.isalpha() for x in temp])
            return len(temp) == total_chars

        snippets = []

        d_sorted = defaultdict(set)

        # putting the DataFrame into a dictionary helps ensure sort order
        # testing is easier if we can guarantee entity generation order
        for _, row in df.iterrows():
            d_sorted[row['Parent']].add(row['Child'])

        parents = [x for x in d_sorted if is_valid(x)]
        for parent in parents:

            parent_entity = to_entity(parent)
            parent_label = to_label(parent)

            children = [x for x in sorted(d_sorted[parent]) if is_valid(x)]
            for child in children:

                child_entity = to_entity(child)
                child_label = to_label(child)

                snippets.append(template_1().replace('ParentEntity', parent_entity).replace(
                    'ChildEntity', child_entity).replace('ChildLabel', child_label))

                snippets.append(template_2().replace(
                    'ChildEntity', parent_entity).replace('ChildLabel', parent_label))

        return snippets
