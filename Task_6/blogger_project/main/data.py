# Цей клас імітує базу даних, як сказано в завданні
class BloggersData:
    bloggers = [
        {
            "id": 1,
            "name": "PewDiePie",
            "category": "Gaming",
            "subscribers": "111M",
            "description": "Один з найвідоміших ютуберів у світі."
        },
        {
            "id": 2,
            "name": "MrBeast",
            "category": "Entertainment",
            "subscribers": "150M",
            "description": "Робить найдорожчі челенджі та благодійність."
        },
        {
            "id": 3,
            "name": "MKBHD",
            "category": "Tech",
            "subscribers": "16M",
            "description": "Найякісніші огляди техніки."
        }
    ]

    @classmethod
    def get_all(cls):
        return cls.bloggers

    @classmethod
    def get_by_id(cls, blogger_id):
        for blogger in cls.bloggers:
            if blogger["id"] == blogger_id:
                return blogger
        return None