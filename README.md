# Creating CLDF data for SegBo using cldfbench

## Overview

This file documents how we create CLDF data format for the SegBo database:

* https://github.com/segbo-db/segbo*

We foloow the `cldfbench` tutorial:

* https://github.com/cldf/cldfbench/blob/master/doc/tutorial.md

See also:

* https://github.com/cldf/cldfbench
* https://cldf.clld.org/
* https://pure.mpg.de/pubman/item/item_3231858_1/component/file_3231859/shh2600.pdf


## Steps taken

First follow the instructions and install the command line tool.

* https://pypi.org/project/cldfbench/

Next, we followed the instructions in the tutorial.

```shell script
cldfbench new
```

Here we give the ID "SegBo" and `cldfbench` creates the file structure.

```
├── __pycache__
│   └── test.cpython-38.pyc
├── cldf
│   └── README.md
├── cldfbench_SegBo.py
├── etc
│   └── README.md
├── metadata.json
├── raw
│   └── README.md
├── setup.cfg
├── setup.py
└── test.py
```

The `cldfbench` tutorial then instructs us to edit the `SegBo/cldfbench_SegBo.py` Python file, for example to update the the `cmd_download` function to download the SegBo data to the `SegBo/raw` folder.

`cldfbench download SegBo/cldfbench_SegBo.py`

Next, we implement the `cmd_makecldf` function to create a `StructureDataset`.

Note that one also needs to clone Glottolog:

* https://github.com/glottolog/glottolog

And install `pyglottolog`.

* https://pypi.org/project/pyglottolog/

`cldfbench makecldf SegBo/cldfbench_SegBo.py --glottolog ../glottolog`


