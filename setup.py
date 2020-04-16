import cx_Freeze
import sys


base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Main.py", base=base, icon = "Main_icon.ico")]
build_exe_options = {"includes":[ 'lab\Lab_1\Calculetion', "lab\Lab_1\File",  "lab\Lab_1\Log", "lab\Lab_1\office",  "lab\Lab_1\Window1",
                                  'lab\Lab_2\Calculetion', "lab\Lab_2\File",  "lab\Lab_2\Log", "lab\Lab_2\office",  "lab\Lab_2\Window2",
                                  'lab\Lab_3\Calculetion', "lab\Lab_3\File",  "lab\Lab_3\Log", "lab\Lab_3\office",  "lab\Lab_3\Window3",
                                  'lab\Lab_4\Calculetion', "lab\Lab_4\File",  "lab\Lab_4\Log", "lab\Lab_4\office",  "lab\Lab_4\Window4",
                                  'lab\Lab_5\Calculetion', "lab\Lab_5\File",  "lab\Lab_5\Log", "lab\Lab_5\office",  "lab\Lab_5\Window5",
                                  'lab\Lab_6\Calculetion', "lab\Lab_6\File",  "lab\Lab_6\Log", "lab\Lab_6\office",  "lab\Lab_6\Window6",
                                  "Main_window", "Sourse"],
                    'packages': [ "matplotlib", "pyqt5", "threading", "logging", "docxtpl", "shutil", "seaborn", "statistics",
                                  "seaborn", "pandas"]
                     }

cx_Freeze.setup(
    name = "Мастер лабы",
    options = {"build_exe": build_exe_options},
    version = "2.0",
    description = "Расчёт лаболаторных по тепломассообмену",
    executables = executables
    )
