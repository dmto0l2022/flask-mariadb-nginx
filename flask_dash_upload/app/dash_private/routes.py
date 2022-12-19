from flask import Blueprint
dash_private_page_bp = Blueprint('dash_private_page_bp', __name__)

@hello_page_bp.route('/dmtprivate')
def privatelanding():
     return "This will be a private dash app"
  
