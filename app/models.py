# Add any model classes for Flask-SQLAlchemy here
from . import db

class MovieInfo(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text())
    poster = db.Column(db.String(255))
    created_at = db.Column(db.DateTime())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
    
        
    def get_title(self):
        try:
            return unicode(self.title)  # python 2 support
        except NameError:
            return str(self.title)  # python 3 support
    
    
    def get_description(self):
        try:
            return unicode(self.description)  # python 2 support
        except NameError:
            return str(self.description)  # python 3 support
        
        
    def get_poster(self):
        try:
            return unicode(self.poster)  # python 2 support
        except NameError:
            return str(self.poster)  # python 3 support
        
        
    def get_created_at(self):
        try:
            return unicode(self.created_at)  # python 2 support
        except NameError:
            return str(self.created_at)  # python 3 support

    def __repr__(self):
        return '<Movie %r>' % (self.title)