"""Test the main CLI entrypoint"""
import typing as t
from pathlib import Path
import os

import pytest

from geomancy.main import main_cli
from geomancy.config import Config


@pytest.fixture
def run(capsys) -> t.Callable:
    """Run the CLI with the given option, check for the expected exit
    code and return the output"""

    def runcmd(options, expected_code: int = 0):
        options = [options] if isinstance(options, str) else options
        try:
            main_cli(options)
        except SystemExit as e:
            if e.code != expected_code:
                raise e
        return capsys.readouterr()

    runcmd.__doc__ = run.__doc__
    return runcmd


@pytest.fixture
def config() -> Config:
    return Config()


@pytest.mark.parametrize("options", ("-h", "--help"))
def test_cli_help(run, options):
    """Test the --help message"""
    captured = run(options)
    assert "show this help message" in captured.out


@pytest.mark.parametrize("options", ("--disable-color",))
def test_cli_disable_color(run, options, config):
    """Test the --disable-color option"""
    captured = run(options)
    assert not config.TERM.USE_COLOR  # flag set to false


@pytest.mark.parametrize("options", ("--config",))
def test_cli_config(run, options):
    """Test the --config option"""
    captured = run(options)
    assert "[config]" in captured.out  # config output in TOML format


@pytest.mark.parametrize("flag", ("-e", "--env"))
def test_cli_env(run, flag, test_env_file):
    """Test the -e/--env and --overwrite flags for loading environment
    variables.

    See ./conftest.py for details on the 'test_env_file' fixture
    """
    # running '--overwrite' without '-e/--env' gives an error
    captured = run("--overwrite", expected_code=2)

    with pytest.MonkeyPatch.context() as mp:
        filepath = test_env_file["filepath"]
        variables = test_env_file["variables"]

        # Reset env variables
        for name in variables.keys():
            mp.delenv(name, raising=False)

        # running "-e/--env" should load environment variables, which are logged
        # in debug mode
        options = ("-d", flag, filepath)
        captured = run(options)

        # The variables are loaded in the current process
        for name, value in variables.items():
            assert os.environ[name] == value


@pytest.mark.parametrize(
    "options", (Path("examples") / "geomancy.toml", Path("examples") / "pyproject.toml")
)
def test_cli_check(run, options):
    """Test the default checks"""
    captured = run(str(options))
    # Check environment variables
    assert "Check environment variable" in captured.out
