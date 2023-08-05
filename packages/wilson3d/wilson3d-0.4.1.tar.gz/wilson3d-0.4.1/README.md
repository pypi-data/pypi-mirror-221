# <img src="public/banner.png" height=150>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Wilson is a 3D visualization tool aimed for (astro) particle physics. It
provides a python package for creating event files / catalogues and a static web
based app for viewing them in your browser written using TypeScript.

[Live Demo](https://tkerscher.github.io/wilson?cat=tutorial)

[Documentation](https://tkerscher.github.io/wilson/docs/)

GitHub has a quota, so please don't use the demo productively. Otherwise I might
have to remove it.

## Installation

### Python Package

From the root directory of the repository run:

```bash
pip install .
```

### Deploy Web App

For deployment, it's enough to just copy the build files onto your server. Since
it's a static app, a simple file serving is enough.

If you want to locally run the app, you must run a local http server. Python
already provides one:

```bash
python -m http.server -d {path to wilson}
```

## Building

### Python

For Python see [Installation: Python](#python-package)

### Web App

1. Install [yarn](https://classic.yarnpkg.com/lang/en/docs/install/).
It will handle all further steps for you through its CLI.
2. Fetch dependencies by running `yarn` from the repository root
3. Issue the build command via `yarn build`
4. The build files are now in the `dist` subdirectory.

### Documentation

The documentation is generated via [Sphinx](https://www.sphinx-doc.org/en/master/).
To install the necessary dependencies you can simply run:

```bash
pip install -r docs/requirements.txt
```

Afterwards you can build the documentation via

```bash
cd docs
make html
```

## Code Style

The repository uses static code analyzing tools like linters. Namely they are:

- [ESLint](https://eslint.org/)
- [MyPy](http://mypy-lang.org/)
- [Black](https://github.com/psf/black)

There exist yarn scripts for easier use:

```bash
yarn lint # typescript
yarn black # python black
```

## File Format

See [proto](/proto) for a detailed description of the event file format.

## Dependencies

### Python Dependencies

#### Python Build Dependencies

- [cmasher](https://cmasher.readthedocs.io/)
- [numpy](https://numpy.org/)
- [protobuf](https://developers.google.com/protocol-buffers/)

### Python Develop Dependencies

- [black](https://github.com/psf/black)
- [mypy](http://mypy-lang.org/)
- [sphinx](https://www.sphinx-doc.org/en/master/)
- [types-protobuf](https://pypi.org/project/types-protobuf/)
  
### Web App Dependencies

#### TypeScript Build Dependencies

- [BabylonJS](https://www.babylonjs.com/)
- [JSZip](https://github.com/Stuk/jszip)
- [Mitt](https://github.com/developit/mitt)
- [Pinia](https://pinia.vuejs.org/)
- [Plotly](https://plotly.com/javascript/)
- [protobuf.js](https://github.com/protobufjs/protobuf.js/)
- [sprintf.js](https://github.com/alexei/sprintf.js)
- [Vue.js](https://vuejs.org/)

#### TypeScript Develop Dependencies

- [ESLint](https://eslint.org/)
- [ts-proto](https://github.com/stephenh/ts-proto)
- [Vite](https://vitejs.dev/)
