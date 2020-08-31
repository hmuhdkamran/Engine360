import os, json

python_path = '/usr/bin/python3.6'


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

    def decode_backed_host_and_port(self):
        config_file = open(self.config_file, 'r')
        config_file = json.loads(config_file.read())
        backend_engine_values = config_file['BackendEngine']

        self.backend_host = backend_engine_values['host']
        self.backend_port = backend_engine_values['port']

        if not self.backend_host:
            self.backend_host = "127.0.0.1"
        if not self.backend_port:
            self.backend_host = "8000"

    def create_venv_if_not_exists(self):
        if not os.path.isdir(self.venv_path):
            os.system("pip install virtualenv")
            venv_path_cmd = "virtualenv --python=" + self.python_path + " " + self.venv_path
            os.system(venv_path_cmd)

    def install_backend_requirements(self):
        venv_file_pip = os.path.join(self.venv_path, 'bin', 'pip')
        os.system(venv_file_pip + ' install -r ' + self.requirement_path)

    def run_server_command(self):
        venv_file_python = os.path.join(self.venv_path, 'bin', 'python')
        while True:
            os.system(
                venv_file_python + " " + self.manage_py_path + " runserver " + self.backend_host + ":" + self.backend_port)


if __name__ == '__main__':
    BackendRunScript().run_server_command()