def save_new(arberatum, menu):
    arberatum.update_json(arberatum.saved_file)
    menu("~+ Saved Data +~")