def _find_recursive(base_dir, extention = 'mff', ftype = 'd'):
    """
    Finds files or directories with the specified extention
    """
    import os
    list_of_files = []
    if ftype == 'd':
        try:
            for root, dirnames, filenames in os.walk(base_dir):
                for d_name in dirnames:
                    if d_name.endswith(extention):
                        list_of_files.append(os.path.join(root, d_name))
                        print('Found-->{}'.format(list_of_files[-1]))
        except Exception as e:
            print(str(e))
            pass
    if ftype == 'f':
        try:
            for root, dirnames, filenames in os.walk(base_dir):
                for f_name in filenames:
                    if f_name.endswith(extention):
                        list_of_files.append(os.path.join(root, f_name))
                        print('Found-- {}'.format(list_of_files[-1]))
        except Exception as e:
            print(str(e))
            pass
        
    return list_of_files
