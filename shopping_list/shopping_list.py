import asyncio
from ourgroceries import OurGroceries

import shopping_list

class ShoppingList:
    def __init__(self, list_name) -> None:
        username,password = open('config.txt').read().split(',');
        self.list_name = list_name

        self.loop = asyncio.get_event_loop()
        self.og = OurGroceries(username, password)
        
        self.login()        
        
        self.list_id = self.get_list_id(list_name)

    def login(self):
        self.loop.run_until_complete(self.og.login())

    def get_list_id(self, list_name):
        '''
            Returns de id of the list named list_name
        '''
        my_lists = self.loop.run_until_complete(self.og.get_my_lists())
        for l in my_lists['shoppingLists']:
            if l['name'] == list_name:
                return l['id']
        return ''

    def get_items(self):
        '''
            Returns a tuple with both not crossed off items and crossed off items
        '''
        shopping_list = self.loop.run_until_complete(self.og.get_list_items(list_id=self.list_id))
        items_not_crossed = [item for item in shopping_list['list']['items'] if item['crossedOff'] is False]
        items_crossed = [item for item in shopping_list['list']['items'] if item['crossedOff'] is True]
        return (items_not_crossed, items_crossed)

    def cross_item(self,list_id, item_id, cross):
        self.loop.run_until_complete(self.og.toggle_item_crossed_off(self.list_id, item_id, cross))
