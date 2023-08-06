#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022-2023 Marcel Werner.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from lark import Lark, tree
from pathlib import Path
import os
import site

def translation(
        src: Path,
        dir_path: Path,
        txt: bool = False,
        dot: bool = False,
        beckhoff: bool = False):

    # Get the list of all global site-packages directories
    site_packages_dirs = site.getsitepackages()

    if beckhoff:
        # Define the relative path to your file from the site-packages directory
        rel_path = "plcrex\data\grammars\STgrammar_Beckhoff.lark"

        # Iterate over all site-packages directories
        for dir in site_packages_dirs:
            # Create an absolute path to the file
            abs_file_path = os.path.join(dir, rel_path)

            print(abs_file_path)

            # Check if the file exists at this path
            if os.path.isfile(abs_file_path):
                # If the file exists, open it
                with open(abs_file_path, 'rt') as file:
                    grammar = file.read()
                    file.close()
                break
        #with open(r'.\plcrex\data\grammars\STgrammar_Beckhoff.lark', 'rt') as file:
        #    grammar = file.read()
    else:
        # Define the relative path to your file from the site-packages directory
        rel_path = "plcrex\data\grammars\STgrammar.lark"

        # Iterate over all site-packages directories
        for dir in site_packages_dirs:
            # Create an absolute path to the file
            abs_file_path = os.path.join(dir, rel_path)

            print(abs_file_path)

            # Check if the file exists at this path
            if os.path.isfile(abs_file_path):
                # If the file exists, open it
                with open(abs_file_path, 'rt') as file:
                    grammar = file.read()
                    file.close()
                break
        #with open(r'.\plcrex\data\grammars\STgrammar.lark', 'rt') as file:
            #grammar = file.read()
    parser = Lark(grammar, maybe_placeholders=False, keep_all_tokens=False)

    with open(src, 'rt') as file:
        source = file.read()

        # write (pretty) tree as .txt
        if txt:
            txt_export = open(fr'{dir_path}\{Path(src).name}.txt', "w")
            txt_export.write(str(parser.parse(source).pretty()))

        # write tree as .dot file
        if dot:
            tree.pydot__tree_to_dot(parser.parse(source), fr'{dir_path}\{Path(src).name}.dot')
        return
