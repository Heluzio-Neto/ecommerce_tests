from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.campo_login = (By.ID, 'user-name')
        self.campo_senha = (By.ID, 'password')
        self.botao_login = (By.ID, 'login-button')
        self.mensagem_erro = (
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')

    def autenticar(self, user, password):
        self.enter_text(self.campo_login, user)
        self.enter_text(self.campo_senha, password)
        self.click(self.botao_login)

    def verificar_erro(self, erro):
        mensagem = self.get_component_text(self.mensagem_erro)
        if mensagem == erro:
            return True

        return False
