# -*- coding: utf-8 -*-
import pytest
from click.testing import CliRunner
from dayone_2_to_1 import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Hello, world.'
