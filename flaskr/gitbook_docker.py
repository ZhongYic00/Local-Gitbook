import os, sys
running_stat = 'idle'
def git_get_repo(url, dest):
	from git import Repo
	import re
	print('git_get_repo', url)
	pattern = re.compile(r'[^/]*(?=\.git)')
	repo_name = pattern.search(url)
	if not repo_name:
		print('Not an git repo url')
		return ''
	repo_name = repo_name.group(0)
	path = os.path.join(dest,repo_name)
	path = os.path.abspath(path)
	
	print('Cloing {} to {}...'.format(repo_name, path))
	global running_stat
	running_stat = 'cloning repo'
	
	try:
		Repo.clone_from(url,path,multi_options=['--depth=1'])
	except BaseException as e:
		print('An error occured when cloning repository at', url, ':')
		print(e)
		return ''
	print('Cloning repository succeeded')
	running_stat = 'repo cloned'
	return path

def check_gitbook_docker_image():
	import docker
	client = docker.from_env()
	try:
		client.images.get('fellah/gitbook')
	except docker.errors.ImageNotFound:
		while True:
			print('Docker image not found, download now?(y/N)')
			b = input()
			if b == 'y':
				client.images.pull('fellah/gitbook')
				return 0
			elif b != 'n' and b != 'N':
				continue
			else:
				return -1
	except BaseException as e:
		print('An error occured when checking docker image')
		print(e)
		return -1
	else:
		print('Docker image checked, found gitbook image')
		return 0

def run_gitbook_build(host_source_path, host_dest_path):
	import docker
	client = docker.from_env()
	#return
	docker_source_path = '/srv/gitbook'
	docker_dest_path = '/srv/html'
	command = 'gitbook build {} {}'.format(docker_source_path, docker_dest_path)
	print(command)
	vols = {
		host_source_path : {
			'bind' : docker_source_path,
			'mode' : 'rw'
		},
		host_dest_path : {
			'bind' : docker_dest_path,
			'mode' : 'rw'
		}
	}
	print('Installing plugins')
	global running_stat
	running_stat = 'installing gitbook plugins'
	client.containers.run('fellah/gitbook', 'gitbook install', volumes=vols)
	print('Plugins installed')
	running_stat = 'building gitbook'
	container = client.containers.run('fellah/gitbook', command, volumes=vols, detach=True)
	container.wait()
	return container.logs()

def append_book_record(bookname, book_storage_name, git_repo_url):
	try:
		f = open('books.json')
		data = f.read()
		f.close
	except BaseException as e:
		print(e)
		return -1
	import json
	data = json.loads(data)
	data.append({'name':bookname, 'hash':book_storage_name, 'src':git_repo_url})
	f = open('books.json','w')
	f.write(json.dumps(data))
	f.close()

def make_local_book(bookname, git_repo_url, git_tmp_dir='/dev/shm/', book_storage_dir='/tmp/html/'):
	if check_gitbook_docker_image() != 0:
		print('check docker image failed, exit now')
		return 'docker image does not exist'
	git_repo_path=git_get_repo(git_repo_url, git_tmp_dir)
	if not git_repo_path:
		print('clone failed, exit now')
		return 'clone failed'
	print(git_repo_path)
	import base62
	book_storage_name = base62.encodebytes(bookname.encode())
	print('build book in', bookname)
	print(run_gitbook_build(git_repo_path, os.path.join(book_storage_dir, book_storage_name)))
	append_book_record(bookname, book_storage_name, git_repo_url)
	global running_stat
	running_status = 'idle'
	return ''
def status():
	return running_stat
if __name__ == '__main__':
	#make_local_book('testbook', sys.argv[1], book_storage_dir='/tmp')
	append_book_record('testbook')
