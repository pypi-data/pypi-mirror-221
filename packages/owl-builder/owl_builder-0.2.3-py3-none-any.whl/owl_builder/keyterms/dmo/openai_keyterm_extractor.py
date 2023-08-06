#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Extract Keyterms using an OpenAI Model """

import hashlib
from typing import List

from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject

from openai_helper import chat
from owl_builder.core import OpenAICache


class OpenAIKeytermExtractor(BaseObject):
    """ Extract Keyterms using an OpenAI Model """

    def __init__(self):
        """
        Created:
            28-Mar-2023
            craigtrim@gmail.com
            *   https://github.com/craigtrim/owl-builder/issues/5
        """
        BaseObject.__init__(self, __name__)
        cache = OpenAICache()
        self._exists_in_cache = cache.exists
        self._write_to_cache = cache.write
        self._read_from_cache = cache.read

    @staticmethod
    def _prompt(input_text: str) -> str:
        return f"Some text is provided below. Given the text, extract up to 10 keywords from the text. Avoid stopwords.---------------------\\n{input_text}\\n---------------------\\nProvide keywords in the following comma-separated format: \'KEYWORDS: <keywords>\'\\n"

    @staticmethod
    def _cleanse(input_text: str) -> str:
        if input_text.endswith('.'):
            input_text = input_text[:-1]

        return input_text

    def process(self,
                input_text: str) -> List[str]:

        sw = Stopwatch()

        if self.isEnabledForDebug:
            Enforcer.is_str(input_text)

        if self._exists_in_cache(input_text):
            return self._read_from_cache(input_text)

        keyterms = chat(
            input_prompt=self._prompt(input_text),
            messages=None,
            remove_emojis=True)

        if keyterms:

            if keyterms.startswith('KEYWORDS:'):
                keyterms = keyterms[9:].strip().split(',')

            keyterms = [
                x.strip() for x in keyterms
            ]

            keyterms = [
                self._cleanse(x) for x in keyterms
                if x and len(x)
            ]

        self._write_to_cache(data=keyterms, file_name=input_text)

        if self.isEnabledForInfo:
            self.logger.info('\n'.join([
                "Keyword Extraction Complete",
                f"\tTotal Time: {str(sw)}",
                f"\tExtracted Terms: {keyterms}"]))

        return keyterms
