import os

def project_path():
    return os.path.abspath(__file__).rpartition('/')[0]