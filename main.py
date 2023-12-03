from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # User ID input
        self.add_widget(Label(text='User ID:'))
        self.user_id = TextInput(multiline=False)
        self.add_widget(self.user_id)
        
        # Password input
        self.add_widget(Label(text='Password:'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        
        # Forget Password button
        forget_password_button = Button(text='Forget Password', on_press=self.forget_password)
        self.add_widget(forget_password_button)
        
        # Remember Me checkbox
        self.add_widget(Label(text='Remember Me'))
        self.remember_me = CheckBox()
        self.add_widget(self.remember_me)
        
        # Login button
        login_button = Button(text='Login', on_press=self.login)
        self.add_widget(login_button)
    
    def login(self, instance):
        user_id = self.user_id.text
        password = self.password.text
        
        # Here, you'd validate the user credentials (e.g., against a database)
        # For this example, let's use hardcoded credentials for simplicity
        
        # Hardcoded user credentials (not secure, for demonstration only)
        valid_user = {'username': 'user', 'password': 'pass123'}
        
        if user_id == valid_user['username'] and password == valid_user['password']:
            if self.remember_me.active:
                # Save user credentials for next login (not secure, use proper encryption/hashing)
                with open("credentials.txt", "w") as file:
                    file.write(f"{user_id},{password}")
            
            self.show_welcome_popup()
        else:
            # Incorrect credentials, show error message
            self.show_error_popup()
    
    def forget_password(self, instance):
        # Implement logic for password recovery process
        pass
    
    def show_welcome_popup(self):
        # Show a welcome popup after successful login
        content = Label(text='Welcome to the Drugs Bank Pharmacy!')
        popup = Popup(title='Welcome', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()
    
    def show_error_popup(self):
        # Show an error popup for incorrect login
        content = Label(text='Incorrect username or password!')
        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(300, 150))
        popup.open()

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
