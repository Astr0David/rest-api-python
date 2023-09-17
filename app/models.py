from app.config import db


class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    episode = db.Column(db.String(15))
    chapter = db.Column(db.String(15))
    year = db.Column(db.Integer)
    note = db.Column(db.Text)
    appearance = db.Column(db.Text)
    personality = db.Column(db.Text)
    abilities_and_powers = db.Column(db.Text)

    def __init__(
        self,
        name,
        episode,
        chapter,
        year,
        note,
        appearance,
        personality,
        abilities_and_powers,
    ):
        self.name = name
        self.episode = episode
        self.chapter = chapter
        self.year = year
        self.note = note
        self.appearance = appearance
        self.personality = personality
        self.abilities_and_powers = abilities_and_powers
