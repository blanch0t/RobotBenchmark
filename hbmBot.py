from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from pyautogui import write

class Bot():

    def __init__(self):
        S = Service("C:\\Users\\tblch\\github\\geoGuessrStatBot\\chromedriver.exe")
        brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

        options = Options()
        options.binary_location = brave_path

        self.driver = webdriver.Chrome(service=S, options=options)

    def allow(self):
        self.driver.execute_script("document.getElementsByClassName('Card__CardBody-sc-1s2p2gv-2 Layer__LayerBody-sc-3vtlsk-2 bWYsaP cLFYDn')[0].scrollTop = document.getElementsByClassName('Card__CardBody-sc-1s2p2gv-2 Layer__LayerBody-sc-3vtlsk-2 bWYsaP cLFYDn')[0].scrollHeight;")
        sleep(1)
        self.driver.find_elements(By.TAG_NAME, 'Button')[2].click()
        sleep(1)

    def reactiontime(self):

        def play(browser):
            red = True
            while red:
                try:
                    browser.find_elements(By.CLASS_NAME, 'view-go.e18o0sx0.css-saet2v.e19owgy77')[0].click()
                    red = False
                except IndexError:
                    pass

        def next(browser):
            browser.find_element(By.CLASS_NAME, 'view-result.e18o0sx0.css-saet2v.e19owgy77').click()

        def end(browser):
            browser.find_elements(By.TAG_NAME, 'Button')[1].click()
            sleep(1)

        self.driver.get('https://humanbenchmark.com/tests/reactiontime')
        sleep(3)
        # self.allow()

        self.driver.find_element(By.CLASS_NAME, 'view-splash.e18o0sx0.css-saet2v.e19owgy77').click()

        for _ in range(4):
            play(self.driver)
            sleep(1)
            next(self.driver)
        play(self.driver)
        sleep(1)
        end(self.driver)

    def numbermemory(self):

        def play(browser):
            ans = browser.find_element(By.CLASS_NAME, 'big-number ').get_attribute('innerHTML')
            running = True
            while running:
                try:
                    input = browser.find_elements(By.TAG_NAME, 'input')[0]
                    input.send_keys(ans)
                    running = False
                    sleep(1)
                except IndexError:
                    pass
            browser.find_elements(By.TAG_NAME, 'Button')[1].click()
            sleep(1)
            browser.find_elements(By.TAG_NAME, 'Button')[1].click()
            sleep(1)

        def end(browser):
            running = True
            while running:
                try:
                    input = browser.find_elements(By.TAG_NAME, 'input')[0]
                    input.send_keys('69')
                    running = False
                    sleep(1)
                except IndexError:
                    pass
            browser.find_elements(By.TAG_NAME, 'Button')[1].click()
            sleep(1)
            browser.find_elements(By.TAG_NAME, 'Button')[1].click()
            sleep(1)

        self.driver.get('https://humanbenchmark.com/tests/number-memory')
        sleep(3)
        # self.allow()
        self.driver.find_elements(By.TAG_NAME, 'Button')[1].click()
        for _ in range(20):
            play(self.driver)
        end(self.driver)

    def aim(self):

        self.driver.get('https://humanbenchmark.com/tests/aim')
        sleep(3)
        # self.allow()
        for _ in range(31):
            action = ActionChains(self.driver)
            target = self.driver.find_element(By.CLASS_NAME, 'css-z6vxiy.e6yfngs3')
            action.move_to_element_with_offset(target, 0, 0)
            action.click()
            action.perform()
        sleep(1)
        self.driver.find_elements(By.TAG_NAME, 'button')[1].click()
        sleep(1)

    def verbalmemory(self):

        self.driver.get('https://humanbenchmark.com/tests/verbal-memory')
        sleep(3)
        # self.allow()
        self.driver.find_elements(By.TAG_NAME, 'Button')[1].click()
        dico = set()
        for _ in range(300):
            sleep(0.07)
            word = self.driver.find_element(By.CLASS_NAME, 'word').get_attribute('innerHTML')
            self.driver.find_elements(By.TAG_NAME, 'Button')[2-(word in dico)].click()
            dico.add(word)
        for _ in range(3):
            sleep(0.07)
            word = self.driver.find_element(By.CLASS_NAME, 'word').get_attribute('innerHTML')
            self.driver.find_elements(By.TAG_NAME, 'Button')[1+(word in dico)].click()
            dico.add(word)
        self.driver.find_elements(By.TAG_NAME, 'button')[1].click()
        sleep(1)


    def typing(self):

        self.driver.get('https://humanbenchmark.com/tests/typing')
        sleep(3)
        # self.allow()
        char_containers = self.driver.find_elements(By.CLASS_NAME, 'incomplete')
        chars = [container.get_attribute('innerHTML') for container in char_containers]
        text = ''
        for char in chars:
            text += char
        write(text, interval=0.03)
        sleep(1)
        self.driver.find_elements(By.TAG_NAME, 'Button')[1].click()
        sleep(1)

    def chimp(self):

        def play(browser):
            browser.find_elements(By.TAG_NAME, 'button')[1].click()
            sleep(1)
            visibles = browser.find_elements(By.CLASS_NAME, 'css-19b5rdt')
            for card in visibles:
                if card.get_attribute('data-cellnumber') == '1':
                    card.click()
                    break
            hidden = browser.find_elements(By.CLASS_NAME, 'css-10qtjsi')
            arr = sorted(hidden, key=lambda x: int(x.get_attribute('data-cellnumber')))
            for card in arr:
                card.click()

        self.driver.get('https://humanbenchmark.com/tests/chimp')
        sleep(3)
        # self.allow()

        self.driver.find_elements(By.TAG_NAME, 'Button')[1].click()
        sleep(1)

        visibles = self.driver.find_elements(By.CLASS_NAME, 'css-19b5rdt')
        toclick = sorted(visibles, key=lambda x: int(x.get_attribute('data-cellnumber')))
        for card in toclick:
            card.click()

        for _ in range(36):
            play(self.driver)
        self.driver.find_elements(By.TAG_NAME, 'Button')[1].click()
        sleep(1)


    def memory(self):

        def play(browser):
            whites_coords = []
            grid = browser.find_element(By.CLASS_NAME, 'css-hvbk5q.eut2yre0')
            lines = grid.find_elements(By.XPATH, './*')
            for i in range(len(lines)):
                line = lines[i].find_elements(By.XPATH, './/*')
                for j in range(len(line)):
                    cell = line[j]
                    if cell.get_attribute('class') == 'active css-lxtdud eut2yre1':
                        whites_coords.append((i,j))
            sleep(1)
            for i in range(len(lines)):
                line = lines[i].find_elements(By.XPATH, './/*')
                for j in range(len(line)):
                    cell = line[j]
                    if (i,j) in whites_coords:
                        cell.click()
            sleep(2)

        self.driver.get('https://humanbenchmark.com/tests/memory')
        sleep(3)
        # self.allow()

        self.driver.find_elements(By.TAG_NAME, 'Button')[1].click()
        sleep(1)

        while True:
            play(self.driver)

    def sequence(self):
        If, Jf = None, None
        def play(browser, turn):
            nonlocal If
            nonlocal Jf
            cards = []
            for k in range(turn):
                try:
                    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'square.active')))
                    cards.append(element.location)
                    sleep(0.5-(k/(15*turn)))
                except TimeoutException:
                    print("pas trouve")
            sleep(0.1)
            carres = browser.find_elements(By.CLASS_NAME, 'square')
            xs = [carre.location['x'] for carre in carres]
            ys = [carre.location['y'] for carre in carres]
            grid = browser.find_element(By.CLASS_NAME, 'squares')
            for element in cards:
                if element['y'] == max(ys):
                    I = 2
                elif element['y'] == min(ys):
                    I = 0
                else:
                    I = 1
                if element['x'] == max(xs):
                    J = 2
                elif element['x'] == min(xs):
                    J = 0
                else:
                    J = 1
                if turn == 1:
                    If, Jf = I, J
                line = grid.find_elements(By.XPATH, './*')[I]
                cell = line.find_elements(By.XPATH, './*')[J]
                cell.click()
                sleep(0.1)

        self.driver.get('https://humanbenchmark.com/tests/sequence')
        sleep(3)
        self.allow()
        self.driver.find_elements(By.TAG_NAME, 'Button')[1].click()
        turn = 1
        while turn <= 23:
            play(self.driver, turn)
            turn += 1
        sleep(30)
        P = lambda x: int(1 - (3*x*x/2) + (5*x/2))
        grid = self.driver.find_element(By.CLASS_NAME, 'squares')
        line = grid.find_elements(By.XPATH, './*')[P(If)]
        cell = line.find_elements(By.XPATH, './*')[P(Jf)]
        cell.click()
        self.driver.find_elements(By.TAG_NAME, 'Button')[1].click()
        sleep(1)

def main():
    bot = Bot()
    bot.sequence()
    bot.verbalmemory()
    bot.typing()
    bot.reactiontime()
    bot.chimp()
    bot.numbermemory()
    bot.aim()
    bot.memory()
    sleep(100)

if __name__ == '__main__':
    main()
