from asgiref.sync import sync_to_async


class Paginate:
    def __init__(self, query, extract, start_index, limit):
        self.query = query
        self.extract = extract
        self.start_index = start_index
        self.limit = limit

    # async def get_object_from_db(self, item):
    #     return await self.extract(item)

    def paginate(self):
        try:
            total = self.query.count()
        except:
            total = len(self.query)

        upper_limit = min(total, self.start_index + self.limit)
        iteration = 0

        items = []
        key_finder = self.start_index + 1
        for item in self.query[self.start_index:upper_limit]:
            iteration = iteration + 1
            ext = self.extract(item)
            # ext = self.get_object_from_db(item)
            if ext is not None:
                items.append(ext)
                key_finder += 1

        return {
            'recordsTotal': total,
            'recordsFiltered': total,
            'data': items
        }
