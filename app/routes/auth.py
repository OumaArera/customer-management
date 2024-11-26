from flask import Blueprint, redirect, url_for, session, jsonify
from app import oauth
from urllib.parse import urlencode, quote_plus
import os

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    """Redirect to Auth0 for login."""
    redirect_uri = url_for('auth.callback', _external=True)
    return oauth.auth0.authorize_redirect(redirect_uri)

@auth_bp.route('/callback', methods=["GET", "POST"])
def callback():
    """Handle the callback from Auth0 and fetch user information."""
    try:
        token = oauth.auth0.authorize_access_token()
        session['user'] = token.get('userinfo')  # Save user info in session
        return jsonify({
            'message': 'Login successful',
            'user': session['user']
        })
    except Exception as e:
        return jsonify({'error': f'Failed to process callback: {str(e)}'}), 500

@auth_bp.route('/logout')
def logout():
    """Clear session and redirect to Auth0 logout."""
    session.clear()
    logout_url = (
        f"https://{os.getenv('AUTH0_DOMAIN')}/v2/logout?"
        + urlencode({
            "returnTo": url_for("auth.login", _external=True),
            "client_id": os.getenv("AUTH0_CLIENT_ID"),
        }, quote_via=quote_plus)
    )
    return redirect(logout_url)

@auth_bp.route('/session')
def session_info():
    """Return the current session info."""
    if 'user' in session:
        return jsonify({'session': session['user']})
    return jsonify({'error': 'Not logged in'}), 401
