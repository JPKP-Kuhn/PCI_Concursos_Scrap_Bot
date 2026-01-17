import os
from crewai_tools import FileReadTool

def file_read_tool() -> FileReadTool | str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        file_path = os.path.join(base_dir, "../../../knowledge/user_preference.txt")
        file_path = os.path.abspath(file_path)
    except FileNotFoundError:
        return "Arquivo não encontrado"


    return FileReadTool(file_path=file_path)

