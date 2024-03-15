import glob

def read_all_files(dir: str, extension: str) -> list[str]:
    search_for = dir + extension 
    return glob.glob(search_for)
