#!/usr/bin/env python3
"""Base Generator

All `garak` generators must inherit from this.
"""

import logging
from typing import List

from colorama import Fore, Style


class Generator:
    """Base class for objects that wrap an LLM or other text-to-text service"""

    name = "Generator"
    description = ""
    generations = 10
    max_tokens = 150
    temperature = None
    top_k = None
    active = True

    def __init__(self, name="", generations=10):
        if "description" not in dir(self):
            self.description = self.__doc__.split("\n")[0]
        if name:
            self.name = name
        self.generations = generations
        if not self.generator_family_name:
            self.generator_family_name = "<empty>"
        print(
            f"🦜 loading {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}generator{Style.RESET_ALL}: {self.generator_family_name}: {self.name}"
        )
        logging.info(f"generator init: {self}")

    def _call_api(self, prompt: str) -> List[str]:
        return ""

    def generate(self, prompt) -> List[str]:
        outputs = []
        return outputs
