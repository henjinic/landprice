# landprice

Download official landprice data.

## Prerequisites
1. Get an authentication key from [here](http://openapi.nsdi.go.kr/nsdi/index.do). (개별공시지가정보/API/개별공시지가속성조회)
2. Set `AUTH_KEY` in `landprice.py` to the key from above.
    ```python
    # landprice.py
    AUTH_KEY = "your_authentication_key"
    ```

## Usage
1. (Optional) Get PNUs by calling `pnu.gets()` with a list of addresses. The addresses should consist of same keywords as those in `pnu.csv`.
    ```python
    import pnu

    addresses = [
        "서울특별시 동대문구 전농동",
        "경기도 오산시",
        ...,
    ]

    pnus = pnu.gets(addresses)
    ```
2. Download landprice data by calling `landprice.downloads()` with a list of PNUs. PNU should have a minimum length of 8. If you skip the `year` parameter, all year data will be downloaded, but it can be a time consuming job.
    ```python
    import landprice

    landprice.downloads("path/to/result.csv", pnus, year=2022)
    ```