# from mongoengine import Document, EmbeddedDocument, fields

from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, ListField, DictField, IntField, FloatField, StringField


class Databases(Document):
    meta = {'collection': 'databases'}
    name = StringField(required=True)
    description = StringField(max_length=300)
    tags = ListField(StringField(max_length=30))


class Arrays(EmbeddedDocument):
    meta = {'strict': False}
    numbers = ListField(IntField())
    positions = ListField(ListField(FloatField()))


class Info(EmbeddedDocument):
    meta = {'strict': False}


class Derived(EmbeddedDocument):
    elements = DictField(IntField())
    arrays_keys = ListField(StringField())
    info_keys = ListField(StringField())


class Atoms(Document):
    meta = {'strict': False}

    # id = ObjectIdField()
    arrays = EmbeddedDocumentField(Arrays)
    info = EmbeddedDocumentField(Info)
    derived = EmbeddedDocumentField(Derived)


# class Atoms(Document):
#     meta = {'strict': False}
#
#     # id = ObjectIdField()
#     arrays = DictField()
#     info = DictField()
#     derived = EmbeddedDocumentField(Derived)
#
#     @classmethod
#     def from_ase(cls, atoms):
#         return cls()


if __name__ == '__main__':
    sample = {
        "pbc": "alias",
        "Lattice": "alias",
        "cell": "alias",
        "positions": "alias",
        "arrays": {
            "numbers":
                [26, 26, 26, "..."],
            "positions":
                [[-0.10204757, -0.24557776, 0.03216429],
                 [1.23818045, 1.64111918, 1.38883472],
                 [-0.01367307, -0.04099747, 3.0774359],
                 "..."],
            "forces":
                [[0.92008082, 1.39988003, -0.1555232],
                 [1.38380678, -1.65299434, 0.55857061],
                 [-0.39713156, -0.11856745, -1.23895032],
                 "..."]},
        "info": {
            "cell":
                [[8.6368128, 0, 0],
                 [0, 8.6368128, 0],
                 [0, 0, 8.6368128]],
            "pbc": [True, True, True],
            "constraints": [],
            "config_name": "bcc_bulk_54_expanded_2_0013",
            "config_type": "bcc_bulk_54_high",
            "degauss": 0.136056917253,
            "ecutwfc": 1224.51225528,
            "energy": -186883.383046,
            "calculator_name": "unknown",
            "calculator_parameters": {},
            "kpoints": [4, 4, 4]
        }
    }

    from mongoengine import connect

    collection_name = 'atoms'

    db  = connect('mongodb://localhost:27017/abcd')
    print(db)