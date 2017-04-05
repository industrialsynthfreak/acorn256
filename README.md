# acorn256
Acorn256 (Archimedes Computers) color palette converter. Converts between Acorn256/16 and RGB256 / HTML / HSV color formats.

ACORN256 / ACORN16 default color palettes, which were implemented in 'Acorn Archimedes' computers. Because obviously there are no complete match between 8-bit and 24-bit palettes, some of the RGB / HTML / HSV values provided will return None.
One should not use this code to convert between rgb and html and etc. because only values, that match Acorn palette, going to be converted.

## Syntax
> convert([input_format], [output_format], [value], [optional: palette])
>  - input_format, output_format - any of: 'hsv', 'rgb', 'acorn', 'html'
>  - value - must match the input format conventions, '#FFFFFF' for html, 0-255 for acorn256 and 0-15 for acorn16, tuple of UInt8 for hsv or rgb
>  - palette - 'acorn16' or 'acorn256', default is acorn256

## Examples
From interpreter / script:
```python
from acorn256 import convert
acorn256.convert('acorn', 'html', 42)
'#226666'
```
From the terminal:
```bash
$ python3 acorn256.py rgb acorn '(255, 255, 255)'
255
```
Of course you can make an executable from it:
```bash
$ mv acorn256.py acorn256
$ chmod u+x acorn256
$ ./acorn256 rgb acorn '(255,255,255)' acorn16
0
```

