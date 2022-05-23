from core.Pantheon import api, app

api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)