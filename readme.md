# **Technical Documentation for a "Chat" Type Application**

<a name="introduction" id="#introduction"></a>
## 1. **Introduction**

The application is based on the Flask framework and serves as a "chat" platform where users can communicate online. A user can register and then log in. Each user receives their own unique tag "#xxxx," which acts as an identifier. When adding a user, both their name and tag must be entered. After adding, a chat room is automatically created where conversations can take place.

---

<a name="requirements"></a>
## 2. **Required Libraries**

The following libraries are essential for the proper functioning of the application:

- **bidict** `0.21.2` - Provides bidirectional dictionary functionality, enabling two-way mapping.
  
- **blinker** `1.6.2` - Enables a signal system, useful for managing events and internal communication within the Flask app.

- **Bootstrap-Flask** `2.4.1` - Integrates Bootstrap with Flask, allowing for user interface styling using Bootstrap components.

- **click** `8.1.7` - A command-line interface tool that Flask uses to manage terminal commands and serve as the base for `flask` commands.

- **Flask** `3.0.3` - A microframework for building web applications in Python, providing the basic tools and servers to run the application.

- **Flask-Login** `0.6.3` - A library for managing user sessions, authorization, and authentication in the application.

- **Flask-SocketIO** `5.3.1` - An extension that enables real-time communication using the WebSocket protocol.

- **Flask-SQLAlchemy** `3.1.1` - Integrates SQLAlchemy with Flask, simplifying database management, model definition, and query execution.

- **greenlet** `3.0.1` - A library used by Flask-SocketIO for managing asynchronous connections.

- **itsdangerous** `2.2.0` - Used for secure token generation, helping to protect sessions and generate secure cookies.

- **Jinja2** `3.1.4` - A templating engine used for generating dynamic HTML pages in Flask.

- **MarkupSafe** `2.1.3` - Provides protection against XSS attacks by correctly handling certain characters in Jinja2.

- **python-engineio** `4.1.0` - A low-level engine for managing SocketIO connections, forming the foundation for Flask-SocketIO.

- **python-socketio** `5.3.0` - A Python implementation of the SocketIO protocol, used to manage SocketIO events.

- **SQLAlchemy** `2.0.34` - An ORM (Object-Relational Mapping) that simplifies working with databases by representing tables as Python classes.

- **typing_extensions** `4.11.0` - Extensions for Python's typing system, useful for creating typed code.

- **Werkzeug** `3.0.4` - A tool for creating web applications, providing routing, error handling, and debugging, serving as the foundation of Flask.

- **WTForms** `3.2.1` - Enables creation and validation of HTML forms.

---

<a name="environment-setup"></a>
## 3. **Environment Setup**

Before running the application, it is necessary to create a virtual environment and install all dependencies. Follow these steps:

### **Steps:**

1. **Install Miniconda (if not already installed):**
   - Miniconda is a lightweight version of Anaconda that allows package and environment management in Python. You can download Miniconda from the [official page](https://docs.conda.io/en/latest/miniconda.html) and follow the installation instructions.

2. **Create a new virtual environment:**
   - Open a terminal and run the following command to create a new environment with the name `myenv` (you can replace `myenv` with any name you prefer):
     ```bash
     conda create --name myenv python=3.11
     ```
   - You can also install other versions of Python by changing `3.11` to the required version.

3. **Activate the environment:**
   - After creating the environment, activate it with the command:
     ```bash
     conda activate myenv
     ```

4. **Install all dependencies:**
   - Ensure you are in the active environment, then install the required packages. You can do this using the `requirements.txt` file, if it exists:
     ```bash
     pip install -r requirements.txt
     ```

5. **Deactivate the environment after finishing work:**
   - After you finish working in the environment, deactivate it with:
     ```bash
     conda deactivate
     ```

### **Benefits of Using Miniconda:**
- **Dependency Management:** Miniconda makes it easy to install and manage packages, eliminating dependency issues.
- **Environment Creation and Management:** You can easily create, activate, and deactivate different virtual environments, allowing for project separation.
- **Support for Different Python Versions:** You can have different Python versions installed in different environments.

Following these steps will ensure you are ready to work on your application in a well-configured environment!









# **Dokumentacja Techniczna Aplikacji typu "gadu gadu"**

<a name="wprowadzenie" id="#wprowadzenie"></a>
## 1. **Wprowadzenie**

Aplikacja oparta na frameworku Flask, która stanowi platformę typu "gadu gadu", gdzie można się komunikować przez internet. Użytkownik może się zarejestrować, a następnie logować.
Każdy użytkownik otrzymuje swój tag "#xxxx", który jest identyfikatorem. Przy dodaniu użytkownika należy wpisać jego nazwę oraz jego tag. Po jego dodaniu jest
automatycznie stworzony pokój, gdzie można prowadzić rozmowę.

---

<a name="wymagania"></a>
### Wymagane Biblioteki

Aby aplikacja działała poprawnie, wymagane są następujące biblioteki:

- **bidict** `0.21.2` - Zapewnia funkcjonalność dwukierunkowego słownika, co umożliwia mapowanie w obie strony.
  
- **blinker** `1.6.2` - Umożliwia tworzenie systemu sygnałów, przydatne do zarządzania zdarzeniami i komunikacją wewnętrzną w aplikacji Flask.

- **Bootstrap-Flask** `2.4.1` - Integracja Bootstrap z Flaskiem, co umożliwia stylizację interfejsu użytkownika przy użyciu komponentów Bootstrap.

- **click** `8.1.7` - Narzędzie dla interfejsu wiersza poleceń. Flask używa go do zarządzania poleceniami terminalowymi oraz jako podstawę komend `flask`.

- **Flask** `3.0.3` - Mikroframework do budowy aplikacji webowych w Pythonie, zapewniający podstawowe narzędzia i serwery do uruchamiania aplikacji.

- **Flask-Login** `0.6.3` - Biblioteka do zarządzania sesjami użytkowników, autoryzacją i uwierzytelnianiem w aplikacji.

- **Flask-SocketIO** `5.3.1` - Rozszerzenie umożliwiające komunikację w czasie rzeczywistym przy użyciu protokołu WebSocket.

- **Flask-SQLAlchemy** `3.1.1` - Integracja SQLAlchemy z Flaskiem, ułatwiająca zarządzanie bazą danych, definiowanie modeli oraz wykonywanie zapytań.

- **greenlet** `3.0.1` - Biblioteka wykorzystywana przez Flask-SocketIO do zarządzania asynchronicznymi połączeniami.

- **itsdangerous** `2.2.0` - Służy do bezpiecznego generowania tokenów, wykorzystywana do ochrony sesji i generowania bezpiecznych cookies.

- **Jinja2** `3.1.4` - Silnik szablonów, używany do generowania dynamicznych stron HTML w Flasku.

- **MarkupSafe** `2.1.3` - Zapewnia ochronę przed atakami XSS, przez prawidłowe traktowanie niektórych znaków w Jinja2.

- **python-engineio** `4.1.0` - Niskopoziomowy silnik do zarządzania połączeniami SocketIO, na którym opiera się Flask-SocketIO.

- **python-socketio** `5.3.0` - Implementacja protokołu SocketIO dla Pythona, używana do zarządzania zdarzeniami SocketIO.

- **SQLAlchemy** `2.0.34` - ORM (Object-Relational Mapping), który ułatwia pracę z bazami danych poprzez reprezentację tabel jako klas Pythona.

- **typing_extensions** `4.11.0` - Rozszerzenia dla systemu typów Pythona, które są przydatne przy tworzeniu kodu typowanego.

- **Werkzeug** `3.0.4` - Narzędzie do tworzenia aplikacji webowych, zapewniające routing, błędy i debugowanie, będące podstawą Flaska.

- **WTForms** `3.2.1` - Umożliwia tworzenie oraz walidację formularzy HTML.

---

<a name="konfiguracja-środowiska"></a>
## 2. **Konfiguracja Środowiska**

Przed uruchomieniem aplikacji konieczne jest utworzenie wirtualnego środowiska i zainstalowanie wszystkich zależności. W tym celu należy postępować zgodnie z poniższymi krokami:

### **Kroki:**

1. **Zainstaluj Miniconda (jeśli jeszcze go nie masz):**
   - Miniconda to lekka wersja Anacondy, która pozwala na zarządzanie pakietami i środowiskami w Pythonie. Możesz pobrać Minicondę ze strony [oficjalnej](https://docs.conda.io/en/latest/miniconda.html) i postępować zgodnie z instrukcjami instalacji.

2. **Utwórz nowe środowisko wirtualne:**
   - Otwórz terminal i uruchom poniższe polecenie, aby utworzyć nowe środowisko z nazwą `myenv` (możesz zastąpić `myenv` dowolną nazwą):
     ```bash
     conda create --name myenv python=3.11
     ```
   - Możesz także zainstalować inne wersje Pythona, zmieniając `3.9` na wersję, której potrzebujesz.

3. **Aktywuj środowisko:**
   - Po utworzeniu środowiska, aktywuj je poleceniem:
     ```bash
     conda activate myenv
     ```

4. **Zainstaluj wszystkie zależności:**
   - Upewnij się, że znajdujesz się w aktywnym środowisku, a następnie zainstaluj potrzebne pakiety. Możesz to zrobić, korzystając z pliku `requirements.txt`, jeśli taki istnieje:
     ```bash
     pip install -r requirements.txt
     ```

5. **Zdezaktywuj środowisko po zakończeniu pracy:**
   - Po zakończeniu pracy w środowisku, możesz je dezaktywować:
     ```bash
     conda deactivate
     ```

### **Zalety korzystania z Minicondy:**
- **Zarządzanie zależnościami:** Miniconda ułatwia instalację i zarządzanie pakietami, eliminując problemy z zależnościami.
- **Tworzenie i zarządzanie środowiskami:** Możesz łatwo tworzyć, aktywować i dezaktywować różne środowiska wirtualne, co pozwala na separację projektów.
- **Wsparcie dla różnych wersji Pythona:** Możesz mieć różne wersje Pythona zainstalowane w różnych środowiskach.

Dzięki tym krokom będziesz gotowy do pracy nad swoją aplikacją w dobrze skonfigurowanym środowisku!

---

