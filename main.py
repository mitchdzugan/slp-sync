import sys
import os
from PySide6.QtCore import QDir, QFile, QStandardPaths
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtSql import QSqlDatabase
import resources_rc
from lib.paths import EnvPaths

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
