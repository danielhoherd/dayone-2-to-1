# dayone 2-to-1

Convert DayOne2 journal.json to DayOne Classic plist files.


# Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ git clone https://github.com/danielhoherd/dayone-2-to-1
    $ cd dayone-2-to-1
    $ pipsi install .


# Usage

To use it:

    $ dayone-2-to-1 --help

# Limitations

- Not all metadata is converted.
- Image files are not handled.

# TODO:

- Add logging
- Write tests
- Make classes for v1 and v2 for uses other than just conversion
