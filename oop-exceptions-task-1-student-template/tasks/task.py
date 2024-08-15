class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.__pages = [self.data[i:i + 5] for i in range(0, len(self.data), 5)]

    @property
    def page_count(self):
        return int(-(-(len(self.data) / self.items_on_page) // 1))

    @property
    def item_count(self):
        return len(self.data)

    def count_items_on_page(self, page_number):
        try:
            return len(self.__pages[page_number])

        except IndexError:
            raise Exception('Invalid index. Page is missing.')

    def find_page(self, data):
        result = [self.__pages.index(i) for i in self.__pages if data in i or str(i).replace(' ', '') in data]
        if not result:
            raise Exception(f"'{data}' is missing on the pages")
        else:
            return result

    def display_page(self, page_number):
        return self.__pages[page_number]


if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    print(pages.page_count)
