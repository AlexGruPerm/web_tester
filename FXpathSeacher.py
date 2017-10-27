from lxml import html

class XpathSearch():
    '''Class for search Xpath in str object with html of lxml'''
    def __init__(self, str_content):
        '''Class constructor, set initial variable - content (str type).'''
        self.content = str_content

    def search(self,what,show_debug):
        '''Make search of what in content'''
        tree = html.fromstring(self.content)
        s = tree.xpath(what)
        if show_debug:
            for node in s:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print(node.tag," ",node.keys()," ",node.values()," ",node.get('name')," ",node.text)
                # print('name =',node.get('name')) # Выводим параметр name
                # print('text =', node.text)  # Выводим текст элемента
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return s

    def print_html_elm(self,elm):
        #print(elm.tag, " ", elm.keys(), " ", elm.values(), " ", elm.get('abbr'), " ", elm.text)
        print(elm.tag, " ", elm.get('class')," ",elm.text)