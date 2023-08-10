#!/usr/bin/env python3
""" Module of Session Auth Exp
"""
from api.v1.auth.session_auth import SessionAuth
from typing import Dict
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Session Expiration """

    def __init__(self):
        SESSION_DURATION = getenv('SESSION_DURATION', 0)

        try:
            SESSION_DURATION = int(SESSION_DURATION)
        except Exception:
            SESSION_DURATION = 0

        self.session_duration = SESSION_DURATION

    def create_session(self, user_id=None):
        """
            Make a new Session and register in the class with time

            Args:
                user_id: Identificator of the user_id

            Return:
                Session ID
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        session_dictionary: Dict = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
            Make a user ID based with time expiration

            Args:
                session_id: String of the session

            Return:
                User ID if not is expired
        """
        if session_id is None or\
           session_id not in self.user_id_by_session_id.keys():
            return None

        session_dictionary = self.user_id_by_session_id.get(session_id)

        if self.session_duration <= 0 or session_dictionary is None:
            return session_dictionary.get('user_id', None)

        created_by = session_dictionary.get('created_at', None)
        if created_by is None:
            return None

        expired_session = created_by + timedelta(seconds=self.session_duration)

        if expired_session < datetime.now():
            return None

        return session_dictionary.get('user_id', None)
