# store standard roots of website
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])

def home():
    if request.method == "POST":
        url1 = request.form.get("url1")
        if url1.startswith("https://"):
            # flash("URL https:// ile başlamalıdır", category="error")

            return redirect(url_for("views.home"))
        else:
            flash("URL https:// ile başlamalıdır", category="error")

    return render_template("home.html")

    """
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='succcess')

    return render_template("home.html", user=current_user)
    """
