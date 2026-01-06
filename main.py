import sys
import os
from PySide6.QtCore import QDir, QFile, QStandardPaths
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtSql import QSqlDatabase
import resources_rc
import platform
from pathlib import Path
import tempfile

path_home = Path.home()
path_tmp = Path(tempfile.gettempdir())

class EnvPaths:
    def __init__(self, name):
        self.name = name
    @property
    def temp(self): return path_tmp / self.name

class DarwinEnvPaths(EnvPaths):
    def __init__(self, *args):
        super().__init__(*args)
        self.library = path_home / 'Library'
    @property
    def data(self): return self.library / "Application Support" / self.name
    @property
    def config(self): return self.library / "Preferences" / self.name
    @property
    def cache(self): return self.library / "Caches" / self.name
    @property
    def log(self): return self.library / "Logs" / self.name

class WindowsEnvPaths(EnvPaths):
    def __init__(self, *args):
        super().__init__(*args)
        self.app_data = os.getenv('APPDATA', (
            path_home / 'AppData' / 'Roaming'
        ))
        self.local_app_data = os.getenv('LOCALAPPDATA', (
            path_home / 'AppData' / 'Local'
        ))
    @property
    def data(self): return self.local_app_data / self.name / 'Data'
    @property
    def config(self): return self.app_data / self.name / 'Config'
    @property
    def cache(self): return self.local_app_data / self.name / 'Cache'
    @property
    def log(self): return self.local_app_data / self.name / 'Log'

def env_or(xdg_varname, *fallback_path):
    varname = f"XDG_{xdg_varname}"
    return Path(os.getenv(varname, path_home.joinpath(*fallback_path)))

class LinuxEnvPaths(EnvPaths):
    def __init__(self, *args):
        super().__init__(*args)
        self.username = path_home.name

    @property
    def data(self): return env_or('DATA_HOME', '.local', '.share') / self.name
    @property
    def config(self): return env_or('CONFIG_HOME', '.config') / self.name
    @property
    def cache(self): return env_or('CACHE_HOME', '.cache') / self.name
    @property
    def log(self): return env_or('STATE_HOME', '.local', '.state') / self.name
    @property
    def temp(self): return path_tmp / self.username / self.name

def EnvPaths(name):
    plat_sys = platform.system()
    match plat_sys:
        case "Windows": return WindowsEnvPaths(name)
        case "Linux": return LinuxEnvPaths(name)
        case "Darwin": return DarwinEnvPaths(name)
    raise ValueError(f"Unknown platform.system(): {plat_sys}")

env_paths = EnvPaths("slp-db")
print(env_paths.data)
print(env_paths.config)
print(env_paths.cache)
print(env_paths.log)
print(env_paths.temp)


if __name__ == "__main__":
    # os.environ["QT_QUICK_CONTROLS_DEFAULT_STYLE"] = "Material" # Optional: set a modern style
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('qrc:/qml/main.qml')
    os.makedirs(env_paths.data, exist_ok=True)
    filename = env_paths.data / "db.sqlite3"
    print(f"FILENAME: {filename}")
    print("pre_sql")
    database = QSqlDatabase.database()
    if not database.isValid():
        database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName(f"{filename}")
    print("pre_open")
    res = database.open()
    print("res")
    print(res)
    sys.exit(app.exec())
