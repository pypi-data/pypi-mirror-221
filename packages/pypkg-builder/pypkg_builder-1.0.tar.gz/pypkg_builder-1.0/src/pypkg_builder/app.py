from flask import Flask, render_template, request, redirect, url_for
def app_fn():
	import webbrowser
	import os
	from .readme import readme
	from .license import license
	from .setuptoolfn import setup
	from .tree import tree
	def collim(c):
		L=[]
		for x in c.split("\n"):
			if len(x)>49:
				t=x[4:]
				while len(t)>=45:
					L.append("    "+t[:45])
					t=t[45:]
				if len(t)!=0:
					L.append("    "+t)
			else:
				L.append(x)
		return "\n".join(L)
	def clean(x):
		x=x.replace("\r","")
		x=x.split("\n")
		L=[]
		for i in x:
			if i!="":
				L.append(i)
		return L
	app = Flask(__name__)
	@app.route('/', methods=['GET', 'POST'])
	def index():
		if request.method == 'POST':
			if request.form.get('shutdown-button') == 'stop':
				os.kill(os.getpid(), 9)
				return 'Server shutting down...' 
			if request.form.get('info') == 'on':
				return render_template("help.html")
			

			package_name = str(request.form.get('package_name'))
			version = str(request.form.get('version'))
			bdescription = str(request.form.get('bdescription'))
			ldescription = str(request.form.get('ldescription'))
			author= str(request.form.get('author'))
			email = str(request.form.get('email'))
			year = str(request.form.get('year'))
			license_type = int(request.form.get('license_type'))
			github = str(request.form.get('github'))

			classifiers = str(request.form.get('Classifiers'))
			installrequires = str(request.form.get('installrequires'))
			pythonrequires = str(request.form.get('pythonrequires'))
			entrypoint = str(request.form.get('entrypoint'))
			installdescription = str(request.form.get('installdescription'))
			installcommand = str(request.form.get('installcommand'))
			usagecommand = str(request.form.get('usagecommand'))
			path = str(request.form.get('path'))
			usagedescription = str(request.form.get('usagedescription'))
			submodules=str(request.form.get('submodules'))
			devrequires=str(request.form.get('devrequires'))

			if version=="":
				version="0.0.1"
			if bdescription=="":
				bdescription="Initial delpoyment"
			if ldescription=="":
				ldescription="Initial Long description"
			if author=="":
				author="Author"
			if email=="":
				email="author@example.org"
			if year=="":
				from datetime import date
				year = str(date.today())
			if license_type=="":
				license_type="GNU GPL V3"

			ldescription=ldescription.replace("\r","")
			classifiers=clean(classifiers)
			installrequires=clean(installrequires)
			entrypoint=clean(entrypoint)
			installdescription=installdescription.replace("\r","")
			usagedescription=usagedescription.replace("\r","")
			submodules=clean(submodules)
			devrequires=clean(devrequires)

			if len(classifiers)==0:
				classifiers.append("License :: OSI Approved :: GNU General Public License v3 (GPLv3)")
				classifiers.append("Programming Language :: Python :: 3.10")
			if pythonrequires=="":
				pythonrequires=">=3.9"

			rdme=readme(package_name,bdescription,ldescription,installdescription,installcommand,installrequires,usagedescription,usagecommand,author,license_type)
			lic=license(license_type,author,package_name,year[:4],bdescription)
			L=[package_name,version,bdescription,github,author,email,license_type,classifiers,installrequires,
			devrequires,entrypoint,pythonrequires,rdme]
			stp=setup(L)
			

			directory=tree(stp,rdme,lic,package_name,submodules,path)

			directory="<pre>"+directory+"</pre>"
			stp=collim(stp)
			stp="<pre>"+stp+"</pre>"
			
			print(10)

			return render_template('index.html', setup_data=stp,tree_data=directory,path=path)

		return render_template('index.html')
	return app
