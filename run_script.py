import os, json, sys
from sys import platform
import threading

python_path = ''


class BackendRunScript:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(os.getcwd()), 'Engine360')
        self.config_file = os.path.join(self.config_path, 'Backend', 'Engine', 'project_settings.json')
        self.backend_path = os.path.join(self.config_path, 'Backend')
        self.frontend_path = os.path.join(self.config_path, 'Frontend')
        self.venv_path = os.path.join(self.backend_path, 'engine360')
        self.requirement_path = os.path.join(self.backend_path, 'requirements.txt')
        self.manage_py_path = os.path.join(self.backend_path, 'manage.py')
        self.python_path = python_path
        self.decode_backed_host_and_port()
        self.create_venv_if_not_exists()
        self.install_backend_requirements()
        self.install_npm()

    def decode_backed_host_and_port(self):
        config_file = open(self.config_file, 'r')
        config_file = json.loads(config_file.read())
        backend_engine_values = config_file['backendEngine']
        frontend_engine_values = config_file['frontEngine']

        self.backend_host = backend_engine_values['host']
        self.backend_port = backend_engine_values['port']

        self.frontend_host = frontend_engine_values['host']
        self.frontend_port = frontend_engine_values['port']

        if not self.backend_host:
            self.backend_host = "127.0.0.1"
        if not self.backend_port:
            self.backend_host = "8000"

    def create_venv_if_not_exists(self):
        if not os.path.isdir(self.venv_path):
            os.system("python -m pip install virtualenv")
            print(self.python_path)
            if self.python_path:
                venv_path_cmd = "python -m virtualenv --python=" + self.python_path + " " + self.venv_path
            else:
                venv_path_cmd = "virtualenv " + self.venv_path
            os.system(venv_path_cmd)

    def install_backend_requirements(self):
        if platform == "linux" or platform == "linux2":
            venv_file_pip = os.path.join(self.venv_path, 'bin', 'pip3')
        else:
            venv_file_pip = os.path.join(self.venv_path, 'Scripts', 'pip')
        os.system(venv_file_pip + 'python -m install -r ' + self.requirement_path)

    def install_npm(self):
        os.chdir(self.frontend_path)
        os.system("npm install")

    def run_front_end(self):
        os.chdir(self.frontend_path)
        os.system("npm run serve -- --port " + self.frontend_port)

    def run_back_end(self):
        if platform == "linux" or platform == "linux2":
            venv_file_python = os.path.join(self.venv_path, 'bin', 'python3')
        else:
            venv_file_python = os.path.join(self.venv_path, 'Scripts', 'python')
        os.system(
            venv_file_python + " " + self.manage_py_path + " runserver " + self.backend_host + ":" + self.backend_port)

    def run_back_end2(self):
        if platform == "linux" or platform == "linux2":
            venv_file_python = os.path.join(self.venv_path, 'bin', 'python')
        else:
            venv_file_python = os.path.join(self.venv_path, 'Scripts', 'python')
        os.system(
            venv_file_python + " " + self.manage_py_path + " runserver " + self.backend_host + ":8003")

    def run_server_command(self):
        front_end_thread = threading.Thread(target=self.run_front_end)
        back_end_thread = threading.Thread(target=self.run_back_end)

        front_end_thread.start()
        back_end_thread.start()

        while True:
            pass


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args):
        python_path = args[0]
    BackendRunScript().run_server_command()
