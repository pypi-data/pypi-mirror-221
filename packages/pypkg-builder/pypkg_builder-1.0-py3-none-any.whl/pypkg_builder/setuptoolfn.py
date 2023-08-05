def setup(L):
    from pyperclip import copy

    name=L[0]
    version=L[1]
    description=L[2]
    url=L[3]
    authorname=L[4]
    authoremail=L[5]
    license=int(L[6])
    classifier=L[7]
    installrequire=L[8]
    extrarequire=L[9]
    consol=L[10]
    pythonrequires=L[11]
    readme=L[12]
    


    if license==1:
        license="GNU GPL V3"
    if license==2:
        license="MIT License"
    if license==3:
        license="Apache License 2.0"
    if license==4:
        license="Mozilla Public License (MPL)"
    if license==5:
        license="A license with no conditions"
    else:
        license="User-defined or other"



    packagedir="src"
    s='''from setuptools import setup
    
with open("'''
    s=s+"README.md"+'''", "r") as f:
    long_description = f.read()
    
setup(
    name="'''+name+'''",
    version="'''+version+'''",
    description="'''+description+'''",
    package_dir={"": "'''+packagedir+'''"},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",'''
    if url!="":
        s=s+'''
    url="'''+url+'''",'''
        
    s=s+'''
    author="'''+authorname+'''",'''
    if authoremail!="":
        s=s+'''
    author_email="'''+authoremail+'''",'''
        
    s=s+'''
    license="'''+license+'''",'''
    if len(classifier)!=0:
        s=s+'''
    classifiers='''
        c='['
        for i in classifier:
            c=c+'"'+i+'",'
        c=c[:-1]+']'
        s=s+c
    if len(installrequire)!=0:
        s=s+''',
    install_requires='''
        
        ir='['
        for i in installrequire:
            ir=ir+'"'+i+'",'
        ir=ir[:-1]+']'
        s=s+ir
    if len(extrarequire)!=0:
        s=s+''',
    extras_require={
                "dev": '''
        exr='['
        for i in extrarequire:
            exr=exr+'"'+i+'",'
        exr=exr[:-1]+']'
        s=s+exr+'''
                },'''
    if len(consol)!=0:
        s=s+"""
    entry_points={
        'console_scripts': ["""
        for i in consol:
            s=s+"'"+i+"',"
        s=s+"""],},"""
    if pythonrequires!="":
        s=s+'''
    python_requires="'''+pythonrequires+'''",'''
    s=s+'''    
)'''
    copy(s)
    return s
