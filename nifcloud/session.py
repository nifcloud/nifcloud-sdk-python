from botocore import __version__ as botocore_version
from botocore import session
from botocore.session import get_session  # noqa: F401

import nifcloud


class Session(session.Session):

    def __init__(self, session_vars=None, event_hooks=None,
                 include_builtin_handlers=True, profile=None):
        super(Session, self).__init__(session_vars, event_hooks,
                                      include_builtin_handlers, profile)
        self.user_agent_name = 'nifcloud'
        self.user_agent_version = nifcloud.__version__
        self.user_agent_extra = 'botocore/%s' % botocore_version


session.Session = Session
