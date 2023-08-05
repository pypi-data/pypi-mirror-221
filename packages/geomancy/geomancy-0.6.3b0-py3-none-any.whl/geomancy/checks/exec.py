"""
Checks for executables
"""
import typing as t
from shutil import which
import subprocess

from .base import CheckVersion
from .utils import version_to_tuple
from ..config import Parameter

__all__ = ("CheckExec",)


class CheckExec(CheckVersion):
    """Check for the presence and version of executables"""

    # The message for checking environment variables
    msg = Parameter(
        "CHECKEXEC.MSG",
        default="Check executable '{check.raw_value}'...",
    )

    # Alternative names for the class
    aliases = ("checkExec",)

    @property
    def value(
        self,
    ) -> t.Tuple[
        t.Union[str, None], t.Union[t.Callable, None], t.Union[t.Tuple[int], None]
    ]:
        """Get the package name, comparison operator and version tuple."""
        cmd_name, op, version = CheckVersion.value.fget(self)

        # Check to see if the cmd_name exists. Returns None if it doesn't
        cmd_name = which(cmd_name) if cmd_name is not None else cmd_name

        return cmd_name, op, version

    @value.setter
    def value(self, v):
        CheckVersion.value.fset(self, v)

    def get_current_version(self) -> t.Union[None, t.Tuple[int]]:
        cmd_name, op, version = self.value

        if cmd_name is None:  # command not found
            return None

        for args in (  # Different commands to try for versions
            (cmd_name, "-V"),
            (cmd_name, "--version"),
        ):
            try:
                proc = subprocess.run(args, capture_output=True)
            except FileNotFoundError:
                # Couldn't find the executable
                continue

            if proc.returncode != 0:  # Wasn't a success
                continue

            # Try to parse the current version string
            current_version = version_to_tuple(proc.stdout.decode("UTF-8"))
            current_version = (
                current_version
                if current_version is not None
                else version_to_tuple(proc.stderr.decode("UTF-8"))
            )

            if current_version is not None:
                # Current version found! We're done
                return current_version

        # Not found
        return None
