# Инструкция для AI-агента: настрой это рабочее место

> **Как этим пользоваться.** Открой папку `starter-kit` в VS Code, запусти Codex или Claude Code
> и скажи ему: **«Прочитай SETUP.md и выполни всё, что там написано».**
> Дальше агент делает всё сам, а тебе останется отвечать «да» на подтверждения.

---

## Кто ты в этой задаче

Ты — инженер, который настраивает рабочее место начинающему разработчику на **macOS**.
Человек только начал: терминала боится, Mac видит впервые, программировать не умеет.

Правила поведения:

- Объясняй каждый шаг **одной фразой на русском** перед тем, как его выполнить.
- Не выполняй разрушительных команд. Ничего не удаляй без прямого разрешения.
- Если команда требует пароль — предупреди, что символы при вводе не отображаются.
- После каждого блока — проверка, что получилось. Не переходи дальше, пока проверка не прошла.
- Если шаг упал — не пытайся обойти молча. Скажи, что именно сломалось, и предложи решение.

---

## Шаг 0. Что уже должно стоять

Проверь и доложи таблицей, что из этого есть:

```bash
sw_vers                       # версия macOS
uname -m                      # arm64 = Apple Silicon, x86_64 = Intel
code --version                # VS Code
docker --version              # Docker
python3 --version             # Python
git --version                 # Git
node -v                       # Node.js
brew --version                # Homebrew
```

Чего нет — ставим ниже. Что есть — пропускаем.

---

## Шаг 1. Homebrew

Если `brew --version` не ответил:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Важно:** после установки Homebrew печатает блок «Next steps» с двумя командами `echo`.
Их обязательно нужно выполнить, иначе система не найдёт `brew`. Для Apple Silicon это:

```bash
echo >> ~/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Проверка: `brew --version` отвечает номером версии.

---

## Шаг 2. Базовый набор

```bash
brew install git node python
brew install --cask visual-studio-code docker
```

Затем настрой Git — спроси у человека имя и почту, подставь их:

```bash
git config --global user.name "Имя Фамилия"
git config --global user.email "почта@gmail.com"
git config --global init.defaultBranch main
```

Проверка: все команды из шага 0 отвечают версиями.

---

## Шаг 3. Расширения VS Code

Ставь по одному, в этом порядке. Список и назначение — в `01-инструменты/vscode-mac.md`.

```bash
# Русский интерфейс
code --install-extension MS-CEINTL.vscode-language-pack-ru

# AI-агенты
code --install-extension openai.chatgpt          # Codex — основной агент
code --install-extension anthropic.claude-code   # Claude Code — второй агент

# Python
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-python.debugpy

# Git и Docker
code --install-extension eamodio.gitlens
code --install-extension ms-azuretools.vscode-containers

# Полезная мелочь
code --install-extension mechatroner.rainbow-csv
code --install-extension davidanson.vscode-markdownlint
```

Проверка: `code --list-extensions` показывает все установленные.

---

## Шаг 4. Правила работы агента

Скопируй правила в домашнюю папку — они действуют во всех проектах:

```bash
mkdir -p ~/.claude
cp CLAUDE.md ~/.claude/CLAUDE.md
cp AGENTS.md ~/.codex/AGENTS.md 2>/dev/null || { mkdir -p ~/.codex && cp AGENTS.md ~/.codex/AGENTS.md; }
```

Объясни человеку одной фразой, что это: **правила, по которым агент будет себя вести
во всех проектах — как отвечать, что уточнять, чего не делать.**

---

## Шаг 5. Первый проект

Создай учебный проект и покажи, что всё работает:

```bash
mkdir -p ~/Projects/hello-vibe && cd ~/Projects/hello-vibe
git init
code .
```

Внутри проекта создай `test.py` с одной строкой `print("окружение готово")`,
запусти его и покажи результат.

Затем сделай первый коммит:

```bash
git add .
git commit -m "Первый коммит: проверка окружения"
```

---

## Шаг 6. Отчёт

Выведи итоговую таблицу: что установлено, каких версий, что не удалось и почему.
Отдельно перечисли, что осталось сделать человеку руками:

- завести аккаунты (Gmail, GitHub) — если ещё нет;
- оформить подписку ChatGPT Plus и войти в Codex;
- включить VPN до входа в любой AI-сервис.

---

## Чего делать НЕ надо

- Не ставь Homebrew-пакеты, которых нет в списке выше, — окружение должно остаться маленьким.
- Не подключай MCP-серверы на этом этапе. Про них — отдельный файл `01-инструменты/mcp-servers.md`,
  их подключают позже и осознанно.
- Не меняй системные настройки macOS.
- Не трогай системный Python (`/usr/bin/python3`) — работаем только с тем, что поставил Homebrew.
