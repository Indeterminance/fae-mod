
# exceptions.rpy
# This file contains the exceptions for certain DDLC/Template errors
# DO NOT MODIFY THIS FILE!

python early:
    
    class NotRenPyEight(Exception):
        def __str__(self):
            return "This version of the mod template is designed for Ren'Py 8.\nEither build/run your mod on Ren'Py 8, or install the 'py2' mod template instead from scratch."

    class DDLCRPAsMissing(Exception):
        def __init__(self, archive):
            self.archive = archive

        def __str__(self):
            return "'" + self.archive + ".rpa' was not found in the game folder. Check your DDLC installation for missing RPAs and try again."

    class IllegalModLocation(Exception):
        def __str__(self):
            return "DDLC mods/mod projects cannot be run from a cloud folder. Move your mod/mod project to another location and try again."
