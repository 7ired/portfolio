import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_login import current_user
from flask_mail import Message
from blog import mail

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
	form_picture.save(picture_path)
	
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)

	prev_picture = os.path.join(current_app.root_path, 'static/profile_pics', current_user.image_file)
	if os.path.exists(prev_picture) and prev_picture != 'default.jpg':
		os.remove(prev_picture)
	
	return picture_fn