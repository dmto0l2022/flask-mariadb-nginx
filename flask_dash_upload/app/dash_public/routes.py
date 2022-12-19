from flask import Blueprint
dash_public_page_bp = Blueprint('dash_public_page_bp', __name__)

@hello_page_bp.route('/dmtpublic')
def publiclanding():
     return "This will be a publich dash app"
  
