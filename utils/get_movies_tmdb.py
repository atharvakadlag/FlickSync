import time
import json
import requests
import os


class TMDB:
    base_url = "https://api.themoviedb.org/3"

    URL_MOVIE_LIST = f"{base_url}/movie/changes?page=1"

    def URL_MOVIE_DETAILS(self, movie_id: int):
        return f"{self.base_url}/movie/{movie_id}?language=en-US"

    HEADERS = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.environ.get('TBDM_API')}"
    }


if __name__ == "__main__":
    try:
        with open("temp/temp.json", "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Unable to load {e}")
        response = requests.get(TMDB.URL_MOVIE_LIST, headers=TMDB.HEADERS)

        with open("temp/temp.json", "w") as f:
            json.dump(response.json(), f)

        data = response.json()

    results = data.get("results")

    if not results:
        raise Exception("No movies fetched")

    results = [i for i in results if not i['adult']]

    print(f"Got {len(results)} movies")

    for movie in results:
        is_adult = movie['adult']
        id = movie['id']

        if is_adult:
            continue

        response = requests.get(TMDB().URL_MOVIE_DETAILS(id), headers=TMDB.HEADERS)
        with open(f"temp/movie_details_{id}.json", "w") as f:
            json.dump(response.json(), f)

        time.sleep(0.1)
