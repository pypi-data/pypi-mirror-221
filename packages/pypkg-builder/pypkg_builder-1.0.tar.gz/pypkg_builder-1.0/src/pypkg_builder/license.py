def license(x,name_author,name_program,year,note):

    file=["GNU GPLv3","MIT License","Apache Version 2.0","Mozilla Public License 2.0","The Unlicense","user_defined"][x-1]
    import pkg_resources
    relativepath=pkg_resources.resource_filename("template_pypackage_builder", "types")
    path=relativepath+"/"+file+".txt"
    with open(path,"r") as template:
        content=template.read()

    content=content.replace("[name of copyright owner]","["+str(name_author)+"]")
    content=content.replace("[yyyy]","["+str(year)+"]")
    content=content.replace("[fullname]","["+str(name_author)+"]")
    content=content.replace("[year]","["+str(year)+"]")
    content=content.replace("<name of author>",""+str(name_author)+"")
    content=content.replace("<year>",""+str(year)+"")
    content=content.replace("<program>",""+str(name_program)+"")
    content=content.replace("<one line to give the program's name and a brief idea of what it does.>",""+str(note)+"")
            
    return content