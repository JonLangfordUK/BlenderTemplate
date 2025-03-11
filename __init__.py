
def check_package_version(package_name, version=None):
    """
    Check if a package is installed with the correct version in the addon's packages directory
    
    Args:
        package_name (str): Name of the package to check
        version (str, optional): Version requirement (e.g. '>=1.0.0', '==2.0.0'). Defaults to None.
    
    Returns:
        bool: True if package exists and version matches requirement (if specified), False otherwise
    """
    import pkg_resources
    import os
    import sys

    # Get the path to the addon's packages directory
    addon_dir = os.path.dirname(os.path.abspath(__file__))
    package_path = os.path.join(addon_dir, 'packages')

    # Create a WorkingSet that only looks in our packages directory
    ws = pkg_resources.WorkingSet([package_path])

    try:
        # Find the package in our custom packages directory
        dist = ws.find(pkg_resources.Requirement.parse(package_name))
        if not dist:
            return False

        # If version requirement specified, check if installed version matches
        if version:
            requirement = pkg_resources.Requirement.parse(
                f"{package_name}{version}"
            )
            return requirement.specifier.contains(dist.version)

        return True

    except pkg_resources.VersionConflict:
        return False


def setup_package_import(package_name):
    """
    Set up package import by adding it to sys.modules and executing the module
    
    Args:
        package_name (str): Name of the package to import
        
    Returns:
        module: The imported module object
        
    Raises:
        ImportError: If package installation or import fails
    """
    import os
    import sys
    import importlib.util
    
    # Get the path to the addon's packages directory
    addon_dir = os.path.dirname(os.path.abspath(__file__))
    package_path = os.path.join(addon_dir, 'packages')
    
    # Check if package is already imported
    if package_name in sys.modules:
        print(f'"{package_name}" is already imported')
        return sys.modules[package_name]
    
    # Verify package is installed
    if not check_package_version(package_name):
        raise ImportError(f'"{package_name}" is not installed in the packages directory')
    
    # Construct path to package's __init__.py file
    module_path = os.path.join(package_path, package_name.replace('-', '_'), '__init__.py')
    
    try:
        # Verify module file exists
        if not os.path.exists(module_path):
            raise ImportError(f'Package file not found: "{module_path}"')
        
        # Create module specification from file path    
        spec = importlib.util.spec_from_file_location(package_name, module_path)
        if spec is None:
            raise ImportError(f'Could not create module spec for "{package_name}"')
        
        # Create module from spec and add to sys.modules
        module = importlib.util.module_from_spec(spec)
        sys.modules[package_name] = module
        spec.loader.exec_module(module)

        print(f'"{package_name}" is ready to be imported')

        return module
        
    except Exception as e:
        raise ImportError(f"Failed to setup {package_name}: {str(e)}")


def install_required_packages(required_packages):
    """
    Install required packages into the addon's packages directory
    
    Args:
        required_packages (dict): Dictionary of packages to install with optional version requirements
                                Format: {'package_name': {'version': '>=1.0.0'}}
    """
    import subprocess
    import sys
    import os

    # Get the Python executable path
    python_executable = sys.executable

    # Iterate through each package in the requirements
    for package_name, config in required_packages.items():
        try:
            print()
            print("-" * 50)

            # Display installation message with version if specified
            if config.get('version'):
                print(f'Installing "{package_name}" ({config["version"]}) ...')
            else:
                print(f'Installing "{package_name}"...')
            
            print("-" * 50)

            # Check if package is already installed with correct version
            if check_package_version(package_name, config.get('version')):
                print(f'"{package_name}" already installed with compatible version')

            else:
                # Construct pip install command
                install_cmd = [
                    python_executable,
                    '-m',
                    'pip',
                    'install',
                    "--target",
                    os.path.join(os.path.dirname(__file__), 'packages'),
                    package_name
                ]

                # Add version specification if provided
                if config.get('version'):
                    install_cmd.extend([f"{package_name}{config['version']}"])

                # Execute pip install command and stream output
                process = subprocess.Popen(
                    install_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True,
                    bufsize=1
                )

                # Print installation progress in real-time
                for line in process.stdout:
                    print(line.strip())

                process.wait()

                # Check if installation was successful
                if process.returncode == 0:
                    print(f'{package_name} installed successfully')
                else:
                    raise subprocess.CalledProcessError(process.returncode, install_cmd)

            # Set up package for importing
            setup_package_import(package_name)

            print("-" * 50)

        except subprocess.CalledProcessError as e:
            print(f'\n✗ Error installing {package_name} package: {e}')
            raise

    print()
    print('Packages Upto Date')
    print()


def register():
    install_required_packages({        
        'requests': {'version': '>=2.25.0,<3.0.0'},     # Range specification
        'numpy': {},                                    # Latest version
        'scipy': {'version': '==1.15.2'}    
    })

    import requests

    print(requests.__version__)


def unregister(): ...