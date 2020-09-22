import setuptools, json, pathlib, os

"""
[USAGE]:
# First
    * python3.7 -m pip install --upgrade pip setuptools wheel

# Source Distribution - Recompile on any platform
    * python3.7 setup.py sdist

# Built Distribution - Archive to a specific platform (Ex: linux-x86_64)
    * python3.7 setup.py bdist_wheel
"""

PROJECT             = pathlib.Path(__file__).resolve().parents[0]
GET_DATA_FILES      = lambda folder: "\n".join( [ f"""include { x[0].replace(f'{ str(PROJECT) }/','') }/*""" for x in os.walk( f"{ PROJECT }/{ folder }" ) ] )

MANIFEST_TEXT = f"""
include README.md
include LICENSE.txt
include CONFIG.json
include requirements.txt

{ GET_DATA_FILES('docs') }
{ GET_DATA_FILES('static') }
{ GET_DATA_FILES('views') }
""".strip()

def set_modules_init():
    try:
        PROJECT_MODULES     = list(filter(lambda x: x not in ["__pycache__"], [ x for x in os.walk( f"{ PROJECT }/{ PROJECT.name }") ][0][1]))
        MODULES_IMPORT_TEXT = "\n".join([f"from . import { module }"for module in PROJECT_MODULES])
        MODULES_METHODS     = "\n".join( [ f'''"{ module }" : { module }.__dir__(),''' for module in PROJECT_MODULES] )
        _ob_                = "{"
        _cb_                = "}"
        MODULES_TEXT        = f"""
# MODULES
{ MODULES_IMPORT_TEXT }



# STRUCTURE
plugins = { _ob_ }
{ MODULES_METHODS }
{ _cb_ }
        """.strip()
        with open(f"{ PROJECT.name }/__init__.py", "w") as f:
            f.write( MODULES_TEXT )
            f.close()
    except Exception as e:
        pass

set_modules_init()

with open("CONFIG.json", "r") as f:
    CONFIG = json.load(f)

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open("MANIFEST.in", "w") as f:
    f.write( MANIFEST_TEXT )
    f.close()

def form(**kwargs) : pass #print(kwargs)

"""            __
  ______ _____/  |_ __ ________
 /  ___// __ \   __\  |  \____ \
 \___ \\  ___/|  | |  |  /  |_> >
/____  >\___  >__| |____/|   __/
     \/     \/           |__|
"""

#
setuptools.setup(
    packages                        = setuptools.find_packages(exclude=(".git",)),
    url                             = f"""https://github.com/{ CONFIG['organization'] }/{ PROJECT.name }""" if not CONFIG['url'] else CONFIG['url'],
    python_requires                 = CONFIG['python_requires'],
    name                            = PROJECT.name,
    version                         = CONFIG['version'],
    author                          = CONFIG['organization'],
    author_email                    = CONFIG['email'],
    description                     = CONFIG['description'],
    long_description                = LONG_DESCRIPTION,
    long_description_content_type   = "text/markdown",
    classifiers                     = CONFIG['classifiers'],
    project_urls                    = CONFIG['project_urls'],
    install_requires                = CONFIG['install_requires'],
    include_package_data            = True,
)
