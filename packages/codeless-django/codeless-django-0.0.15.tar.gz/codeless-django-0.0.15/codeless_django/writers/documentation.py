from django.conf import settings
from codeless_django.utils import get_os_file_path
import os

class DocumentationWriter:
    def __init__(self):
        self.file_name=settings_file=settings.ROOT_URLCONF.split(".")[0] + "/urls.py"

    def write_documentation_url(self):
        os_file_path = get_os_file_path('additional_files/root_urls.py')
        os.system(f"cp {os_file_path} {self.file_name}")