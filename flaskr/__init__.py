import os
from flask import Flask, render_template, send_file, url_for, send_from_directory

def get_book_data():
	try:
		f = open('books.json')
		data = f.read()
		f.close()
	except BaseException:
		return []
	import json
	print(data)
	return json.loads(data)

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
	)
	if test_config is None:
		app.config.from_pyfile('config.py',silent=True)
	else:
		app.config.from_mapping(test_config)
	
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	@app.route('/')
	@app.route('/<path:subpath>')
	def index(subpath=''):
		if not os.path.isfile('static/local-gitbook/'+subpath):
			subpath = 'index.html'
		return send_from_directory('static/local-gitbook',subpath)
	@app.route('/server_status')
	def server_status():
		return 'Server running'
	@app.route('/status')
	def status():
		return render_template('status.html', books=len(get_book_data()))
	@app.route('/books')
	def books():
		print('here')
		import json
		return json.dumps(get_book_data())
	@app.route('/book/<bookname>/', defaults={'subpath':'index.html'})
	@app.route('/book/<bookname>/<path:subpath>')
	def show_book(bookname, subpath):
		# check if there's such book on server
		
		# resolve static page
		book = [item for item in get_book_data() if item['name']==bookname][0]
		if not book:
			return
		book_storage_name = book['hash']
		if not os.path.isfile('static/{}/{}'.format(book_storage_name,subpath)):
			subpath+='index.html'
			if not os.path.exists('static/{}/{}'.format(book_storage_name,subpath)):
				return ''
		return send_file('static/{}/{}'.format(book_storage_name,subpath))
	task_counter = 0
	@app.route('/addBook', methods=['POST','GET'])
	def add_book():
		from flask import request, make_response, redirect
		from . import gitbook_docker as gitbook
		response = make_response()
		print('requested')
		if request.method == 'POST':
			json_data = request.get_json()
			print(json_data)
			#print(request.content_type, request.is_json, request.data)
			bookname = json_data['name']
			repo_url = json_data['url']
			nonlocal task_counter
			task_counter += 1
			response.data = gitbook.make_local_book(bookname,repo_url,book_storage_dir=os.path.abspath('static'))
			task_counter -= 1	
			return response
		elif request.method == 'GET':
			if task_counter>0:
				return gitbook.status()
			return ''
		else:
			abort(500)

	return app

