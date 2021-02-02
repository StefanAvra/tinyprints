ALLOWED_CHARS = [
    # code page 437
    # pparently the printer can print all these letters. this needs some testing
    0x0057,  # LATIN CAPITAL LETTER W
    0x0058,  # LATIN CAPITAL LETTER X
    0x0059,  # LATIN CAPITAL LETTER Y
    0x005a,  # LATIN CAPITAL LETTER Z
    0x005b,  # LEFT SQUARE BRACKET
    0x005c,  # REVERSE SOLIDUS
    0x005d,  # RIGHT SQUARE BRACKET
    0x005e,  # CIRCUMFLEX ACCENT
    0x005f,  # LOW LINE
    0x0060,  # GRAVE ACCENT
    0x0061,  # LATIN SMALL LETTER A
    0x0062,  # LATIN SMALL LETTER B
    0x0063,  # LATIN SMALL LETTER C
    0x0064,  # LATIN SMALL LETTER D
    0x0065,  # LATIN SMALL LETTER E
    0x0066,  # LATIN SMALL LETTER F
    0x0067,  # LATIN SMALL LETTER G
    0x0068,  # LATIN SMALL LETTER H
    0x0069,  # LATIN SMALL LETTER I
    0x006a,  # LATIN SMALL LETTER J
    0x006b,  # LATIN SMALL LETTER K
    0x006c,  # LATIN SMALL LETTER L
    0x006d,  # LATIN SMALL LETTER M
    0x006e,  # LATIN SMALL LETTER N
    0x006f,  # LATIN SMALL LETTER O
    0x0070,  # LATIN SMALL LETTER P
    0x0071,  # LATIN SMALL LETTER Q
    0x0072,  # LATIN SMALL LETTER R
    0x0073,  # LATIN SMALL LETTER S
    0x0074,  # LATIN SMALL LETTER T
    0x0075,  # LATIN SMALL LETTER U
    0x0076,  # LATIN SMALL LETTER V
    0x0077,  # LATIN SMALL LETTER W
    0x0078,  # LATIN SMALL LETTER X
    0x0079,  # LATIN SMALL LETTER Y
    0x007a,  # LATIN SMALL LETTER Z
    0x007b,  # LEFT CURLY BRACKET
    0x007c,  # VERTICAL LINE
    0x007d,  # RIGHT CURLY BRACKET
    0x007e,  # TILDE
    0x007f,  # DELETE
    0x00c7,  # LATIN CAPITAL LETTER C WITH CEDILLA
    0x00fc,  # LATIN SMALL LETTER U WITH DIAERESIS
    0x00e9,  # LATIN SMALL LETTER E WITH ACUTE
    0x00e2,  # LATIN SMALL LETTER A WITH CIRCUMFLEX
    0x00e4,  # LATIN SMALL LETTER A WITH DIAERESIS
    0x00e0,  # LATIN SMALL LETTER A WITH GRAVE
    0x00e5,  # LATIN SMALL LETTER A WITH RING ABOVE
    0x00e7,  # LATIN SMALL LETTER C WITH CEDILLA
    0x00ea,  # LATIN SMALL LETTER E WITH CIRCUMFLEX
    0x00eb,  # LATIN SMALL LETTER E WITH DIAERESIS
    0x00e8,  # LATIN SMALL LETTER E WITH GRAVE
    0x00ef,  # LATIN SMALL LETTER I WITH DIAERESIS
    0x00ee,  # LATIN SMALL LETTER I WITH CIRCUMFLEX
    0x00ec,  # LATIN SMALL LETTER I WITH GRAVE
    0x00c4,  # LATIN CAPITAL LETTER A WITH DIAERESIS
    0x00c5,  # LATIN CAPITAL LETTER A WITH RING ABOVE
    0x00c9,  # LATIN CAPITAL LETTER E WITH ACUTE
    0x00e6,  # LATIN SMALL LIGATURE AE
    0x00c6,  # LATIN CAPITAL LIGATURE AE
    0x00f4,  # LATIN SMALL LETTER O WITH CIRCUMFLEX
    0x00f6,  # LATIN SMALL LETTER O WITH DIAERESIS
    0x00f2,  # LATIN SMALL LETTER O WITH GRAVE
    0x00fb,  # LATIN SMALL LETTER U WITH CIRCUMFLEX
    0x00f9,  # LATIN SMALL LETTER U WITH GRAVE
    0x00ff,  # LATIN SMALL LETTER Y WITH DIAERESIS
    0x00d6,  # LATIN CAPITAL LETTER O WITH DIAERESIS
    0x00dc,  # LATIN CAPITAL LETTER U WITH DIAERESIS
    0x00a2,  # CENT SIGN
    0x00a3,  # POUND SIGN
    0x00a5,  # YEN SIGN
    0x20a7,  # PESETA SIGN
    0x0192,  # LATIN SMALL LETTER F WITH HOOK
    0x00e1,  # LATIN SMALL LETTER A WITH ACUTE
    0x00ed,  # LATIN SMALL LETTER I WITH ACUTE
    0x00f3,  # LATIN SMALL LETTER O WITH ACUTE
    0x00fa,  # LATIN SMALL LETTER U WITH ACUTE
    0x00f1,  # LATIN SMALL LETTER N WITH TILDE
    0x00d1,  # LATIN CAPITAL LETTER N WITH TILDE
    0x00aa,  # FEMININE ORDINAL INDICATOR
    0x00ba,  # MASCULINE ORDINAL INDICATOR
    0x00bf,  # INVERTED QUESTION MARK
    0x2310,  # REVERSED NOT SIGN
    0x00ac,  # NOT SIGN
    0x00bd,  # VULGAR FRACTION ONE HALF
    0x00bc,  # VULGAR FRACTION ONE QUARTER
    0x00a1,  # INVERTED EXCLAMATION MARK
    0x00ab,  # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00bb,  # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x2591,  # LIGHT SHADE
    0x2592,  # MEDIUM SHADE
    0x2593,  # DARK SHADE
    0x2502,  # BOX DRAWINGS LIGHT VERTICAL
    0x2524,  # BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0x2561,  # BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
    0x2562,  # BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE
    0x2556,  # BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE
    0x2555,  # BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE
    0x2563,  # BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    0x2551,  # BOX DRAWINGS DOUBLE VERTICAL
    0x2557,  # BOX DRAWINGS DOUBLE DOWN AND LEFT
    0x255d,  # BOX DRAWINGS DOUBLE UP AND LEFT
    0x255c,  # BOX DRAWINGS UP DOUBLE AND LEFT SINGLE
    0x255b,  # BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
    0x2510,  # BOX DRAWINGS LIGHT DOWN AND LEFT
    0x2514,  # BOX DRAWINGS LIGHT UP AND RIGHT
    0x2534,  # BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0x252c,  # BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0x251c,  # BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0x2500,  # BOX DRAWINGS LIGHT HORIZONTAL
    0x253c,  # BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x255e,  # BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
    0x255f,  # BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
    0x255a,  # BOX DRAWINGS DOUBLE UP AND RIGHT
    0x2554,  # BOX DRAWINGS DOUBLE DOWN AND RIGHT
    0x2569,  # BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    0x2566,  # BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    0x2560,  # BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    0x2550,  # BOX DRAWINGS DOUBLE HORIZONTAL
    0x256c,  # BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    0x2567,  # BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
    0x2568,  # BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
    0x2564,  # BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE
    0x2565,  # BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE
    0x2559,  # BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
    0x2558,  # BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
    0x2552,  # BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
    0x2553,  # BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE
    0x256b,  # BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE
    0x256a,  # BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
    0x2518,  # BOX DRAWINGS LIGHT UP AND LEFT
    0x250c,  # BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x2588,  # FULL BLOCK
    0x2584,  # LOWER HALF BLOCK
    0x258c,  # LEFT HALF BLOCK
    0x2590,  # RIGHT HALF BLOCK
    0x2580,  # UPPER HALF BLOCK
    0x03b1,  # GREEK SMALL LETTER ALPHA
    0x00df,  # LATIN SMALL LETTER SHARP S
    0x0393,  # GREEK CAPITAL LETTER GAMMA
    0x03c0,  # GREEK SMALL LETTER PI
    0x03a3,  # GREEK CAPITAL LETTER SIGMA
    0x03c3,  # GREEK SMALL LETTER SIGMA
    0x00b5,  # MICRO SIGN
    0x03c4,  # GREEK SMALL LETTER TAU
    0x03a6,  # GREEK CAPITAL LETTER PHI
    0x0398,  # GREEK CAPITAL LETTER THETA
    0x03a9,  # GREEK CAPITAL LETTER OMEGA
    0x03b4,  # GREEK SMALL LETTER DELTA
    0x221e,  # INFINITY
    0x03c6,  # GREEK SMALL LETTER PHI
    0x03b5,  # GREEK SMALL LETTER EPSILON
    0x2229,  # INTERSECTION
    0x2261,  # IDENTICAL TO
    0x00b1,  # PLUS-MINUS SIGN
    0x2265,  # GREATER-THAN OR EQUAL TO
    0x2264,  # LESS-THAN OR EQUAL TO
    0x2320,  # TOP HALF INTEGRAL
    0x2321,  # BOTTOM HALF INTEGRAL
    0x00f7,  # DIVISION SIGN
    0x2248,  # ALMOST EQUAL TO
    0x00b0,  # DEGREE SIGN
    0x2219,  # BULLET OPERATOR
    0x00b7,  # MIDDLE DOT
    0x221a,  # SQUARE ROOT
    0x207f,  # SUPERSCRIPT LATIN SMALL LETTER N
    0x00b2,  # SUPERSCRIPT TWO
    0x25a0,  # BLACK SQUARE
    0x00a0,  # NO-BREAK SPACE
]