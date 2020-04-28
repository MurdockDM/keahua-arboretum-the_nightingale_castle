import glob

def get_saves():
    db_files = glob.glob("database/*.json")
    return db_files