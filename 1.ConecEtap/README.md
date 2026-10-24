# ETAP 24 + VS Code: Python API Setup

My guide to connecting **ETAP 24** with **Visual Studio Code** through the ETAP Python API, using a virtual environment (`.venv`). It ends with a connection test (`ping`) and a load flow on the IEEE 4-bus example that ships with ETAP.

**Reference setup:** ETAP 24.0.1 · ETAP's bundled Python 3.11.4 · Windows

## Files

| File | Purpose |
| ---- | ------- |
| [`prueba.py`](prueba.py) | Connection test: imports `etap.api` and calls `ping()` |
| [`flujo_potencia.py`](flujo_potencia.py) | Load flow on the IEEE 4-bus example, printing results per bus |

## How it works

- **VS Code** is the editor where I run the scripts.
- **`.venv`** is a Python environment just for this project.
- **ETAP Python API** (`etap.api`) is the client library, and `connect()` talks to the local ETAP service (DataHub).

Importing `etap.api` does not prove the service is available, so I check the import and the `ping()` separately.

<!-- PEGA AQUÍ: captura del DataHub / servicio de API de ETAP funcionando. Guárdala como images/etap-datahub.png -->
![ETAP DataHub running](images/etap-datahub.png)

## Requirements

- ETAP 24 with a valid license, and VS Code with the Microsoft **Python** extension
- ETAP API service (DataHub) started and accepting local connections

Reference paths (adjust them if your ETAP is installed elsewhere):

```
ETAP's Python:     C:\ETAP 2400\ThirdParty\Python\Distro\python.exe
ETAP's libraries:  C:\ETAP 2400\ThirdParty\Python\Distro\Lib\site-packages
```

## Setup

**1. Open the project folder** in VS Code (**File → Open Folder**) and open a terminal (**Terminal → New Terminal**).

**2. Create the virtual environment with ETAP's Python**, so I start from the version ETAP expects:

```powershell
& "C:\ETAP 2400\ThirdParty\Python\Distro\python.exe" -m venv .venv
& ".\.venv\Scripts\python.exe" --version
```

Expected: Python 3.11.4. Activating the environment is optional, I can always call `.\.venv\Scripts\python.exe` directly. If I want to activate it and PowerShell blocks the script:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

**3. Let the environment find ETAP's library.** A new `.venv` does not see ETAP's packages. Instead of copying the `etap` folder, I create a file `etap_paths.pth` in `.venv\Lib\site-packages` with a single line:

```
C:\ETAP 2400\ThirdParty\Python\Distro\Lib\site-packages
```

Make sure it is not saved as `etap_paths.pth.txt`. This only adds a search path and does not modify any ETAP file. Check it:

```powershell
& ".\.venv\Scripts\python.exe" -c "import etap.api; print(etap.api.__file__)"
```

The output must be a path inside the ETAP installation, ending in `etap\api\__init__.py`.

<!-- PEGA AQUÍ: captura del archivo etap_paths.pth abierto en VS Code mostrando su ruta (recorta para que no se vea tu usuario de Windows). Guárdala como images/etap-paths-pth.png -->
![etap_paths.pth](images/etap-paths-pth.png)

**4. Select the interpreter.** Press `Ctrl+Shift+P`, choose **Python: Select Interpreter**, pick `.venv\Scripts\python.exe` of this project and open a new terminal.

**5. Run the connection test.** [`prueba.py`](prueba.py) imports `etap.api`, connects to `https://localhost:60000`, calls `ping()` and prints any error instead of crashing. If your API uses another protocol or port, change `baseAddress` in the script.

```powershell
& ".\.venv\Scripts\python.exe" .\prueba.py
```

Expected output:

```
Python: <your-project>\.venv\Scripts\python.exe
Library: C:\ETAP 2400\ThirdParty\Python\Distro\Lib\site-packages\etap\api\__init__.py
ETAP response: {"Value" : "True"}
Connection test completed.
```

<!-- PEGA AQUÍ: captura de la terminal de VS Code con el resultado {"Value" : "True"} de prueba.py (recorta la ruta de tu usuario). Guárdala como images/ping-result.png -->
![Successful ping](images/ping-result.png)

`{"Value" : "True"}` means the service answered. It does not yet prove a study ran correctly.

## Load flow example

[`flujo_potencia.py`](flujo_potencia.py) connects to ETAP, runs a load flow on the **IEEE 4-bus example that ships with ETAP** and prints, for each bus, its ID, type, nominal kV, voltage in % and angle in degrees.

1. Open the IEEE 4-bus example from your ETAP installation. *(edit: nombre exacto del proyecto y del caso de estudio)*
2. Keep ETAP open with the API service active.
3. Run `& ".\.venv\Scripts\python.exe" .\flujo_potencia.py`

The ETAP example project is not included here, since it comes with ETAP.

<!-- PEGA AQUÍ: captura de la tabla de resultados del flujo de potencia en la terminal (barra, tipo, kV, tensión, ángulo). Recorta la ruta de tu usuario. Guárdala como images/load-flow-results.png -->
![Load flow results](images/load-flow-results.png)

> Official ETAP examples can include What-If commands, such as closing a breaker, that change the study scenario. Read every command before running an example.

## Troubleshooting

| Problem | What to check |
| ------- | ------------- |
| `No module named 'etap'` | `etap_paths.pth` is in `.venv\Lib\site-packages`, it is not `.pth.txt`, the path is exact, and the script runs with the `.venv` interpreter |
| Connection refused or timeout | ETAP is open if required, the API service (DataHub) is started, protocol and port match, and no firewall blocks local connections |
| VS Code runs another Python | Check `sys.executable` and use **Python: Select Interpreter**, or run with the full `.venv\Scripts\python.exe` path |
| PowerShell blocks `Activate.ps1` | Use the session-only setting from step 2, or skip activation |
| ETAP installed elsewhere | Use the `python.exe` and `Lib\site-packages` of your own installation in steps 2 and 3 |

Before reinstalling Python or deleting `.venv`, first find out whether the import fails or the connection to the service fails.

---

Made by [@Ryanqg21](https://github.com/Ryanqg21). ETAP and its Python API belong to their respective owner and require a valid license.