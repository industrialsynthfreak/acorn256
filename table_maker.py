#!/usr/bin/python3
"""
This module is used to produce a python-style color table from the original
tab-separated text table. This is the only purpose of this program.

"""

import warnings

header = '''# Acorn256 | HTML | RGB256 | HSV color mapping table

color_table = ('''


def parse_table(input_path='table256', output_path='table256.py'):
    try:
        input_file = open(input_path, 'r')
        output_file = open(output_path, 'w')
        output_file.write(header)

        for line in input_file:
            try:
                data = line.split()
                gridpos, color_number, hsv, html, rgb, rgb_256 = data[:6]
                hsv = ', '.join(hsv.split(','))
                rgb_256 = ', '.join(rgb_256.split(','))
            except ValueError:
                warnings.warn('A processing problem have occured. Check your'
                              '{proc} file'.format(proc=output_path))
                continue
            text = '\n\t({n}, {h}, ({r}), ({hs})),'.format(
                n=color_number, h=html, r=rgb_256, hs=hsv)
            output_file.write(text)

        output_file.write('\n)\n')

    except (OSError, IOError) as e:
        print('Problems occurred while accessing file.')
    finally:
        input_file.close()
        output_file.close()


if __name__ == "__main__":
    parse_table()
