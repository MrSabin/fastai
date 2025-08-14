# Разработчикам бэкенда

## Как развернуть local-окружение

### Необходимое ПО

Для запуска ПО вам понадобятся консольный Git и Make. Инструкции по их установке ищите на
официальных сайтах:

- [Git SCM](https://git-scm.com/)
- [GNU Make](https://www.gnu.org/software/make/)

Вы можете проверить, установлены ли эти программы с помощью команд:
```shell
$ git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]
<...>

$ make --help
Usage: make [options] [target] ...
Options:
<...>
```

Для тех, кто использует Windows необходимы также программы **git** и **git bash**. В git bash надо добавить ещё команду
make:

- Go to [ezwinports](https://sourceforge.net/projects/ezwinports/files/)
- Download make-4.4.1-without-guile-w32-bin.zip (get the version without guile)
- Extract zip
- Copy the contents to C:\ProgramFiles\Git\mingw64\ merging the folders, but do NOT overwrite/replace any exisiting
  files.

Все дальнейшие команды запускать из-под **git bash**.

#### Локальный сервер minio

Для хранения сгенерированных сайтов и изображений необходимо установить локальный сервер **minio** и клиент для настройки и управления **mc**. Инструкции по установке:

- [minio](https://github.com/minio/minio)
- [mc](https://docs.min.io/community/minio-object-store/reference/minio-mc.html#install-mc)

После установки запускаем сервер:

```shell
$ ./minio server /<Директория для хранилища minio>
MinIO Object Storage Server
Copyright: 2015-2025 MinIO, Inc.
License: GNU AGPLv3 - https://www.gnu.org/licenses/agpl-3.0.html
Version: RELEASE.2025-07-23T15-54-02Z (go1.24.5 linux/amd64)

API: http://192.168.31.23:9000  http://192.168.31.20:9000  http://172.17.0.1:9000  http://172.18.0.1:9000  http://172.19.0.1:9000  http://127.0.0.1:9000
   RootUser: minioadmin
   RootPass: minioadmin

WebUI: http://192.168.31.23:42067 http://192.168.31.20:42067 http://172.17.0.1:42067 http://172.18.0.1:42067 http://172.19.0.1:42067 http://127.0.0.1:42067
   RootUser: minioadmin
   RootPass: minioadmin
<...>
```

Заходим в веб-интерфейс по адресу, который выдаст сервер, в данном случае **http://127.0.0.1:42067** и создаем бакет. Бакет по умолчанию создается типа **Private**, чтобы сделать его публичным нужно зарегистрировать алиас для нашего сервера используя один из адресов API в **mc** и изменить права доступа:

```shell
$ mc alias set 'myminio' 'http://192.168.31.23:9000' 'minioadmin' 'minioadmin'
$ mc anonymous set public myminio/<Название бакета>
```

### Настройка pre-commit хуков

В репозитории используются хуки pre-commit, чтобы автоматически запускать линтеры и автотесты. Перед началом разработки
установите [pre-commit package manager](https://pre-commit.com/).

В корне репозитория запустите команду для настройки хуков:

```shell
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

В последующем при коммите автоматически будут запускаться линтеры и автотесты. Есть линтеры будет недовольны, то коммит прервётся с ошибкой.

### Создание виртуального окружения для работы с IDE

IDE для корректной работы подсказок необходимо развернуть виртуальное окружение со всеми установленными зависимостями.

В качестве пакетного менеджера на проекта используется [uv](https://docs.astral.sh/uv/).

Установите [uv](https://docs.astral.sh/uv/) и в корне репозитория выполните команду

```shell
$ uv sync
```

[uv](https://docs.astral.sh/uv/) создаст виртуальное окружение, установит необходимую версию Python и все необходимые зависимости.

После этого активируйте виртуальное окружение в текущей сессии терминала:

```shell
$ source .venv/bin/activate  # для Linux
$ .\.venv\Scripts\activate  # Для Windows
```

## Как вести разработку

Код проекта находится в папке `/src`.

Находясь в корневой директории проекта, запустить проект можно командой:

```shell
$ fastapi dev src/main.py
```

Проект будет работать по адресу http://127.0.0.1:8000/

### Как установить python-пакет в виртуальное окружение

В качестве менеджера пакетов используется [uv](https://docs.astral.sh/uv/).

Вот пример как добавить в зависимости библиотеку `beautifulsoup4`.

```shell
$ uv add beautifulsoup4
```

Конфигурационные файлы `pyproject.toml` и `uv.lock` обновятся автоматически.

Аналогичным образом можно удалять python-пакеты:

```shell
$ uv remove beautifulsoup4
```

Если необходимо обновить `uv.lock` вручную, то используйте команду:

```shell
$ uv lock
```

### Команды для быстрого запуска с помощью make

Для часто используемых команд подготовлен набор альтернативных коротких команд `make`.

```shell
$ make help
Cписок доступных команд:
lint                      Проверяет линтерами код в репозитории
format                    Автоматически исправляет форматирование кода -- порядок импортов, лишние пробелы и т.д.
help                      Отображает список доступных команд и их описания
```
