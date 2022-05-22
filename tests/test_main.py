import pytest
import logging
import main


LOGGER = logging.getLogger(__name__)


def test_main(caplog):
    with caplog.at_level(logging.INFO):
        main.main()
    assert 'WHISTAB is starting!' in caplog.text
