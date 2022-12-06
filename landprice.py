import json
from typing import List

import pandas as pd
import requests


N_ROWS_FOR_EACH_REQUEST = 10000
AUTH_KEY = "..." # http://openapi.nsdi.go.kr/nsdi/index.do - 개별공시지가정보/API - 개별공시지가속성조회 - 신청하기


def download(path, pnu, year=None, header=True, mode="w", encoding="cp949"):
    def get(pnu, num_of_rows, page_no):
        params = {
            "authkey": AUTH_KEY,
            "pnu": pnu,
            "format": "json",
            "numOfRows": num_of_rows,
            "pageNo": page_no
        }
        if year is not None:
            params["stdrYear"] = str(year)

        response = requests.get("http://openapi.nsdi.go.kr/nsdi/IndvdLandPriceService/attr/getIndvdLandPriceAttr", params=params)
        result = json.loads(response.text)["indvdLandPrices"]
        return pd.DataFrame.from_records(result["field"]), int(result["totalCount"])

    page_no = 1

    print(f"Donwload page {page_no} of {pnu}")

    df, total = get(pnu, N_ROWS_FOR_EACH_REQUEST, 1)
    df.to_csv(path, encoding=encoding, index=False, header=header, mode=mode)

    while N_ROWS_FOR_EACH_REQUEST * page_no < total:
        page_no += 1

        print(f"Donwload page {page_no} of {pnu}")

        df, total = get(pnu, N_ROWS_FOR_EACH_REQUEST, page_no)
        df.to_csv(path, encoding=encoding, index=False, header=False, mode="a")


def downloads(path: str, pnus: List[str], year=None, encoding: str = "cp949"):
    """* The minimum length of pnu is 8.
    * If year is `None`, all years will be downloaded.
    """
    it = iter(pnus)
    download(path, next(it), encoding=encoding, year=year)

    for pnus in it:
        download(path, pnus, year=year, header=False, mode="a", encoding=encoding)


def main():
    downloads("result.csv", [
        "111101770010",
        "111101020010"
    ])


if __name__ == "__main__":
    main()
