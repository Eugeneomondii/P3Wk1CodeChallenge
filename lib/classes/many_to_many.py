class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            raise Exception("Title cannot be changed after initialization")
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        self._magazine = value



class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise Exception("Name cannot be changed after initialization")
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = value

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list({a.magazine.category for a in self.articles()})



class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        if len(self.articles()) == 0:
            return None

        result = []
        for author in self.contributors():
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                result.append(author)

        return result if len(result) > 0 else None

    @classmethod
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))
