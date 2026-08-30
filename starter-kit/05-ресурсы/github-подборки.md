# Куда идти дальше: подборки и материалы

> Проверенные ссылки на август 2026. Не пытайся изучить всё —
> открывай, когда появилась конкретная потребность.

---

## Скиллы и настройки агентов

| Ресурс | Что там | Когда открывать |
|---|---|---|
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 1000+ скиллов от команд и сообщества, работают в Claude Code, Codex, Cursor, Gemini CLI | Когда нужен скилл под конкретную задачу |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Скиллы, агенты, статус-лайны, инструменты, плагины | Обзор экосистемы целиком |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Каталог скиллов с описаниями | Поиск по теме |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Ещё один каталог, с пояснением формата | Разобраться, как устроен `SKILL.md` |

**Как пользоваться:** нашёл нужный скилл → прочитал `SKILL.md` целиком →
скопировал папку в `~/.claude/skills/`. Читать обязательно: скилл — это инструкции,
которые агент выполнит.

---

## Про сам подход

| Ресурс | Что там |
|---|---|
| [github/spec-kit](https://github.com/github/spec-kit) | Инструмент от GitHub для цикла «спецификация → план → задачи → код». Работает с Codex, Claude Code, Copilot, Cursor |
| [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | Тяжёлый фреймворк с ролями: аналитик, продакт, архитектор, разработчик, тестировщик. Полезно посмотреть, как разделяют роли |
| [taskade/awesome-vibe-coding](https://github.com/taskade/awesome-vibe-coding) | Большая подборка: инструменты, практики, ссылки |
| [filipecalegario/awesome-vibe-coding](https://github.com/filipecalegario/awesome-vibe-coding) | То же, другой составитель — местами полнее по инструментам |
| [analyticalrohit/awesome-vibe-coding-guide](https://github.com/analyticalrohit/awesome-vibe-coding-guide) | Практические приёмы и правила контролируемой работы с AI |

Начинать стоит не с инструментов, а с привычки: пять вопросов → SPEC → PLAN → шаг за шагом.
Инструмент осваивается за час, привычка — за месяц. Вторая ценнее.

---

## Официальная документация

| Что | Ссылка |
|---|---|
| Codex — установка и возможности | https://developers.openai.com/codex/ |
| Claude Code — документация | https://docs.claude.com/en/docs/claude-code/overview |
| MCP — протокол и список серверов | https://modelcontextprotocol.io |
| Git — учебник на русском | https://git-scm.com/book/ru/v2 |
| Python — официальный учебник | https://docs.python.org/3/tutorial/ |

---

## Как искать самому

**На GitHub** — по темам:

- [github.com/topics/vibe-coding](https://github.com/topics/vibe-coding)
- [github.com/topics/claude-code](https://github.com/topics/claude-code)
- [github.com/topics/mcp-server](https://github.com/topics/mcp-server)

Фильтр по звёздам и дате последнего коммита. Репозиторий без изменений больше года —
скорее всего, мёртвый.

**Признаки полезного репозитория:**

- есть README с примерами, а не только список ссылок;
- последний коммит свежее трёх месяцев;
- в issues отвечают.

**Признаки бесполезного:**

- список из 500 ссылок без пояснений, что и когда применять;
- «awesome»-список, состоящий из других «awesome»-списков;
- обещания «10x продуктивности» в заголовке.

---

## Чего в подборках нет

Ни один список не заменит две вещи:

**Собственный `CLAUDE.md`.** Правила, выросшие из твоих ошибок, работают лучше любых
скачанных. Ведёшь его месяц — получаешь то, чего нет ни в одном репозитории.

**Прочитанный собственный код.** Скачать сто скиллов проще, чем разобраться в двухстах
строках, которые агент написал вчера. Но работает только второе.
