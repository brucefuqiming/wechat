import os
import time


class BaseSetting(object):
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.workspace_dir = self.mk_dir(os.path.join(self.root_dir, "workspace"))
        self.contact_dir = self.mk_dir(os.path.join(self.workspace_dir, "contact"))
        self.current_contact_path = os.path.join(self.contact_dir, f'contact_{int(time.time())}.csv')

    @staticmethod
    def mk_dir(path):
        if not os.path.exists(path):
            os.mkdir(path)
        return path


if __name__ == '__main__':
    print(BaseSetting().root_dir)
    print(BaseSetting().current_contact_path)
