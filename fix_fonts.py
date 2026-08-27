#!/usr/bin/env python3
"""Fix font references in generate_textbook_pdf.py to use Georgia TTF fonts with Unicode support."""

import re

with open('generate_textbook_pdf.py', 'r') as f:
    content = f.read()

# 1. Add TTF font imports after the existing import block
old_imports = "from reportlab.lib.colors import HexColor\nimport os"
new_imports = """from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ─── Register Georgia TTF fonts (full Unicode, including Extended Latin) ─────────
font_dir = "/System/Library/Fonts/Supplemental/"
pdfmetrics.registerFont(TTFont('Georgia',            font_dir + 'Georgia.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-Bold',       font_dir + 'Georgia Bold.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-Italic',       font_dir + 'Georgia Italic.ttf'))
pdfmetrics.registerFont(TTFont('Georgia-BoldItalic',   font_dir + 'Georgia Bold Italic.ttf'))"""

content = content.replace(old_imports, new_imports)

# 2. Replace fontName references carefully
# Use regex to match fontName='Times-Bold', fontName="Times-Bold", etc.
replacements = {
    r'fontName\s*=\s*["\']Times-Roman["\']':    'fontName="Georgia"',
    r'fontName\s*=\s*["\']Times-Bold["\']':     'fontName="Georgia-Bold"',
    r'fontName\s*=\s*["\']Times-Italic["\']':   'fontName="Georgia-Italic"',
    r'fontName\s*=\s*["\']Times-BoldItalic["\']': 'fontName="Georgia-BoldItalic"',
    r'fontName\s*=\s*["\']Helvetica["\']':       'fontName="Georgia"',
    r'fontName\s*=\s*["\']Helvetica-Bold["\']':   'fontName="Georgia-Bold"',
}

for pattern, replacement in replacements.items():
    content = re.sub(pattern, replacement, content)

with open('generate_textbook_pdf.py', 'w') as f:
    f.write(content)

print("Done. Font references updated to Georgia TTF.")
