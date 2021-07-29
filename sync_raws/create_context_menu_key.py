import os
import sys
import winreg as registry

# get current working directory
cwd = os.getcwd()

# get python path
python_exe = sys.executable

# key to be added in registry
key_path = r"Directory\\Background\\shell\\SyncRaw"

# add key to HKEY_CLASSES_ROOT
key = registry.CreateKeyEx(registry.HKEY_CLASSES_ROOT, key_path)

# set value of key
registry.SetValue(key, '', registry.REG_SZ, "&Sync Raw")

# add the command key
actual_key = registry.CreateKeyEx(key, r"command")

# add the command to be run
# %V is to read the folder name which can be passed as an argument
registry.SetValue(actual_key, '', registry.REG_SZ,
                  python_exe + f' "{cwd}\\sync_raw_jpeg.py" "%V"')
