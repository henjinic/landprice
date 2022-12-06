from collections import defaultdict
from itertools import chain
from typing import List

import pandas as pd


_dtype_map = defaultdict(lambda: str)
_dtype_map["IS_EXISTS"] = bool
_base_df = pd.read_csv("pnu.csv", encoding="cp949", dtype=_dtype_map)


def gets(texts: List[str]):
    return sorted(set(chain.from_iterable(get(text) for text in texts)))


def get(text):
    def detailed_get(sd, sgg=None, emd=None, ri=None):
        df = _base_df[_base_df["IS_EXISTS"] == True]
        df = df[df["SD"] == sd]
        if sgg is not None:
            df = df[df["SGG"] == sgg]
        if emd is not None:
            df = df[df["EMD"] == emd]
        if ri is not None:
            df = df[df["RI"] == ri]
        pnu_s = df["SD_CD"] + df["SGG_CD"] + df["EMD_CD"] + df["RI_CD"]
        return pnu_s.tolist()

    return sorted(detailed_get(*text.split()))


def main():
    addresses = [
        "서울특별시 종로구",
        "서울특별시 금천구 가산동"
    ]
    print(gets(addresses))


if __name__ == "__main__":
    main()
