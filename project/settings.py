from irekua_dev_settings.settings import *
from irekua_database.settings import *
from irekua_autocomplete.settings import *


INSTALLED_APPS = (
    IREKUA_AUTOCOMPLETE_APPS +
    IREKUA_DATABASE_APPS +
    IREKUA_BASE_APPS
)
