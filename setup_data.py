import logging
import urllib3
import os
import gzip
import shutil


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
    chunk_size = 1000

    for _file in DATA_FILES:
        print(f"Processing {_file}")
        _file_url = DATA_MAIN_URL + "/" + _file

        if os.path.isfile("data/" + _file) and os.path.isfile(
            "data/" + _file.replace(".gz", "")
        ):
            logging.debug(f"file {_file} is already there")
            continue

        logging.info(f"downloading file {_file_url}")

        http = urllib3.PoolManager()
        r = http.request("GET", _file_url, preload_content=False)

        with open("data/" + _file, "wb") as out:
            while True:
                data = r.read(chunk_size)
                if not data:
                    break
                out.write(data)

        r.release_conn()

        with gzip.open("data/" + _file, "rb") as f_in:
            logging.info(f"saving file {_file.replace('.gz', '')}")
            with open("data/" + _file.replace(".gz", ""), "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)


def main():
    logging.info("Starting the setup (download the fresh data and populate the database)")
    load_data()


if __name__ == "__main__":
    main()