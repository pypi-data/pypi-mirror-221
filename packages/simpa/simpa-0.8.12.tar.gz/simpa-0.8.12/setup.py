# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simpa',
 'simpa.core',
 'simpa.core.device_digital_twins',
 'simpa.core.device_digital_twins.detection_geometries',
 'simpa.core.device_digital_twins.illumination_geometries',
 'simpa.core.device_digital_twins.pa_devices',
 'simpa.core.processing_components',
 'simpa.core.processing_components.monospectral',
 'simpa.core.processing_components.monospectral.noise',
 'simpa.core.processing_components.multispectral',
 'simpa.core.simulation_modules',
 'simpa.core.simulation_modules.acoustic_forward_module',
 'simpa.core.simulation_modules.optical_simulation_module',
 'simpa.core.simulation_modules.reconstruction_module',
 'simpa.core.simulation_modules.volume_creation_module',
 'simpa.io_handling',
 'simpa.log',
 'simpa.utils',
 'simpa.utils.libraries',
 'simpa.utils.libraries.absorption_spectra_data',
 'simpa.utils.libraries.anisotropy_spectra_data',
 'simpa.utils.libraries.scattering_spectra_data',
 'simpa.utils.libraries.structure_library',
 'simpa.utils.quality_assurance',
 'simpa.visualisation',
 'simpa_tests',
 'simpa_tests.automatic_tests',
 'simpa_tests.automatic_tests.device_tests',
 'simpa_tests.automatic_tests.structure_tests',
 'simpa_tests.automatic_tests.tissue_library',
 'simpa_tests.manual_tests',
 'simpa_tests.manual_tests.acoustic_forward_models',
 'simpa_tests.manual_tests.digital_device_twins',
 'simpa_tests.manual_tests.image_reconstruction',
 'simpa_tests.manual_tests.optical_forward_models',
 'simpa_tests.manual_tests.processing_components',
 'simpa_tests.manual_tests.test_with_experimental_measurements',
 'simpa_tests.manual_tests.volume_creation',
 'simpa_tests.test_utils']

package_data = \
{'': ['*'],
 'simpa_tests': ['checklists/*'],
 'simpa_tests.manual_tests.test_with_experimental_measurements': ['test_data/*']}

install_requires = \
['Deprecated>=1.2.13',
 'coverage>=6.1.2',
 'h5py>=3.6.0',
 'jdata>=0.5.2',
 'matplotlib>=3.5.0',
 'numpy>=1.21.4',
 'pacfish>=0.4.4',
 'pandas>=1.3.4',
 'pynrrd>=0.4.2',
 'python-dotenv>=0.19.2',
 'requests>=2.26.0',
 'scikit-image>=0.18.3',
 'scipy>=1.7.2',
 'torch>=1.10.0',
 'wget>=3.2',
 'xmltodict>=0.12.0']

setup_kwargs = {
    'name': 'simpa',
    'version': '0.8.12',
    'description': 'Simulation and Image Processing for Photonics and Acoustics',
    'long_description': '[![Documentation Status](https://readthedocs.org/projects/simpa/badge/?version=develop)](https://simpa.readthedocs.io/en/develop/?badge=develop)\n![Build Status](https://github.com/IMSY-DKFZ/simpa/actions/workflows/automatic_testing.yml/badge.svg)\n[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/IMSY-DKFZ/simpa/blob/main/LICENSE.md)\n\n[![Pypi Badge](https://img.shields.io/pypi/v/simpa)](https://pypi.org/project/simpa/)\n[![PyPI downloads](https://img.shields.io/pypi/dw/simpa?color=gr&label=pypi%20downloads)](https://pypi.org/project/simpa/)\n\n![Logo](docs/source/images/simpa_logo.png?raw=true "Logo")\n\n# The toolkit for Simulation and Image Processing for Photonics and Acoustics (SIMPA)\n\nSIMPA aims to facilitate realistic image simulation for optical and acoustic imaging modalities by\nproviding adapters to crucial modelling steps, such as volume generation; optical modelling; acoustic\nmodelling; and image reconstruction. SIMPA provides a communication layer between various modules\nthat implement optical and acoustic forward and inverse models.\nNon-experts can use the toolkit to create sensible simulations from default parameters in an end-to-end fashion. Domain experts are provided with the functionality to set up a highly customisable\npipeline according to their specific use cases and tool requirements.\nThe paper that introduces SIMPA including visualisations and explanations can be found here: [https://doi.org/10.1117/1.JBO.27.8.083010](https://doi.org/10.1117/1.JBO.27.8.083010)\n\n* [Getting started](#getting-started)\n* [Simulation examples](#simulation-examples)\n* [Documentation](#documentation)\n* [Contributing](#how-to-contribute)\n* [Performance profiling](#performance-profiling)\n* [Troubleshooting](#troubleshooting)\n* [Citation](#citation)\n* [Funding](#funding)\n\nThe toolkit is still under development and is thus not fully tested and may contain bugs. \nPlease report any issues that you find in our Issue Tracker: https://github.com/IMSY-DKFZ/simpa/issues. \nAlso make sure to double check all value ranges of the optical and acoustic tissue properties \nand to assess all simulation results for plausibility.\n\n# Getting started\n\nIn order to use SIMPA in your project, SIMPA has to be installed as well as the external tools that make the actual simulations possible.\nFinally, to connect everything, SIMPA has to find all the binaries of the simulation modules you would like to use.\nThe SIMPA path management takes care of that.\n\n* [SIMPA installation instructions](#simpa-installation-instructions)\n* [External tools installation instructions](#external-tools-installation-instructions)\n* [Path Management](#path-management)\n\n## SIMPA installation instructions\n\nThe recommended way to install SIMPA is a manual installation from the GitHub repository, please follow steps 1 - 3:\n\n1. `git clone https://github.com/IMSY-DKFZ/simpa.git`\n2. `cd simpa`\n3. `git checkout main`\n4. `git pull`\n\nNow open a python instance in the \'simpa\' folder that you have just downloaded. Make sure that you have your preferred\nvirtual environment activated (we also recommend python 3.8)\n1. `pip install .`\n2. Test if the installation worked by using `python` followed by `import simpa` then `exit()`\n\nIf no error messages arise, you are now setup to use SIMPA in your project.\n\nYou can also install SIMPA with pip. Simply run:\n\n`pip install simpa`\n\nYou also need to manually install the pytorch library to use all features of SIMPA.\nTo this end, use the pytorch website tool to figure out which version to install:\n[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)\n\n## External tools installation instructions\n\nIn order to get the full SIMPA functionality, you should install all third party toolkits that make the optical and \nacoustic simulations possible. \n\n### mcx (Optical Forward Model)\n\nEither download suitable executables or build yourself from the following sources:\n\n[http://mcx.space/](http://mcx.space/)\n\nIn order to obtain access to all custom sources that we implemented, please build mcx yourself from the\nfollowing mcx Github fork:\n[https://github.com/IMSY-DKFZ/mcx](https://github.com/IMSY-DKFZ/mcx)\n\nFor the installation, please follow steps 1-4:\n1. `git clone https://github.com/IMSY-DKFZ/mcx.git`\n2. `cd mcx/src`\n3. In `MAKEFILE` adapt line 111 the sm version [according to your GPU](https://arnon.dk/matching-sm-architectures-arch-and-gencode-for-various-nvidia-cards/).\n4. `make`\n\nThe built binary can be found in `src/bin`.\nNote, in case you can’t build mcx with the GPU-specific sm version you need to install a more recent NVIDIA driver and nvcc toolkit. \nOne option would be to install cuda in a conda environment via `conda install cuda -c nvidia`.\nPlease note that there might be compatibility issues using mcx-cl with the MCX Adapter as this use case is not \nbeing tested and supported by the SIMPA developers.\n\n### k-Wave (Acoustic Forward Model)\n\nPlease follow the following steps and use the k-Wave install instructions \nfor further (and much better) guidance under:\n\n[http://www.k-wave.org/](http://www.k-wave.org/)\n\n1. Install MATLAB with the core, image processing and parallel computing toolboxes activated at the minimum.\n2. Download the kWave toolbox (version >= 1.4)\n3. Add the kWave toolbox base path to the toolbox paths in MATLAB\n4. If wanted: Download the CPP and CUDA binary files and place them in the k-Wave/binaries folder\n5. Note down the system path to the `matlab` executable file.\n\n## Path management\n\nAs a pipelining tool that serves as a communication layer between different numerical forward models and\nprocessing tools, SIMPA needs to be configured with the paths to these tools on your local hard drive.\nTo this end, we have implemented the `PathManager` class that you can import to your project using\n`from simpa.utils import PathManager`. The PathManager looks for a `path_config.env` file (just like the\none we provided in the `simpa_examples`) in the following places in this order:\n1. The optional path you give the PathManager\n2. Your $HOME$ directory\n3. The current working directory\n4. The SIMPA home directory path\n\nPlease follow the instructions in the `path_config.env` file in the `simpa_examples` folder. \n\n# Simulation examples\n\nTo get started with actual simulations, SIMPA provides an [example package](simpa_examples) of simple simulation \nscripts to build your custom simulations upon. The [minimal optical simulation](simpa_examples/minimal_optical_simulation.py)\nis a nice start if you have MCX installed.\n\nGenerally, the following pseudo code demonstrates the construction and run of a simulation pipeline:\n\n```python\nimport simpa as sp\n\n# Create general settings \nsettings = sp.Settings(general_settings)\n\n# Create specific settings for each pipeline element \n# in the simulation pipeline\nsettings.set_volume_creation_settings(volume_creation_settings)\nsettings.set_optical_settings(optical_settings)\nsettings.set_acoustic_settings(acoustic_settings)\nsettings.set_reconstruction_settings(reconstruction_settings)\n\n# Set the simulation pipeline\nsimulation_pipeline = [sp.VolumeCreatorModule(settings),\n    sp.OpticalForwardModule(settings),\n    sp.AcousticForwardModule(settings),\n    sp.ReconstructionModule(settings)]\n    \n# Choose a PA device with device position in the volume\ndevice = sp.CustomDevice()\n\n# Simulate the pipeline\nsp.simulate(simulation_pipeline, settings, device)\n```\n\n# Documentation\n\nThe updated version of the SIMPA documentation can be found at [https://simpa.readthedocs.io/en/develop](https://simpa.readthedocs.io/en/develop).\n\n## Building the documentation\n\nIt is also easily possible to build the SIMPA documentation from scratch.\nWhen the installation succeeded, and you want to make sure that you have the latest documentation\nyou should do the following steps in a command line:\n\n1. Navigate to the `simpa/docs` directory\n2. If you would like the documentation to have the https://readthedocs.org/ style, type `pip install sphinx-rtd-theme`\n3. Type `make html`\n4. Open the `index.html` file in the `simpa/docs/build/html` directory with your favourite browser.\n\n# How to contribute\n\nPlease find a more detailed description of how to contribute as well as code style references in our\n[contribution guidelines](CONTRIBUTING.md).\n\nTo contribute to SIMPA, please fork the SIMPA github repository and create a pull request with a branch containing your \nsuggested changes. The core developers will then review the suggested changes and integrate these into the code \nbase.\n\nPlease make sure that you have included unit tests for your code and that all previous tests still run through.\n\nThere is a regular SIMPA status meeting every Friday on even calendar weeks at 10:00 CET/CEST, and you are very welcome to participate and\nraise any issues or suggest new features. If you want to join this meeting, write one of the core developers.\n\nPlease see the github guidelines for creating pull requests: [https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)\n\n\n# Performance profiling\n\nDo you wish to know which parts of the simulation pipeline cost the most amount of time? \nIf that is the case then you can use the following commands to profile the execution of your simulation script.\nYou simply need to replace the `myscript` name with your script name.\n\n`python -m cProfile -o myscript.cprof myscript.py`\n\n`pyprof2calltree -k -i myscript.cprof`\n\n# Troubleshooting\n\nIn this section, known problems are listed with their solutions (if available):\n\n## 1. Error reading hdf5-files when using k-Wave binaries:\n   \nIf you encounter an error similar to:\n\n    Error using h5readc\n    The filename specified was either not found on the MATLAB path or it contains unsupported characters.\n\nLook up the solution in [this thread of the k-Wave forum](http://www.k-wave.org/forum/topic/error-reading-h5-files-when-using-binaries).  \n      \n# Citation\n\nIf you use the SIMPA tool, we would appreciate if you cite our Journal publication in the Journal of Biomedical Optics:\n\nGröhl, Janek, Kris K. Dreher, Melanie Schellenberg, Tom Rix, Niklas Holzwarth, Patricia Vieten, Leonardo Ayala, Sarah E. Bohndiek, Alexander Seitel, and Lena Maier-Hein. *"SIMPA: an open-source toolkit for simulation and image processing for photonics and acoustics."* **Journal of Biomedical Optics** 27, no. 8 (2022).\n\n```Bibtex\n@article{2022simpatoolkit,\n  title={SIMPA: an open-source toolkit for simulation and image processing for photonics and acoustics},\n  author={Gr{\\"o}hl, Janek and Dreher, Kris K and Schellenberg, Melanie and Rix, Tom and Holzwarth, Niklas and Vieten, Patricia and Ayala, Leonardo and Bohndiek, Sarah E and Seitel, Alexander and Maier-Hein, Lena},\n  journal={Journal of Biomedical Optics},\n  volume={27},\n  number={8},\n  year={2022},\n  publisher={SPIE}\n}\n```\n\n# Funding\n\nThis project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. [101002198]).\n\n![ERC](docs/source/images/LOGO_ERC-FLAG_EU_.jpg "ERC")',
    'author': 'Division of Intelligent Medical Systems (IMSY), DKFZ',
    'author_email': 'k.dreher@dkfz-heidelberg.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/IMSY-DKFZ/simpa',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
