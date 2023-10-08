#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Author  huang22
Date    ：2023/9/28 18:25
"""
from unicodetext import UnicodeCategories


def remove_punctuations(doc: str):
    return doc.translate({ord(i): None for i in UnicodeCategories.Po})


if __name__ == "__main__":
    s = "iqwg weuh 823t49 - =qr- / 1!.../l;六分。！"
    print(remove_punctuations(s))
