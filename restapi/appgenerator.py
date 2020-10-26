from flask import Flask
from flask_cors import CORS
from restapi.db import init_db

def create_app():
    app = Flask(__name__)
    CORS(app, resources=[r'/api/*'], methods=['GET'])
    app.config.from_pyfile('config.py')
    init_db(app)
    from restapi.circuits.endpoints import circuit_bp
    from restapi.drivers.endpoints import driver_bp
    from restapi.races.endpoints import race_bp
    from restapi.results.endpoints import result_bp
    from restapi.standings.endpoints import standings_bp
    from restapi.teams.endpoints import team_bp
    app.register_blueprint(circuit_bp)
    app.register_blueprint(driver_bp)
    app.register_blueprint(race_bp)
    app.register_blueprint(result_bp)
    app.register_blueprint(standings_bp)
    app.register_blueprint(team_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
