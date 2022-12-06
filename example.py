import landprice
import pnu

locations = [
    "서울특별시 동대문구 전농동",
    "경기도 오산시"
]

pnus = pnu.gets(locations)

landprice.downloads("path_to_result.csv", pnus, year=2022)
