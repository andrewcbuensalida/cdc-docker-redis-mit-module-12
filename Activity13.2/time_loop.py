import threading
import time

titles = ["Harry Potter", "Pride and Prejudice"]
pages = ["250", "430"]
first_name = ["J.K", "Jane"]
last_name = ["Rowling", "Austen"]
location = ["UK", "UK"]

def build_book_dict(titles, pages, first_name, last_name, location):
    inputs = zip(titles, pages, first_name, last_name, location)
    d = {}
    for title, page, first, last, loc in inputs:
        d.update({
            title : {
                'Pages': int(page),
                'Author': {
                    'First': first,
                    'Last': last
                },
                'Publisher': {
                    'Location': loc
                }
            }
        })

    time.sleep(3)
    return d
  

timer = threading.Timer(5, build_book_dict, args=(titles, pages, first_name, last_name, location))
timer.start()
timer.cancel()
print('Timer Cancelled')