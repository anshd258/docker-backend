
from pathlib import Path
import os

print(os.environ.get('DJANGO_ENV'))
if os.environ.get('DJANGO_ENV') == 'development':
    from .development_settings import *
else:
    from .deployment_settings import *