from modules.Pantheon import api, app
from modules.Pantheon.Config import system_config
api.init_app(app)

if __name__ == "__main__":
    app.run(
        debug=system_config.debug,
        port=system_config.port,
        host=system_config.bind_addr,
    )