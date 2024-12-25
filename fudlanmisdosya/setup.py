from cx_Freeze import setup, Executable

# Define the executable and options
executables = [
    Executable(
        "shitting.py",  # Your script
        target_name="shitting.exe",  # Output executable name
        base="Win32GUI",  # Win32GUI application
        icon=None,  # Path to your .ico file
        uac_admin=True  # Request admin privileges
    )
]

# Fine-tune build options
build_options = {
    "packages": [],
    "includes": [],
    "excludes": [],
    "include_msvcr": True,
    "include_files": [
    ],
}

# Setup configuration for cx_Freeze
setup(
    name="shitting",  # Application name
    version="0.1",  # Version number
    description="shitting",
    options={"build_exe": build_options},  # Build options
    executables=executables,  # List of executables
)