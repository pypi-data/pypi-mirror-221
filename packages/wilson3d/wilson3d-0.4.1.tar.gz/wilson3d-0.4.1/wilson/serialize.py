import numpy as np
import cmasher as cmr  # type: ignore[import]
import re
from types import SimpleNamespace
from typing import Any, Tuple

from wilson.color import getColorByName
from wilson.data import (
    ColorMap,
    ColorProperty,
    Graph,
    Interpolation,
    ScalarProperty,
    Path,
    TextLike,
    VectorProperty,
)
from wilson.objects import Animatable, Line, Prism, Sphere, Tube, Overlay
from wilson.project import Camera, Project
import wilson.proto as proto

# Mandatory xkcd: https://xkcd.com/1171/
text_pattern = re.compile("%\(([^\.]+?)(?:\[(\d*?)\])?(\.[x-z])?\)(.*?[a-z])?", re.MULTILINE)


def serializeProject(project: Project) -> bytes:
    """
    Returns a bytes object containing the serialized representation of the given
    project ready to be saved.
    """
    out = proto.Project()

    # create serialization state
    state = SimpleNamespace(cmapMin=float("inf"), cmapMax=float("-inf"))

    # fill meta
    out.meta.name = project.name
    if project.author is not None:
        out.meta.author = project.author
    if project.date is not None:
        out.meta.date.FromDatetime(project.date)
    if project.description is not None:
        out.meta.description = project.description

    # camera
    if project.camera is not None:
        out.camera.CopyFrom(_serializeCamera(project.camera, project))

    # We'll fill missing names with '[type] [i]' ,e.g. Sphere 1
    nextSphereId = 1
    nextLineId = 1
    nextPrismId = 1
    nextTubeId = 1
    nextTextId = 1

    # animatables
    for a in project.animatables:
        if isinstance(a, Sphere):
            # fill name if not present
            if a.name is None:
                a.name = "Sphere " + str(nextSphereId)
                nextSphereId += 1
            out.animatibles.append(_serializeSphere(a, project, state))
        elif isinstance(a, Line):
            if a.name is None:
                a.name = "Line " + str(nextLineId)
                nextLineId += 1
            out.animatibles.append(_serializeLine(a, project, state))
        elif isinstance(a, Prism):
            if a.name is None:
                a.name = "Prism " + str(nextPrismId)
                nextPrismId += 1
            out.animatibles.append(_serializePrism(a, project, state))
        elif isinstance(a, Tube):
            if a.name is None:
                a.name = "Tube " + str(nextTubeId)
                nextTubeId += 1
            out.animatibles.append(_serializeTube(a, project, state))
        elif isinstance(a, Overlay):
            if a.name is None:
                a.name = "Label " + str(nextTextId)
                nextTextId += 1
            out.animatibles.append(_serializeOverlay(a, project))
        # skip UnknownAnimatible

    # hidden groups
    out.hiddenGroups.extend(project.hiddenGroups)

    # serialize data
    # Do this after serializing animatables as they might add implicit data
    out.graphs.extend(_serializeGraph(graph, i) for i, graph in enumerate(project.graphs))
    out.paths.extend(_serializePath(path, i) for i, path in enumerate(project.paths))

    # serialize colormap after we inferred ranges during animatable serialization
    cmapRange = project.colormapRange
    if cmapRange is None:
        cmapRange = (state.cmapMin, state.cmapMax)
    if project.colormap is not None:
        out.colormap.CopyFrom(_serializeColormap(project.colormap, cmapRange))
    else:
        # If no color map specified use default: viridis
        out.colormap.CopyFrom(_serializeColormap("viridis", cmapRange))

    # Fill time related stuff
    # We need to do this after we got all paths and graphs as we might have to
    # check them in order to get start and/or endTime
    if project.startTime is not None:
        out.meta.startTime = project.startTime
    else:
        inf = float("inf")
        startGraph = min((g.points[0].time for g in out.graphs if len(g.points) > 0), default=inf)
        startPath = min((p.points[0].time for p in out.paths if len(p.points) > 0), default=inf)
        start = min(startGraph, startPath)
        if start == inf:
            start = 0.0
        out.meta.startTime = start
    if project.endTime is not None:
        out.meta.endTime = project.endTime
    else:
        ninf = float("-inf")
        endGraph = max((g.points[-1].time for g in out.graphs if len(g.points) > 0), default=ninf)
        endPath = max((p.points[-1].time for p in out.paths if len(p.points) > 0), default=ninf)
        end = max(endGraph, endPath)
        if end == ninf:
            end = 0.0
        out.meta.endTime = end
    out.meta.speedRatio = project.speedRatio

    # ask protobuf to serialize
    return out.SerializeToString()


################################## Data ########################################


def _serializeInterpolation(intpol: Interpolation) -> proto.Interpolation.ValueType:
    if intpol == Interpolation.LINEAR:
        return proto.Interpolation.LINEAR
    if intpol == Interpolation.HOLD:
        return proto.Interpolation.HOLD
    if intpol == Interpolation.AHEAD:
        return proto.Interpolation.AHEAD
    if intpol == Interpolation.STEP:
        return proto.Interpolation.STEP
    else:
        raise ValueError("Unknown interpolation mode!")


def _serializeGraph(graph: Graph, id: int) -> proto.Graph:
    result = proto.Graph()
    # meta
    result.name = graph.name
    result.id = id
    result.interpolation = _serializeInterpolation(graph.interpolation)
    # data - sorted by time
    a = np.array(graph.array, dtype=np.float64)
    a = a[a[:, 0].argsort()]
    # serialize array
    for row in a:
        point = result.points.add()
        point.time = row[0]
        point.value = row[1]
    # done
    return result


def _serializePath(path: Path, id: int) -> proto.Path:
    result = proto.Path()
    # meta
    result.name = path.name
    result.id = id
    result.interpolation = _serializeInterpolation(path.interpolation)
    # data - sorted by time
    a = np.array(path.array, dtype=np.float64)
    a = a[a[:, 0].argsort()]
    # serialize array
    for row in a:
        point = result.points.add()
        point.time = row[0]
        point.position.x, point.position.y, point.position.z = row[1:]
    # done
    return result


def _serializeColor(color: Tuple[Any, ...]) -> proto.Color:
    result = proto.Color()
    if isinstance(color, tuple) and len(color) >= 3:
        result.r = float(color[0])
        result.g = float(color[1])
        result.b = float(color[2])
        # optional alpha channel
        if len(color) == 3:
            result.a = 1.0
        elif len(color) == 4:
            result.a = float(color[3])

        return result

    # Could not serialize -> error
    raise ValueError("Invalid color tuple")


def _serializeColormap(colormap: ColorMap, range: Tuple[float, float]) -> proto.ColorMap:
    result = proto.ColorMap()
    min_out = range[0]
    d = range[1] - range[0]
    if isinstance(colormap, str):
        # look up color map
        colors = cmr.take_cmap_colors(colormap, None)
        n = len(colors)
        stop = None
        for i, c in enumerate(colors):
            stop = result.stops.add()
            stop.value = i * d / n + min_out  # rescale cmap
            stop.color.r, stop.color.g, stop.color.b = c
            stop.color.a = 1.0
        # Force range on last stop
        if stop is not None:
            stop.value = range[1]
    else:
        cmaps = np.array(colormap, dtype=np.float64)
        # check dimensions
        if len(cmaps.shape) != 2 or not (cmaps.shape[1] == 4 or cmaps.shape[1] == 5):
            raise ValueError("Invalid color map!")
        cmaps = cmaps[cmaps[:, 0].argsort()]
        min_in = cmaps.min()
        d_in = cmaps.max() - cmaps.min()
        stop = None
        for c in cmaps:
            stop = result.stops.add()
            stop.value = (c[0] - min_in) * d / d_in + min_out  # rescale cmap
            stop.color.r, stop.color.g, stop.color.b = c[1:4]
            if cmaps.shape[1] == 4:
                stop.color.a = 1.0
            else:
                stop.color.a = c[4]
        # Force range on last stop
        if stop is not None:
            stop.value = range[1]
    return result


def _serializeText(text: TextLike, objName: str, project: Project) -> str:
    # plain string?
    if isinstance(text, str):
        return text

    # serialize data obtain list of properties (either const or global id)
    gn, pn = f".{objName}_graph ", f".{objName}_path"
    graphs = [
        (
            g.name if isinstance(g, Graph) else "",  # name (if graph)
            _serializeScalarProperty(g, gn + str(i), project),
        )  # scalar prop
        for i, g in enumerate(text.graphs)
    ]
    paths = [
        (
            p.name if isinstance(p, Path) else "",  # name (if path)
            _serializeVectorProperty(p, pn + str(i), project),
        )  # vector prop
        for i, p in enumerate(text.paths)
    ]

    # create substitution function
    def sub(match: re.Match) -> str:
        name = match[1]
        # Index graph?
        if name == "graphs":
            # sanity check
            if match[2] is None:
                raise ValueError(f'Error in text reference "{match[0]}": No graph index provided!')
            graph_id = int(match[2])
            if graph_id < 0 or graph_id >= len(graphs):
                raise ValueError(f'Error in text reference "{match[0]}": Graph index out of range!')
            if match[3] is not None:
                raise ValueError(
                    f'Error in text reference "{match[0]}": Graphs do not provide properties!'
                )

            # process graph
            graph = graphs[graph_id][1]  # tuple: (name, graph)

            # const value?
            if graph.HasField("constValue"):
                # const value -> replace it
                return f'%{match.group(4) or "s"}' % graph.constValue
            else:
                # construct correct template string
                return f'%(graphs[{graph.graphId}]){match.group(4) or ""}'
        elif name == "paths":
            # sanity check
            if match[2] is None:
                raise ValueError(f'Error in text reference "{match[0]}": No path index provided!')
            path_id = int(match[2])
            if path_id < 0 or path_id >= len(paths):
                raise ValueError(f'Error in text reference "{match[0]}": Path index out of range!')

            # process path
            path = paths[path_id][1]  # tuple: (name, path)

            # const value?
            if path.HasField("constValue"):
                # check what to print
                if match.group(3) == ".x":
                    return f'${match.group(4) or "s"}' % path.constValue.x
                elif match.group(3) == ".y":
                    return f'${match.group(4) or "s"}' % path.constValue.y
                else:  # match.group(3) == '.z'
                    return f'${match.group(4) or "s"}' % path.constValue.z
            else:
                # construct correct template string
                return f'%(paths[{path.pathId}]{match.group(3)}){match.group(4) or ""}'

        # it must be a named data object

        # sanity check -> no index if named
        if match.group(2) is not None:
            raise ValueError(f'Error in text reference "{match[0]}": Cannot index named data!')

        # search by name; lists of tuple: (name, data)
        graph_matches = [g[1] for g in graphs if g[0] == name]
        path_matches = [p[1] for p in paths if p[0] == name]

        # sanity check
        matches = len(graph_matches) + len(path_matches)
        if matches == 0:
            raise ValueError(
                f'Error in text reference "{match[0]}": The referenced data was not found!'
            )
        if matches > 1:
            raise ValueError(
                f'Error in text reference "{match[0]}": The referenced data is not unique by name!'
            )

        # Is it a path?
        if len(path_matches) == 1:
            path = path_matches[0]
            return f'%(paths[{path.pathId}]{match.group(3)}){match.group(4) or ""}'
        else:
            graph = graph_matches[0]
            return f'%(graphs[{graph.graphId}]){match.group(4) or ""}'

    # END def sub

    # find all references and replace with global id
    return re.sub(text_pattern, sub, text.content)


################################ Properties ####################################


def _serializeScalarProperty(
    scalar: ScalarProperty, name: str, project: Project
) -> proto.ScalarProperty:
    result = proto.ScalarProperty()
    if isinstance(scalar, float) or isinstance(scalar, int):
        # const value
        result.constValue = float(scalar)
    elif isinstance(scalar, Graph):
        # graph -> check if already present in project
        #      -> Either fetch graph id or add graph
        if scalar in project.graphs:
            id = project.graphs.index(scalar)
            result.graphId = id
        else:
            id = len(project.graphs)
            project.graphs.append(scalar)
            result.graphId = id
    else:
        # scalar is path like, but not a graph -> create a new graph
        id = len(project.graphs)
        project.graphs.append(Graph(scalar, name))
        result.graphId = id
    return result


def _serializeVectorProperty(
    vector: VectorProperty, name: str, project: Project
) -> proto.VectorProperty:
    result = proto.VectorProperty()
    if isinstance(vector, tuple) and len(vector) == 3:
        # const value
        result.constValue.x = vector[0]
        result.constValue.y = vector[1]
        result.constValue.z = vector[2]
    elif isinstance(vector, Path):
        # Check if already present in project
        # -> Either fetch path id or add path
        if vector in project.paths:
            id = project.paths.index(vector)
            result.pathId = id
        else:
            id = len(project.paths)
            project.paths.append(vector)
            result.pathId = id
    else:
        # path like, but not a path -> create new path
        id = len(project.paths)
        project.paths.append(Path(vector, name))
        result.pathId = id
    return result


def _serializeColorProperty(
    color: ColorProperty, name: str, project: Project, state: SimpleNamespace
) -> proto.ColorProperty:
    result = proto.ColorProperty()
    if isinstance(color, str):
        # lookup color
        result.constValue.CopyFrom(_serializeColor(getColorByName(color)))
    elif isinstance(color, float) or isinstance(color, int):
        # scalar into cmap
        value = float(color)
        # update cmap range
        state.cmapMin = min(state.cmapMin, value)
        state.cmapMax = max(state.cmapMax, value)
        # save value
        result.scalarValue = float(color)
    elif isinstance(color, tuple):
        result.constValue.CopyFrom(_serializeColor(color))
    elif isinstance(color, Graph):
        # graph -> check if already present in project
        #      -> Either fetch graph id or add graph
        if color in project.graphs:
            id = project.graphs.index(color)
            result.graphId = id
        else:
            id = len(project.graphs)
            project.graphs.append(color)
            result.graphId = id
            # update color map
            state.cmapMin = min(state.cmapMin, np.min(color.array))
            state.cmapMax = max(state.cmapMax, np.max(color.array))
    else:
        # color is graph like, but not a graph -> create a new graph
        id = len(project.graphs)
        graph = Graph(color, name)
        project.graphs.append(graph)
        result.graphId = id
        # update color map
        state.cmapMin = min(state.cmapMin, np.min(graph.array))
        state.cmapMax = max(state.cmapMax, np.max(graph.array))
    return result


def _serializeCamera(camera: Camera, project: Project) -> proto.Camera:
    result = proto.Camera()
    if camera.position is not None:
        result.position.x = camera.position[0]
        result.position.y = camera.position[1]
        result.position.z = camera.position[2]
    if camera.target is not None:
        result.target.x = camera.target[0]
        result.target.y = camera.target[1]
        result.target.z = camera.target[2]
    return result


def _serializeTextPosition(target: proto.Overlay, position: str) -> None:
    if position == "center":
        target.position = proto.TextPosition.CENTER
    elif position == "top" or position == "t":
        target.position = proto.TextPosition.TOP
    elif position == "bottom" or position == "b":
        target.position = proto.TextPosition.BOTTOM
    elif position == "left" or position == "l":
        target.position = proto.TextPosition.LEFT
    elif position == "right" or position == "r":
        target.position = proto.TextPosition.RIGHT
    elif position == "upper right" or position == "ur":
        target.position = proto.TextPosition.UPPER_RIGHT
    elif position == "upper left" or position == "ul":
        target.position = proto.TextPosition.UPPER_LEFT
    elif position == "lower right" or position == "lr":
        target.position = proto.TextPosition.LOWER_RIGHT
    elif position == "lower left" or position == "ll":
        target.position = proto.TextPosition.LOWER_LEFT
    else:
        raise ValueError("Unknown Text Position!")


################################## Objects #####################################


def _createAnimatable(meta: Animatable, project: Project) -> proto.Animatible:
    result = proto.Animatible()
    assert meta.name is not None
    result.name = meta.name
    if meta.description is not None:
        result.description = _serializeText(meta.description, result.name, project)
    if len(meta.groups) > 0:
        result.groups[:] = meta.groups
    return result


def _serializeSphere(sphere: Sphere, project: Project, state: SimpleNamespace) -> proto.Animatible:
    result = _createAnimatable(sphere, project)
    # properties
    result.sphere.color.CopyFrom(
        _serializeColorProperty(sphere.color, f".{sphere.name}_color", project, state)
    )
    if sphere.position is not None:
        result.sphere.position.CopyFrom(
            _serializeVectorProperty(sphere.position, f".{sphere.name}_position", project)
        )
    result.sphere.radius.CopyFrom(
        _serializeScalarProperty(sphere.radius, f".{sphere.name}_radius", project)
    )
    # done
    return result


def _serializeTube(tube: Tube, project: Project, state: SimpleNamespace) -> proto.Animatible:
    result = _createAnimatable(tube, project)
    # properties
    result.tube.color.CopyFrom(
        _serializeColorProperty(tube.color, f".{tube.name}_color", project, state)
    )
    result.tube.radius.CopyFrom(
        _serializeScalarProperty(tube.radius, f".{tube.name}_radius", project)
    )
    result.tube.isGrowing = tube.isGrowing
    # path
    if isinstance(tube.path, Path):
        # Check if already present in project
        # -> Either fetch path id or add path
        if tube.path in project.paths:
            id = project.paths.index(tube.path)
            result.tube.pathId = id
        else:
            id = len(project.paths)
            project.paths.append(tube.path)
            result.tube.pathId = id
    else:
        # path like, but not a path -> create new path
        id = len(project.paths)
        project.paths.append(Path(tube.path, f".{tube.name}_path"))
        result.tube.pathId = id
    # done
    return result


def _serializeLine(line: Line, project: Project, state: SimpleNamespace) -> proto.Animatible:
    result = _createAnimatable(line, project)
    # properties
    result.line.color.CopyFrom(
        _serializeColorProperty(line.color, f".{line.name}_color", project, state)
    )
    if line.start is not None:
        result.line.start.CopyFrom(
            _serializeVectorProperty(line.start, f".{line.name}_start", project)
        )
    if line.end is not None:
        result.line.end.CopyFrom(_serializeVectorProperty(line.end, f".{line.name}_end", project))
    result.line.lineWidth.CopyFrom(
        _serializeScalarProperty(line.lineWidth, f".{line.name}_lineWidth", project)
    )
    result.line.pointForward = line.pointForward
    result.line.pointBackward = line.pointBackward
    # done
    return result


def _serializePrism(prism: Prism, project: Project, state: SimpleNamespace) -> proto.Animatible:
    result = _createAnimatable(prism, project)
    # properties
    result.prism.color.CopyFrom(
        _serializeColorProperty(prism.color, f".{prism.name}_color", project, state)
    )
    if prism.position is not None:
        result.prism.position.CopyFrom(
            _serializeVectorProperty(prism.position, f".{prism.name}_position", project)
        )
    if prism.normal is not None:
        result.prism.normal.CopyFrom(
            _serializeVectorProperty(prism.normal, f".{prism.name}_normal", project)
        )
    result.prism.rotation.CopyFrom(
        _serializeScalarProperty(prism.rotation, f".{prism.name}_rotation", project)
    )
    result.prism.radius.CopyFrom(
        _serializeScalarProperty(prism.radius, f".{prism.name}_radius", project)
    )
    result.prism.height.CopyFrom(
        _serializeScalarProperty(prism.height, f".{prism.name}_height", project)
    )
    result.prism.nVertices = prism.nVertices
    # done
    return result


def _serializeOverlay(overlay: Overlay, project: Project) -> proto.Animatible:
    result = _createAnimatable(overlay, project)
    # properties
    assert overlay.name is not None  # redundant but keeps mypy happy
    result.overlay.text = _serializeText(overlay.text, overlay.name, project)
    _serializeTextPosition(result.overlay, overlay.position)
    result.overlay.fontSize.CopyFrom(
        _serializeScalarProperty(overlay.fontSize, f".{overlay.name}_fontSize", project)
    )
    result.overlay.bold = overlay.bold
    result.overlay.italic = overlay.italic

    # done
    return result
