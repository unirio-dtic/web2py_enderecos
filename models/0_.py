from gluon.custom_import import track_changes
track_changes(True)
from gluon.contrib.appconfig import AppConfig
myconf = AppConfig(reload=True)