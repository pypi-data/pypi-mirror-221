def readme(package_name,breif,note,install_description,install_cmd,install_require,usage_note,usage_cmds,author_name,license_type):

    usage_note=[usage_note]
    usage_cmds=[usage_cmds]
    license_type=int(license_type)
    if license_type==1:
        license_type="GNU GPL V3"
    elif license_type==2:
        license_type="MIT License"
    elif license_type==3:
        license_type="Apache License 2.0"
    elif license_type==4:
        license_type="Mozilla Public License (MPL)"
    elif license_type==5:
        license_type="A license with no conditions"
    else:
        license_type="User-defined or other"


    
    s="# "+package_name+"\n"+breif+"\n"
    s=s+"""## Table of Contents
    
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)
- [License](#license)
    
## Description
    """+note+"\n## Installation\n"+install_description+"\n\n```\n"+install_cmd+"\n```\n#### Install requires\n\n"
    for i in install_require:
        s=s+i+"\n\n"
    s=s+"## Usage\n"
    for idx,x in enumerate(usage_cmds):
        s=s+usage_note[idx]+"\n\n"
        s=s+"```\n"+x+"\n```\n"
    s=s+"## Author\n"+author_name+"\n"+"## License\n"+license_type

    return s