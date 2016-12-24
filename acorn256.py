#!/usr/bin/python3
"""
This code converts colors between RGB256, HTML, HSV and ACORN256 / ACORN16.

ACORN256 / ACORN16 default color palettes, which were implemented in
'Acorn Archimedes' computers.
Because obviously there are no complete match between 8-bit and 24-bit
palettes, some of the RGB / HTML / HSV values provided will return None.

convert([input_format], [output_format], [value], [optional: palette])
	input_format, output_format - any of: 'hsv', 'rgb', 'acorn', 'html'
	value - must match the input format conventions, '#FFFFFF' for html, etc.
	palette - 'acorn16' or 'acorn256'

Examples.

From interpreter / script:
>>>acorn256.convert('acorn', 'html', 42)
'#226666'

From bash console:
$ python3 acorn256.py rgb acorn '(255, 255, 255)'
255

"""

import table16
import table256

_variants = ('acorn', 'html', 'rgb', 'hsv')
_tables = {'acorn16': table16.color_table, 'acorn256': table256.color_table}


def convert(input_format, output_format, value, palette='acorn256'):
    color_table = _tables[palette]
    if input_format == 'html':
        value = value.upper()
    _in = _variants.index(input_format)
    _out = _variants.index(output_format)

    for values in color_table:
        if values[_in] == value:
            return values[_out]
    else:
        return None


if __name__ == '__main__':
    # to use from the terminal
    import sys

    try:
        inp, out, value, palette = sys.argv[1:5]
        inp = inp.lower()
        out = out.lower()
        if inp not in _variants or out not in _variants:
            raise ValueError
        if inp == 'acorn':
            value = int(value)
        if inp in ('rgb', 'hsv'):
            value = value.strip()
            value = value[1:-1].split(',')
            value = tuple((int(v.strip()) for v in value))
        sys.stdout.write('%s\n' % convert(inp, out, value))
    except ValueError:
        print("Bad arguments.")
    finally:
        sys.exit(0)
