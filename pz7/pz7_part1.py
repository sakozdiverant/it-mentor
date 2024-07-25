import os
import subprocess

# Путь к корневой папке с тестами
root_dir = os.path.dirname(os.path.abspath(__file__))[:-3]
print('root_dir =',root_dir)
# Список папок с тестами
test_folders = [f"pz{i}" for i in range(1, 7)]
print('test_folders =',test_folders)
def run_tests():
    for folder in test_folders:
        test_file = f'{root_dir}{folder}\\{folder}_test.py'
        if os.path.exists(test_file):
            print(f"Running tests in {test_file}")
            subprocess.run(['pytest', test_file])
        else:
            print(f"Test file {test_file} not found")

if __name__ == "__main__":
    run_tests()
