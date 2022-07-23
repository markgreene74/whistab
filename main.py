import logging
import urllib3
import os
import gzip
import shutil
import pandas as pd


def search_actor(name):
    df = pd.read_csv('data/base.csv')
    name = name.lower()
    result = df[df['primaryName'].str.lower().str.contains(name)]
    return result.iloc[:,0].to_list()


def main():
    logging.info("WHISTAB is starting!")


if __name__ == "__main__":
    main()

