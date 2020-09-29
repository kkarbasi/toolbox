def find_recursive(base_dir, extention='mff', ftype='d', max_depth=None, verbose=False):
    """
    Finds files or directories with the specified extention
    """
    import os
    def walk(top, maxdepth):
        dirs, nondirs = [], []
        for name in os.listdir(top):
            (dirs if os.path.isdir(os.path.join(top, name)) else nondirs).append(name)
        yield top, dirs, nondirs
        if maxdepth > 1:
            for name in dirs:
                for x in walk(os.path.join(top, name), maxdepth-1):
                    yield x
    if max_depth == None:
        walker = os.walk
    else:
        walker = walk
        
    list_of_files = []
    if ftype == 'd':
        try:
            for root, dirnames, filenames in walker(base_dir, max_depth):
                for d_name in dirnames:
                    if d_name.endswith(extention): #and d_name.startswith('SHWK'):
                        list_of_files.append(os.path.join(root, d_name))
                        if verbose:
                            print('Found-->{}'.format(list_of_files[-1]))
        except Exception as e:
            print(str(e))
            pass
    if ftype == 'f':
        try:
            for root, dirnames, filenames in walker(base_dir, max_depth):
                for f_name in filenames:
                    if f_name.endswith(extention):
                        list_of_files.append(os.path.join(root, f_name))
                        if verbose:
                            print('Found-- {}'.format(list_of_files[-1]))
        except Exception as e:
            print(str(e))
            pass
        
    return list_of_files
