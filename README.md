# gear


## Project structure

```ascii
gear/
├── gear_backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── models.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_routes.py
│   │   └── test_models.py
│   ├── config.py
│   ├── requirements.txt
│   └── run.py
│   ├── venv/
├── gear_frontend/
│   ├── public/
│   ├── src/
│   └── package.json
|   |-- tests/
|   |   |-- bdd/
|   |   |   |-- features/
|   |   |   |   |-- user_registration.feature
|   |   |   |   |-- product_listing.feature
|   |   |   |   |-- ...
|   |   |   |-- step_definitions/
|   |   |   |   |-- user_registration.js
|   |   |   |   |-- product_listing.js
|   |   |   |   |-- ...
|   |   |   |-- support/
|   |   |   |   |-- world.js
|   |   |   |   |-- ...
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
```


In this structure, the backend is located in the `backend` folder and contains the Flask application code, while the frontend is located in the `frontend` folder and contains a React application. The `requirements.txt` file in the backend folder lists all the required Python packages, and the `package.json` file in the frontend folder lists all the required npm packages. The `config.py` file contains configuration settings for the Flask application. The `run.py` file is the entry point for starting the Flask application. The public folder in the frontend folder contains static files, and the src folder contains the React components and other JavaScript code. The Dockerfile and `docker-compose.yml` files can be used to containerize the application, and the `.gitignore` file lists files and directories that should be ignored by Git.

The `__init__.py` file in the app folder is the entry point of the Flask application.
The routes.py file contains the routing information for the different endpoints of the application.

The models.py file contains the database models for the application.
The tests folder contains the pytest testing code.
The __init__.py file in the tests folder is used to import the test modules into the testing framework.
The test_routes.py and test_models.py files contain the tests for the routes and models respectively.
The venv folder contains the virtual environment for the backend.

The features folder contains the Gherkin feature files, which describe the behavior of the application.
The step_definitions folder contains the implementation of the steps in the feature files, usually in JavaScript if using CucumberJS.
The support folder contains helper classes and functions used by the step definitions.

## Erstellen einer virtuellen Umgebung

Sie können eine virtuelle Umgebung mit pip erstellen, indem Sie die folgenden Schritte ausführen:

1. Öffnen Sie eine Kommandozeile oder ein Terminal.
2. Navigieren Sie zu dem Ordner, in dem Sie Ihre virtuelle Umgebung erstellen möchten.
3. Führen Sie den Befeh ```python3 -m venv myenv``` aus, um eine virtuelle Umgebung namens ```myenv``` zu erstellen.
4. Aktivieren Sie Ihre virtuelle Umgebung mit dem Befehl ```source myenv/bin/activate``` (für Linux/macOS) oder ```myenv\Scripts\activate``` (für Windows). Ihre Shell-Prompt sollte nun den Namen der virtuellen Umgebung anzeigen.
5. Überprüfen Sie, ob Sie die aktuelle Version von pip installiert haben, indem Sie den Befehl ```pip --version``` ausführen. Wenn nicht, aktualisieren Sie pip mit dem Befehl ```pip install --upgrade``` pip.
6. Überprüfen Sie, ob die virtuelle Umgebung aktiviert wurde, indem Sie den Befehl ```which python``` ausführen. Es sollte auf den Pfad in Ihrer virtuellen Umgebung verweisen.
7. Installieren Sie jetzt die benötigten Pakete mit dem Befehl ```pip install <Paketname>```.
8. Jetzt können Sie in Ihrer virtuellen Umgebung arbeiten und sicherstellen, dass Ihre Abhängigkeiten von anderen Projekten getrennt sind.
9. Um Ihre virtuelle Umgebung zu deaktivieren, geben Sie den Befehl ```deactivate``` ein.
10. Um Ihre virtuelle Umgebung später wieder zu verwenden, wechseln Sie in das Verzeichnis, in dem es erstellt wurde, und aktivieren Sie es erneut mit dem Befehl source ```myenv/bin/activate``` (für Linux/macOS) oder ```myenv\Scripts\activate``` (für Windows).