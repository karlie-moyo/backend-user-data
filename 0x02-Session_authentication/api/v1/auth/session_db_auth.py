#!/usr/bin/env python3
""" Module of Session in Database
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """Session in database Class"""

    def create_session(self, user_id=None):
        """
            Make a new Session to Database

            Args:
                user_id: Identificator of the user_id

            Return:
                Session ID
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        user_session = UserSession(
            user_id=user_id,
            session_id=session_id
        )

        if user_session is None:
            return None

        user_session.save()
        UserSession.save_to_file()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
            Make user id to session

            Args:
                session_id: String of the session

            Return:
                User ID if not is expired
        """
        if session_id is None:
            return None

        UserSession.load_from_file()
        user_sess = UserSession.search({'session_id': session_id})

        if not user_sess:
            return None

        user = user_sess[0]

        if user is None:
            return None

        expired_tm = user.created_at + \
            timedelta(seconds=self.session_duration)

        if expired_tm < datetime.now():
            return None

        return user.user_id

    def destroy_session(self, request=None):
        """ Destroy the auth session if this

        Return:
            Destuction
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)

        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        session_user = UserSession.search({'session_id': session_id})
        if not session_user or session_user is None:
            return False

        try:
            session_user[0].remove()
            UserSession.save_to_file()
        except Exception:
            return False

        return True
