from app import app
from controller.Home import Home

app.add_url_rule("/",'mainhome', view_func=Home.to_view("mainhome", handle_name='home'), methods=['GET','POST'])
#app.add_url_rule("/home",'home', view_func=Home.as_view("chome"), methods=['GET','POST'])