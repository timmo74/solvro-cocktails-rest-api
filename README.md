# Cocktail API - Zadanie Rekrutacyjne

Zamieszczam tutaj moje REST API z zadania rekrutacyjnego. Pierwszy raz robiłem projekt korzystając z Django, dlatego z pewnością nie wszystkie moje rozwiązania są najlepsze. Mimo tego, bardzo przyjemnie mi się nad tym pracowało i wydaję mi się, że dużo sie nauczyłem.

## O projekcie
Aplikacja to backendowy system do zarządzania bazą przepisów na koktajle. Pozwala na dodawanie składników (w tym alkoholi), komponowanie z nich receptur z określonymi proporcjami oraz wystawianie ocen przez społeczność.

## Schemat bazy danych
<img width="773" height="709" alt="image" src="https://github.com/user-attachments/assets/8ca629a9-12f4-4ddd-93e4-7187924f0cb7" />


## Realizacja wymagań:

### Wymagania podstawowe zostały spełnone:
- [x] paginacja i walidacja obecne
- [x] full CRUD
- [x] PostgreSQL z relacjami kluczy obcych

### Z Nice to have:
- [x] **Autoryzacja i użytkownicy:** Zaimplementowana autoryzacja za pomocą tokenów JWT (SimpleJWT) oraz endpoint do rejestracji.
- [x] **Powiązanie z autorem:** Koktajle są powiązane kluczem obcym z użytkownikiem, który je dodał.
- [x] **Uprawnienia:** Zastosowano `IsAuthenticatedOrReadOnly` – przeglądać mogą wszyscy, dodawać/oceniać tylko zalogowani.
- [x] **Schemat bazy danych:** Załączony powyżej.
      

## Jak uruchomić projekt lokalnie

1. **Sklonuj repozytorium:**
   ```bash
   git clone <[LINK_DO_REPOZYTORIUM](https://github.com/timmo74/solvro-cocktails-rest-api/blob/main/README.md)>
   cd mysite

2. **Utwórz i aktywuj środowisko wirtualne:**
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    # source .venv/bin/activate  # Linux/Mac

3. **Zainstaluj zależności:**
    pip install -r requirements.txt
4. **Konfiguracja bazy danych:**
    Upewnij się, że masz zainstalowanego PostgreSQL. Utwórz lokalnie bazę o nazwie cocktail_db. Następnie w pliku settings.py (w sekcji DATABASES) podmień hasło i nazwę użytkownika (USER, PASSWORD) na swoje dane dostępowe.
5. **Migracje i uruchomienie:**
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

6.**Tworzenie użytkownika:**
    Aby móc testować dodawanie przepisów i ocenianie, musisz posiadać konto.

   Przez terminal (Konto Admina): Przed uruchomieniem serwera wpisz python manage.py createsuperuser i postępuj zgodnie z                instrukcjami.

   Przez API: Uruchom serwer i wyślij żądanie POST z podanym username i password pod endpoint /register/.
