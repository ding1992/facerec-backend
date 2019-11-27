from flask import request, Blueprint
from models import Video, videos_schema
from app import db
import json

video_api = Blueprint('video', __name__)
@video_api.route('/video', methods=['GET','POST'])
def video():
    if request.method == 'POST':
        static_file = request.files['video']
        static_file.save(f'./uploads/{static_file.filename}')
        video = Video(filename=static_file.filename)
        db.session.add(video)
        db.session.commit()
        db.session.flush()
        return f"Upload successful, video id {video.id}"
    elif request.method == 'GET':
        video_list = []
        videos = Video.query.all()
        for video in Video.query.all():
            video_list.append({"id":video.id, "filename":video.filename})
        return json.dumps(videos_schema.dump(videos))