# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import tiktoken


class Tokenizer:
    """Handle LLM tokenizing using the tiktoken library."""

    def __init__(self, model_name: str):
        self.model_name = model_name

        # Get fast tokenizer for model_name
        self.encoding = tiktoken.get_encoding("cl100k_base")

    def count_tokens(self, input_str: str) -> int:
        # Count tokens, including special tokens like <|endofprompt|>
        return len(self.encoding.encode(input_str, allowed_special="all"))
