import os, sys

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

print(check_gitbook_docker_image())
