from controllers.main_controller import MainController

# asyncio is used as a foundation for various Python asynchronous
# frameworks that provide high-performance networks and web servers,
# database connection libraries, distributed task queues, etc.
import asyncio


class MemberService:

    def __init__(self, controller: MainController):
        self.controller = controller

    def load_members(self):
        """Load Members from DB using  MainController without modification..."""
        return self.controller.load_members()

    def print_members(self):
        items = self.load_members()
        for item in items:
            print(item)

    async def print_members_async(self):
        await asyncio.create_task(self.__async_print_members__())

    def get_members(self):
        """Get members for table [ [x1,x2,x3...], [y1,y2,y3...],  [z1,z2,z3...]]"""
        items = self.load_members()
        return self.__list_to_matrix__(items)

    async def get_members_async(self):
        """Async: Get members for table [ [x1,x2,x3...], [y1,y2,y3...],  [z1,z2,z3...]]"""
        task = asyncio.create_task(
            self.__async_get_members__())  # create a task
        print(task.done())  # Will print False
        await task
        print(task.done())  # Will print True

    async def __async_get_members__(self):
        return self.get_members()

    async def __async_print_members__(self):
        """This is a corountine"""
        self.print_members()

    def __list_to_matrix__(self, list_of_items):
        return list(map(lambda elment: [elment], list_of_items))
