import os

from botocore import loaders

loaders.Loader.BUILTIN_DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'data'
)
