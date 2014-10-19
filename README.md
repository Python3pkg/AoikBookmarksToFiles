# AoikBookmarksToFiles
Convert a bookmark file in NETSCAPE-Bookmark-file-1 format exported from browsers like Chrome and Firefox into a set of Windows ".url" files or Gnome ".desktop" files.

Tested working with:
- Windows, Linux
- Python: 2.7+, 3.3+

[Package on PyPI](https://pypi.python.org/pypi/AoikBookmarksToFiles)

## Contents
- [How to install](#how-to-install)
  - [Install via pip](#install-via-pip)
- [How to use](#how-to-use)
  - [Find the command](#find-the-command)
  - [Run the command](#run-the-command)
- [How to read the funny source code](#how-to-read-the-funny-source-code)

## How to install

### Install via pip
Run
```
pip install AoikBookmarksToFiles
```
or
```
pip install git+https://github.com/AoiKuiyuyou/AoikBookmarksToFiles
```

## How to use
### Find the command
After the [installation](#how-to-install), a command named **aoikbtf** should be available on your console.

### Run the command
Show usage: 
```
aoikbtf -h
```

Convert a bookmark file:
```
aoikbtf bookmarks.html
```

Specify an output dir.  
By default, output files are put in working dir.
```
aoikbtf bookmarks.html -d output_dir
```

Output Gnome **.desktop** files.  
By default output Windows **.url** files.
```
aoikbtf bookmarks.html --fm-de
```

Name output files by page title.  
By default name by page URL.
```
aoikbtf bookmarks.html --nbt
```

Convert invalid characters in output file name to empty.  
By default, convert to % escape.
```
aoikbtf bookmarks.html --ete
```

Convert invalid characters in output file name to spaces.  
By default, convert to % escape.
```
aoikbtf bookmarks.html --ets
```

Specify stdin, stdout, and stderr encoding.  
If given, overrides env var **PYTHONIOENCODING**.
```
aoikbtf bookmarks.html --stdioe utf-8
```

Specify stdin encoding.  
If given, overrides env var **PYTHONIOENCODING**.
```
aoikbtf bookmarks.html --stdie utf-8
```

Specify stdout encoding.  
If given, overrides env var **PYTHONIOENCODING**.
```
aoikbtf bookmarks.html --stdoe utf-8
```

Specify stderr encoding.  
If given, overrides env var **PYTHONIOENCODING**.
```
aoikbtf bookmarks.html --stdee utf-8
```

Specify cmd arg encoding.  
By default same as default locale encoding.
```
aoikbtf bookmarks.html --cae utf-8
```

Specify input file encoding.  
By default utf-8.
```
aoikbtf bookmarks.html --ife utf-8
```

Specify output file encoding.  
By default utf-8.
```
aoikbtf bookmarks.html --ofe utf-8
```

Show encoding info:
```
aoikbtf --ei
```

Specify localization locale.  
Currently English, Chinese, and Japanese languages are supported.  
By default **en** locale is used.
```
aoikbtf bookmarks.html -l en
aoikbtf bookmarks.html -l zh
aoikbtf bookmarks.html -l ja
```

Select localization locale automatically:
```
aoikbtf bookmarks.html --la
```

Show localization locale choices:
```
aoikbtf --lc
```

Show localization locale info:
```
aoikbtf --li
```

Enable debug mode to show debugging info:
```
aoikbtf bookmarks.html --debug
```

## How to read the funny source code
For developers interested in reading the source code,  
Here is a flowchart ([.png](/doc/dev/main.png?raw=true), [.svg](/doc/dev/main.svg?raw=true), or [.graphml](/doc/dev/main.graphml?raw=true)) that has recorded key steps of the program.  
![Image](/doc/dev/main.png?raw=true)

The flowchart is produced using free graph editor [yEd](http://www.yworks.com/en/products_yed_download.html).

If you want to copy the text in the graph, it's recommended to download the [.svg](/doc/dev/main.svg?raw=true) file and open it locally in your browser. (For security reason, Github has disabled rendering of SVG images on the page.)

The meaning of the shapes in the flowchart should be straightforward.  
One thing worth mentioning is isosceles trapezium means sub-steps.

The most useful feature of the flowchart is, for each step in it,
there is a 7-character ID.  
This ID can be used to locate (by text searching) the code that implements a step.  
This mechanism has two merits:

1. It has provided **precise** (locating precision is line-level)
  and **fast** (text searching is fast) mapping from doc to code, which is
  very handy for non-trivial project.

  Without it you have to rely on developers' memory to recall the code locations (*Will you recall them after several months, precise and fast?*).

2. It has provided **precise** (unique ID) and **concise** (7-character long) names
  for each steps of a program, which is very handy for communicating between
  members of a development team.

  Without it describing some steps of a program between team members tends to be unclear.
