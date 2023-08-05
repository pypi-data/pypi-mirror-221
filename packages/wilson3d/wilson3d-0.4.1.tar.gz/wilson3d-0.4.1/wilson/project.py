from __future__ import annotations
from datetime import datetime
import string
from typing import Iterable, List, Optional, Tuple

from wilson.objects import Animatable
from wilson.data import ColorLike, ColorMap, Graph, Path, VectorProperty


class Camera:
    """A virtual camera representing the view of the animation

    Attributes
    ----------
    position: {Tuple[float, float, float], None}, default=None
        The position the camera sits. (1,1,1) if None

    target: {Tuple[float, float, float], None}: default=None
        The location the camera points at. (0,0,0) if None
    """

    def __init__(
        self,
        *,
        position: Optional[Tuple[float, float, float]] = None,
        target: Optional[Tuple[float, float, float]] = None,
    ):
        self.position = position
        self.target = target

    @property
    def position(self) -> Optional[Tuple[float, float, float]]:
        """Position the camera sits."""
        return self._position

    @position.setter
    def position(self, value: Optional[Tuple[float, float, float]]) -> None:
        self._position = value

    @property
    def target(self) -> Optional[Tuple[float, float, float]]:
        """Location the camera points at."""
        return self._target

    @target.setter
    def target(self, value: Optional[Tuple[float, float, float]]) -> None:
        self._target = value


class Project:
    """Data model for a animation project with the ability to serialize and
    deserialize.

    Attributes
    ----------
    name: str, default=''
        Name of the project

    author: Optional[str], default=`None`
        Name of the author or detector of the event

    date: Optional[datetime], default=`None`
        Date of the experiment or event

    description: Optional[str], default=`None`
        Additional information about the event

    startTime: Optional[float], default=`None`
        Time value, from which the animation starts.
        If None, will be set to earliest graph or path point.

    endTime: Optional[float], default=`None`
        Time value, where the animation ends.
        If None, will be set to latest graph or path point.

    speedRatio: float, default=1.0
        Playback speed in time units per second

    graphs: Iterable[GraphLike]
        List of graph like data to be included into the project

    paths: Iterable[PathLike]
        List of path like data to be included into the project

    animatables: Iterable[Animatable]
        List of animatables to be included into the project

    hiddenGroups: Iterable[str]
        List of group names, that should be hidden by viewers by default

    camera: Optional[Camera], default=`None`
        An optional animatable camera

    colormap: Optional[Camera], default=`None`
        Color map used to translate scalars into colors. If None, viridis is used.

    colormapRange: Optional[Tuple[float,float]], default=`None`
        Range of the colormap to use as a tuple (min,max). If None, this is
        inferred during serialization from the data.
    """

    def __init__(
        self,
        name: str = "",
        *,
        author: Optional[str] = None,
        date: Optional[datetime] = None,
        description: Optional[str] = None,
        startTime: Optional[float] = None,
        endTime: Optional[float] = None,
        speedRatio: float = 1.0,
        graphs: Iterable[Graph] = [],
        paths: Iterable[Path] = [],
        animatables: Iterable[Animatable] = [],
        hiddenGroups: Iterable[str] = [],
        camera: Optional[Camera] = None,
        colormap: Optional[ColorMap] = None,
        colormapRange: Optional[Tuple[float, float]] = None,
    ):
        self.name = name
        self.author = author
        self.date = date
        self.description = description
        self.startTime = startTime
        self.endTime = endTime
        self.speedRatio = speedRatio
        self.graphs = graphs  # type: ignore[assignment]
        self.paths = paths  # type: ignore[assignment]
        self.animatables = animatables  # type: ignore[assignment]
        self.hiddenGroups = hiddenGroups  # type: ignore[assignment]
        self.camera = camera
        self.colormap = colormap
        self.colormapRange = colormapRange

    @property
    def name(self) -> str:
        """Name of the project"""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def author(self) -> Optional[str]:
        """Name of the author or detector of the event"""
        return self._author

    @author.setter
    def author(self, value: Optional[str]) -> None:
        self._author = value

    @author.deleter
    def author(self) -> None:
        self._author = None

    @property
    def date(self) -> Optional[datetime]:
        """Date of the experiment or event"""
        return self._date

    @date.setter
    def date(self, value: Optional[datetime]) -> None:
        self._date = value

    @date.deleter
    def date(self) -> None:
        self._date = None

    @property
    def description(self) -> Optional[str]:
        """Additional information about the event"""
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        self._description = value

    @description.deleter
    def description(self) -> None:
        self._description = None

    @property
    def startTime(self) -> Optional[float]:
        """Time value, from which the animation starts"""
        return self._startTime

    @startTime.setter
    def startTime(self, value: Optional[float]) -> None:
        self._startTime = value

    @startTime.deleter
    def startTime(self) -> None:
        self._startTime = None

    @property
    def endTime(self) -> Optional[float]:
        """Time value, where the animation ends"""
        return self._endTime

    @endTime.setter
    def endTime(self, value: Optional[float]) -> None:
        self._endTime = value

    @endTime.deleter
    def endTime(self) -> None:
        self._endTime = None

    @property
    def speedRatio(self) -> float:
        """Playback speed in time units per second"""
        return self._speedRatio

    @speedRatio.setter
    def speedRatio(self, value: float) -> None:
        self._speedRatio = value

    @property
    def graphs(self) -> List[Graph]:
        return self._graphs

    @graphs.setter
    def graphs(self, value: Iterable[Graph]) -> None:
        self._graphs = list(value)

    @graphs.deleter
    def graphs(self) -> None:
        self._graphs = []

    def appendGraph(self, graph: Graph) -> None:
        """Appends a single graph to the internal list"""
        self.graphs.append(graph)

    def addGraphs(self, graphs: Iterable[Graph]) -> None:
        """Adds multiple graphs"""
        self.graphs.extend(graphs)

    def clearGraphs(self) -> None:
        """Removes all graphs from this project"""
        self._graphs = []

    @property
    def paths(self) -> List[Path]:
        return self._paths

    @paths.setter
    def paths(self, value: Iterable[Path]) -> None:
        self._paths = list(value)

    @paths.deleter
    def paths(self) -> None:
        self._paths = []

    def appendPath(self, path: Path) -> None:
        """Appends a single path to the internal list"""
        self.paths.append(path)

    def addPaths(self, paths: Iterable[Path]) -> None:
        """Adds multiple paths"""
        self.paths.extend(paths)

    def clearPaths(self) -> None:
        """Removes all paths from this project"""
        self._paths = []

    @property
    def animatables(self) -> List[Animatable]:
        return self._animatables

    @animatables.setter
    def animatables(self, value: Iterable[Animatable]) -> None:
        self._animatables = list(value)

    @animatables.deleter
    def animatables(self) -> None:
        self._animatables = []

    def appendAnimatable(self, animatable: Animatable) -> None:
        """Appends a single animatable to the internal list"""
        self.animatables.append(animatable)

    def addAnimatables(self, animatables: Iterable[Animatable]) -> None:
        """Adds multiple animatables"""
        self.animatables.extend(animatables)

    def clearAnimatables(self) -> None:
        """Removes all animatables from this project"""
        self._animatables = []

    @property
    def hiddenGroups(self) -> List[str]:
        """List of group names, that should be hidden by viewers by default"""
        return self._hiddenGroups

    @hiddenGroups.setter
    def hiddenGroups(self, value: Iterable[str]) -> None:
        self._hiddenGroups = list(value)

    @hiddenGroups.deleter
    def hiddenGroups(self) -> None:
        self._hiddenGroups = []

    @property
    def camera(self) -> Optional[Camera]:
        """An optional animatable camera"""
        return self._camera

    @camera.setter
    def camera(self, value: Optional[Camera]) -> None:
        self._camera = value

    @camera.deleter
    def camera(self) -> None:
        self._camera = None

    @property
    def colormap(self) -> Optional[ColorMap]:
        """Color map used to translate scalars into colors."""
        return self._colormap

    @colormap.setter
    def colormap(self, value: Optional[ColorMap]) -> None:
        self._colormap = value

    @colormap.deleter
    def colormap(self) -> None:
        self._colormap = None

    @property
    def colormapRange(self) -> Optional[Tuple[float, float]]:
        """
        Range of the colormap to use as a tuple (min,max). If None, this is
        inferred during serialization from the data.
        """
        return self._cmapRange

    @colormapRange.setter
    def colormapRange(self, value: Optional[Tuple[float, float]]) -> None:
        # check range
        if value is not None and value[0] >= value[1]:
            raise ValueError("min must be larger than max")
        self._cmapRange = value

    @colormapRange.deleter
    def colormapRange(self) -> None:
        self._cmapRange = None
