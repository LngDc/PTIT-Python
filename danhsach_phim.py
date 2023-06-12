from datetime import datetime

class FilmInfo:
    ID = 1
    
    def __init__(self, category_id, date, name, episodes) -> None:
        self.category_id = category_id
        self.date = date
        self.name = name
        self.episodes = int(episodes)
        
        self.id = f'P{FilmInfo.ID:03d}'
        FilmInfo.ID += 1
        
        self.datetime = datetime.strptime(self.date, '%d/%m/%Y')
        
    def get_category(self, categories):
        self.category = categories[int(self.category_id[2:])]
    
    def __str__(self) -> str:
        return f'{self.id} {self.category} {self.date} {self.name} {self.episodes}'
        
        

def main():
    category_count, film_count = map(int, input().split())
    
    categories = ['']
    for i in range(category_count):
        categories.append(input())

    films = []
    for j in range(film_count):
        category_id, date, name, episodes = input(), input(), input(), input()
        film = FilmInfo(category_id, date, name, episodes)
        film.get_category(categories)
        films.append(film)
        
    films.sort(key = lambda x : (x.datetime, x.name, -x.episodes))
    
    for film in films:
        print(film)
         
if __name__ == '__main__':
    main()