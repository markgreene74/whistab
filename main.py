import logging
import tarfile
import urllib3
import os


DATA_MAIN_URL = "https://datasets.imdbws.com"
DATA_FILES = [
    "name.basics.tsv.gz",
    "title.akas.tsv.gz",
    "title.basics.tsv.gz",
    "title.crew.tsv.gz",
    "title.episode.tsv.gz",
    "title.principals.tsv.gz",
    "title.ratings.tsv.gz",
]


def load_data():
    logging.info("Loading data")

    for _file in DATA_FILES:
        _file_url = DATA_MAIN_URL + "/" + _file
        if os.path.isfile(_file):
            continue
        print(f"downloading file {_file_url}")

    """url = 'https://datasets.imdbws.com/name.basics.tsv.gz'
    chunk_size = 1000
    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)

    with open('text_file', 'wb') as out:
        while True:
            data = r.read(chunk_size)
            if not data:
                break
            out.write(data)

    r.release_conn()"""

    """tar = tarfile.open("filename.tar.gz", "r:gz")
    for member in tar.getmembers():
        f = tar.extractfile(member)
        if f is not None:
            content = f.read()"""


def main():
    logging.info("WHISTAB is starting!")
    load_data()


if __name__ == "__main__":
    main()
