from distutils.core import setup, Extension

module1 = Extension(
        'chessmoves',
        sources = [
                'Source/chessmovesmodule.c',
                'Source/Board.c',
                'Source/Polyglot.c',
                'Source/stringCopy.c'],
        extra_compile_args = ['-std=c99', '-pedantic']
)

setup(
        name         = 'chessmoves',
        version      = '1.0a',
        description  = 'Package to generate chess positions and moves (FEN/SAN/UCI)',
        author       = 'Marcel van Kervinck',
        author_email = 'marcelk@bitpit.net',
        url          = 'http://marcelk.net/chessmoves',
        ext_modules  = [module1])
