#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract Keyterms from Input Text using Textacy """


import pandas as pd
from pandas import DataFrame

from spacy.lang.en import English

from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject

from owl_builder.keyterms.dmo import TextacyKeytermExtractor
from owl_builder.keyterms.dmo import TextacyNgramExtractor
from owl_builder.keyterms.dmo import TextacyNounChunkExtractor
from owl_builder.keyterms.dmo import TextacyTermExtractor


class ExtractKeyterms(BaseObject):
    """ Aggregation Service for Extracting Keyterms """

    def __init__(self,
                 model: English):
        """
        Created:
            18-Jul-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/buildowl/issues/3
        """
        BaseObject.__init__(self, __name__)
        self._extract_terms = TextacyTermExtractor(model).process
        self._extract_ngrams = TextacyNgramExtractor(model).process
        self._extract_keyterms = TextacyKeytermExtractor(model).process
        self._extract_nounchunks = TextacyNounChunkExtractor(model).process

    def _process(self,
                 input_text: str,
                 use_keyterms: bool,
                 use_ngrams: bool,
                 use_terms: bool,
                 use_nounchunks: bool) -> DataFrame:

        master = []

        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)

        input_text = input_text.replace('-', '')  # hyphens are problematic ...

        if use_keyterms:
            [master.append(x) for x in self._extract_keyterms(input_text)]

        if use_ngrams:
            [master.append(x) for x in self._extract_ngrams(input_text)]

        if use_terms:
            [master.append(x) for x in self._extract_terms(input_text)]

        if use_nounchunks:
            [master.append(x) for x in self._extract_nounchunks(input_text)]

        return pd.DataFrame(master)

    def process(self,
                input_text: str,
                use_terms: bool = True,
                use_keyterms: bool = True,
                use_ngrams: bool = False,
                use_nounchunks: bool = False) -> DataFrame:

        sw = Stopwatch()

        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)

        df = self._process(input_text,
                           use_terms=use_terms,
                           use_keyterms=use_keyterms,
                           use_ngrams=use_ngrams,
                           use_nounchunks=use_nounchunks)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Keyword Extraction Complete",
                f"\tTotal Time: {str(sw)}",
                f"\tTotal Size: {len(df)}"]))

        return df
