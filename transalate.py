from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from time import sleep

class Trans(object):
    def __init__(self,timeout= None):
        self.timout = timeout
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
 
                 #   Modo de interfaz
        # self.browser = webdriver.Chrome()
 
    def __del__(self):
        self.browser.close()
 
    def get_trans(self):
        self.browser.get("https://translate.google.com/")
        words = self.input_words()
        self.browser.find_element_by_id("source").send_keys(words)
        sleep(1)
        self.working(words)
 
    def working(self,words):
        page_html = self.browser.page_source
        page_tree = etree.HTML(page_html)
        res_items = []
        res_item = {}
        my_result = page_tree.xpath("//div[@class='source-target-row']//span/span[1]/text()")[0].strip()
        res_item['{}'.format(words)] = my_result
        res_items.append(res_item)
        # print(res_items)
        print ("{} El resultado de la traducción es: {}". formato (palabras, mi_resultado))
 
                 #Escribir archivo:
        save_it = input ("Ingrese para guardar en local, no se guarda ningún carácter:")
        if save_it =="":
            res_ = "{}-----------{}".format(my_result, words)
            with open(r".\word_book.txt", 'a', encoding='utf8') as fp:
                fp.write(res_)
                fp.write("\n")
                fp.close()
        else:
            pass
        
 
    def input_words(self):
        words = input ("Por favor ingrese el texto a traducir:")
        language = input ("El idioma a traducir (chino / inglés):")
        if language == " ":
            self.browser.find_element_by_xpath("//div[@class='tl-sugg']//div[@id='sugg-item-en']").click()
            sleep(1)
        elif language == " ":
            self.browser.find_element_by_xpath("//div[@class='tl-sugg']//div[@id='sugg-item-zh-CN']").click()
            sleep(1)
        # Traducido por defecto al inglés
        else:
            self.browser.find_element_by_xpath("//div[@class='tl-sugg']//div[@id='sugg-item-en']").click()
            sleep(1)
        # pass
        # palabras = "Inteligencia artificial"
        return words
 
if __name__ == '__main__':
    process = Trans()
    process.get_trans()
