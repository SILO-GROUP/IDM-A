from apis import api
from core.Pantheon.AppFactory import app

api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)