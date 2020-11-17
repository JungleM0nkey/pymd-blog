from flask import render_template, flash, redirect, url_for, request, jsonify, abort, send_from_directory
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app import db, POST_DIR
from app.forms import LoginForm, RegisterForm
from app.models import User, Posts
from werkzeug.urls import url_parse
import datetime
import os
from sqlalchemy import or_, and_
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.meta
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name
import frontmatter
from datetime import datetime


@app.route('/', methods=['GET','POST'])
def index():
    post_files = [ x[:-3] for x in os.listdir(POST_DIR) ]
    unsorted_files = {}
    #get the date for the files from the file metadata
    for f in post_files:
        post = frontmatter.load(f"{POST_DIR}\\{f}.md")
        date = str(post['published-on']).replace(',','')
        datetime_object = datetime.strptime(date, '%B %d %Y')
        unsorted_files[f'{f}'] = datetime_object
    #sort the files by date
    sorted_files = sorted(unsorted_files, key=unsorted_files.get)
    sorted_files.reverse()
    return render_template('index.html', posts=sorted_files)

@app.route('/posts/<post>', methods=['GET'])
def post(post):
    #parse the md file
    filepath = f"{POST_DIR}\\{post}"
    readme_file = open(filepath, "r")
    #md_post_string = markdown.markdown(readme_file.read(), extensions=["fenced_code", "codehilite", "meta"])
    md = markdown.Markdown(extensions=["fenced_code", "codehilite", "meta"])
    html = md.convert(readme_file.read())
    #apply formatting
    formatter = HtmlFormatter(style="emacs",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    #prepend meta information to the html output
    post_title = "<h2>" + str(md.Meta['title'][0]) + "</h2>"
    post_date = "<b>" + str(md.Meta['published-on'][0]) + "</b>"
    html = post_title + post_date + html
    #combine html and css
    markdown_post = md_css_string + html
    return markdown_post