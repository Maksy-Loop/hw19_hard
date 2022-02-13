from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, rid, data):
        self.dao.update(data, rid)
        return self.dao.update(data, rid)

    def delete(self, rid):
        self.dao.delete(rid)
