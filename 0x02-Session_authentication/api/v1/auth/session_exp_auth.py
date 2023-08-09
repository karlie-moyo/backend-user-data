#!/usr/bin/env python3
"""
Expiring session module
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """ Expiring session class
    """
    def __init__(self) -> None:
        """ Initialize SessionExpAuth instance
        """
        super().__init__()
        duration = getenv('SESSION_DURATION')
        if not duration:
            self.session_duration = 0
        else:
            try:
                duration = int(duration)
                self.session_duration = duration
            except ValueError:
                self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """ Gets session_id from parent class method
            Updates user_id_by_session_id dictionary to hold
            key-pair value
            Return:
             - None if session_id can't be created
             - session id if created
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        user_id = SessionExpAuth.user_id_by_session_id.get(session_id)
        created_at = datetime.now()
        session_dict = {"user_id": user_id, "created_at": created_at}
        SessionExpAuth.user_id_by_session_id.update({session_id: session_dict})
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Gets user id associated with passed session id
            Return:
                - user's id
        """
        if not session_id and type(session_id) is not str:
            return None
        session_info = SessionExpAuth.user_id_by_session_id.get(session_id)
        if not session_info:
            return None
        user_id = session_info.get("user_id")
        created_at = session_info.get("created_at")

        # Get user id for session with no expiry duration
        if self.session_duration <= 0:
            return user_id

        # Get user id for associated with expiry session
        if not created_at:
            return None
        expiry_date = created_at + timedelta(seconds=self.session_duration)
        if datetime.now() > expiry_date:
            return None
        return user_id
