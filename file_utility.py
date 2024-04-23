def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            return fh.readlines() #we return a list here
    except FileNotFoundError:
        print("Can't find the file, please check the path")
        return []
    except Exception as e:
        print(f'We have an error, pelase fix it! {e}')
        return []