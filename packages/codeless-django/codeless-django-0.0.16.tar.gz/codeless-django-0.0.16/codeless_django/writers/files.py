from codeless_django.writers.base import BaseWriter
import os
from codeless_django.utils import get_os_file_path

class PrepareFiles:

    def __init__(self,app_name,write_api_views=False):
        self.app_name=app_name
        self.write_api_views=write_api_views
        self.write_import_line_to_view_file()
        self.write_import_line_to_url_file()
        self.write_import_line_to_serializers_file()

    def write_import_line(self,file_name,import_line):

        with open(file_name,'w') as f:
            f.write(import_line + "\n \n")

    def write_import_line_to_view_file(self):
        file_name=f"{self.app_name}/views.py"
        import_line="from django.views import generic \n"
        import_line+=f"from {self.app_name} import models as {self.app_name}_models \n"
        if self.write_api_views:
            import_line+="from rest_framework import generics \n" + f"from {self.app_name} import serializers\n"
        self.write_import_line(file_name,import_line)

    def write_import_line_to_serializers_file(self):
        file_name=f"{self.app_name}/serializers.py"
        if self.write_api_views:
            import_line="from rest_framework import serializers  \n"
            import_line+=f"from {self.app_name} import models as {self.app_name}_models \n"
            self.write_import_line(file_name,import_line)

    def write_import_line_to_url_file(self):
        file_name=f"{self.app_name}/urls.py"
        import_line="from django.urls import path" + "\n" + f"from {self.app_name} import views \n"
        initial_url_pattern = "urlpatterns = [] \n"
        text = import_line + initial_url_pattern
        self.write_import_line(file_name,text)

class RequirementTextWriter:
    def __init__(self):
        self.file_name="requirements.txt"
        with open(self.file_name,'a') as f:
            f.write(f"django>=2.2.16 \nPillow==9.5.0 \n")

    
    def add_new_package(self,package_name,version):
        with open(self.file_name,'a') as f:
            f.write(f"{package_name}=={version}\n")


class DotEnvFileWriter:
    def __init__(self):
        self.file_name=".env"
    
    def add_new_key(self,key,value):
        with open(self.file_name,'a') as f:
            f.write(f"{key}={value}")


class AdditionalFileWriter:
    def __init__(self):
        self.requirement_text_writer = RequirementTextWriter()


    def write_gitignore_file(self):
        os_file_path = get_os_file_path('additional_files/.gitignore')
        os.system(f"cp {os_file_path} .gitignore")
    
    def write_new_package_in_requirements_text(self,package_name,version):
        self.requirement_text_writer.add_new_package(package_name, version)
