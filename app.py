import subprocess

def install_package(package_name):
    print(f"Installing {package_name}...")
    subprocess.run(['yum', 'install', '-y', package_name])

def change_folder_permissions(folder_path):
    print(f"Changing permissions of {folder_path} folder...")
    subprocess.run(['chmod', '-R', '777', folder_path])

if __name__ == "__main__":
    packages_to_install = ['httpd', 'java', 'mysql']
    folder_to_change_permissions = '/test1'

    for package in packages_to_install:
        install_package(package)

    change_folder_permissions(folder_to_change_permissions)
