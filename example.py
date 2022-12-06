import landprice
import pnu


addresses = [
    "서울특별시 동대문구 전농동",
    "경기도 오산시"
]

pnus = pnu.gets(addresses)

landprice.downloads("path_to_result.csv", pnus, year=2022)
