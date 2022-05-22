import pytest
import logging
import main


LOGGER = logging.getLogger(__name__)


def test_main(caplog):
    with caplog.at_level(logging.INFO):
        main.main()
    assert "WHISTAB is starting!" in caplog.text


def test_load_data(caplog):
    with caplog.at_level(logging.INFO):
        main.load_data()
    assert "Loading data" in caplog.text
