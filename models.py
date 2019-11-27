
from app import db, ma



class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Video %r>' % self.filename

class VideoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "filename")

video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)