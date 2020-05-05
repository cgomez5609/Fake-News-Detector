from pathlib import Path


class FilePath:
    
    def __init__(self, filename: str, subdir: str):
        self.filename: str = filename
        self.subdir: str = subdir
        
    def __get_project_root(self):
        return Path(__file__).parent.parent.parent
    
    def get_path(self) -> Path:
        path = self.__get_project_root() / "data" / self.subdir / self.filename
        if path.exists() == False:
            raise FileNotFoundError("Not a valid filepath. Check the filename or subdirectory")
        else:
            return path
                