import os
import pickle as pkl

class FileWriter:

    path = property()

    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(path):
            self.path_ = path
            self.file = None

    def __enter__(self):
        self.file = open(self.path, 'a')
        return self

    def __exit__(self, exp_type, exp_value, traceback):
        if self.file is not None:
            self.file.close()

    def _check_path(self, path):
        try:
            if not os.path.exists(path[:path.rfind('/')+1]):
                raise Exception('dir does not exist')
        except Exception as e:
            print(e)
        else:
            return True

    @path.getter
    def path(self):
        return self.path_

    @path.setter
    def path(self, path):
        self.__init__(path)

    @path.deleter
    def path(self):
        self.path_ = ''

    def print_file(self):
        if self.file is None:
            print('file does not exist')
        else:
            self.file = open(self.path, 'r')
            lines = self.file.readlines()
            for line in lines:
                print(line)
            self.file.close()

    def write(self, some_string):
        self.file.write(some_string)

    def save_yourself(self, file_name):
        file = open(file_name, 'wb')
        pkl.dump(FileWriter(self.path), file)
        file.close()

    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as file:
            new_obj = pkl.load(file)
            return new_obj
