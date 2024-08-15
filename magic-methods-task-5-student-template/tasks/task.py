import os
import shutil
import uuid


class TempDir:
    def __init__(self):
        self.current_path = os.getcwd()

    def __enter__(self):
        unique_folder_name = str(uuid.uuid4())[:8]
        try:
            os.mkdir(unique_folder_name, mode=0o777)
        except:
            pass
        finally:
            self.new_path = os.path.abspath(os.getcwd()) + f'/{unique_folder_name}'
            os.chdir(self.new_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.current_path)
        shutil.rmtree(self.new_path)


if __name__ == '__main__':
    print(os.getcwd())
    with TempDir() as f:
        os.mkdir('inside')
        print(os.getcwd())
    print(os.getcwd())
