# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Emeralds
# Author: Jason Drawdy
# Version: 0.0.1
# Date: 07/21/23
# #########################################################################
# Description:
# Allows the generation of checksums from binary data.
# #########################################################################
from src.tools.logger import Logger
import hashlib

class Hasher:
    """Allows checksum generation of binary data either from a file or message."""
    def __init__(self) -> None:
        """Creates a new hashing object instance to allow checksum generation of files and messages."""
        self._logger = Logger(__name__)

    def get_file_checksum(self: "Hasher", filename: str, block: int = 2**20) -> str:
        """|coro|
        
        Generates a calculated ``SHA512`` hash for a given file.

        Parameters
        ----------
        filename : :class:`str`
            The name of the file to generate the checksum for.
        block : Optional[:class:`int`]
            Chunk size to read and hash the file in bytes. Default is ``2^20``.

        Returns
        ----------
        :class:`str`
            The calculated ``SHA512`` hash of the file, or ``None`` if there was an error generating the checksum.

        Notes
        ----------

        - This function generates a ``SHA512`` hash for a given file by reading the file in blocks and hashing each block.\
        The generated hash is a digest checksum (a unique fixed-sized representation of the file content) and\
        the file is treated as a binary file (read in ``rb`` mode) for proper handling of all types of files. 

        - The reason ``SHA512`` was chosen is purely for the lack of collisions at runtime when performing dynamic checks. 
        """
        try:
            sha512 = hashlib.sha512()
            with open(filename, 'rb') as file:
                while True:
                    data = file.read(block)
                    if not data:
                        break
                    sha512.update(data)
                return sha512.hexdigest()
        except IOError: # pragma: no cover
            self._logger.error("File \'" + filename + "\' not found!")
            return None