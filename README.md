Тесты c применением библиотеки requests для [API SpaceX](https://docs.spacexdata.com/#00ac651a-8ba2-4b4c-858a-4034dd1254fa)

## Для запуска тестов в директории requests_tests:
1. Настройте виртуальное окружение
```bash
python -m venv venv
```
Для macOS/Linux
```bash
source venv/bin/activate
```
Для Windows
```bash
source venv/Scripts/activate
```
2. Установите зависимости
```bash
pip install -r requirements.txt
```
3. Запустите тесты
```bash
pytest
```
## Тестируемые эндпоинты:
- GET /capsules/{id}
- GET /dragons/{id}
- GET /info
- GET /landpads
