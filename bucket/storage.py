from django.core.files.storage import FileSystemStorage


class CustomFileSystemStorage(FileSystemStorage):
    def get_valid_name(self, name):
        return name.strip()

    # def get_available_name(self, name, max_length=None):
    #     return name