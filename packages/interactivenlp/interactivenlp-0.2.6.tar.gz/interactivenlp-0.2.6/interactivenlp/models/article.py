from typing import List, Optional

from ..models.block import Block


class Article:
    def __init__(self, title: str, url: str, blocks: Optional[List['Block']] = None, global_block: Optional['Block'] = None):
        self.title = title
        self.url = url
        self.blocks = blocks
        self.global_block = global_block
