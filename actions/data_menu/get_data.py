import glob

def get_saves():
    db_files = glob.glob("api/*.json")
    return db_files