from dao.director import DirectorDAO
from flask import request


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self):
        data = request.json
        return self.dao.create(data)

    def update(self, rid):
        data = request.json

        return self.dao.update(data, rid)

    def delete(self, rid):
        return self.dao.delete(rid)