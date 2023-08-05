from __future__ import annotations
from typing import IO, List, Literal, Union
from zipfile import ZipFile, ZIP_DEFLATED

from wilson.project import Project
from wilson.serialize import serializeProject
from wilson.parse import parseProjectFromBytes


class Catalogue:
    """Class with methods to read from and write to event catalogues.

    Attributes
    ----------
    file: { str, IO[bytes]}
        Either the path to catalogue file, or a file-like object.
    mode: Literal['r', 'w', 'x', 'a'], default='r'
        The mode can be either read 'r', write 'w', exclusive create 'x',
        or append 'a'.
    """

    def __init__(
        self, file: Union[str, IO[bytes]], mode: Literal["r", "w", "x", "a"] = "r"
    ) -> None:
        self._archive = ZipFile(file, mode, ZIP_DEFLATED)

    def __enter__(self) -> Catalogue:
        return self

    def __exit__(self, type, value, traceback) -> None:  # type: ignore[no-untyped-def]
        self.close()

    def __del__(self) -> None:
        self.close()

    def namelist(self) -> List[str]:
        """Return a list of file names in the catalogue"""
        return self._archive.namelist()

    def open(self, name: str) -> Project:
        """Opens the given entry in the catalogue and returns the parsed project."""
        return parseProjectFromBytes(self._archive.read(name))

    def save(self, name: str, project: Project) -> None:
        """Serializes the given project and saves it under the given name in the
        catalogue
        """
        self._archive.writestr(name, serializeProject(project))

    def close(self) -> None:
        """Close the file, and for mode 'w', 'x' and 'a' write the ending records."""
        self._archive.close()


def saveProject(project: Project, path: str) -> None:
    """Saves the given project under the specified path by creating a catalogue
    with only one entry."""
    with Catalogue(path, "w") as cat:
        cat.save("project", project)


def openProject(path: str) -> Project:
    """Opens the given catalogue ans returns the first entry."""
    with Catalogue(path, "r") as cat:
        if len(cat.namelist()) == 0:
            raise RuntimeError("Catalogue is empty!")
        return cat.open(cat.namelist()[0])
