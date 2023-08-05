def tree(setup="",readme="",license="",*kwargs):
    def generate_directory_tree(dir_path, indent='', is_last=True, is_subdir=False):
        tree_str = ''
        items = os.listdir(dir_path)
        
        
        if is_subdir and not is_last:
            tree_str += f"{indent}│\n"
        
        for i, item in enumerate(items):
            is_last_item = i == len(items) - 1
        
            full_path = os.path.join(dir_path, item)
            prefix = '└── ' if is_last_item else '├── '
        
            if is_subdir and not is_last:
                connector = '│   ' if is_last_item else '│   '
                tree_str += f"{indent}{prefix}{item}\n"
            else:
                tree_str += f"{indent}{prefix}{item}\n"
        
            if os.path.isdir(full_path):
                sub_tree = generate_directory_tree(full_path, indent + ('    ' if is_last_item else '│   '), is_last_item, True)
                tree_str += sub_tree
        
        return tree_str

    package_name=kwargs[0]
    sub_packages=kwargs[1]
    path=kwargs[2]
    import os
    import shutil
    try:
        os.chdir(path)
    except:
        pass
    
    ini_dir=os.getcwd()
    if os.path.exists(package_name):
        shutil.rmtree(package_name)
    os.mkdir(package_name)
    os.chdir(package_name)
    with open("README.md","w") as rd:
        rd.write(readme)
        rd.close()
    with open("License.txt","w") as ls:
        ls.write(license)
        ls.close()
    with open("setup.py","w") as st:
        st.write(setup)
        st.close()
    with open("MANIFEST.in","w") as m:
        m.write("recursive-include src/"+package_name+" *")
        m.close()
    os.mkdir("src")
    os.chdir("src")
    os.mkdir(package_name)
    os.chdir(package_name)
    open("__init__.py","w")
    for i in sub_packages:
        os.mkdir(i)
        open(i+"/__init__.py","w")
        open(i+"/"+i+".py","w")
   
    os.chdir(ini_dir)
    p=generate_directory_tree(ini_dir+"/"+package_name)
    s=package_name+"\n"
    for x in p.split("\n"):
        s=s+(len(package_name)-1)*" "+x+"\n"
    return s
    
    
    
