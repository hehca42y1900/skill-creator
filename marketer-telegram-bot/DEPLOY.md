# Перенос бота на сервер (VPS), чтобы работал постоянно

Локальный запуск (`python bot.py` в терминале на своём компьютере) работает,
только пока открыт терминал и включён компьютер. Чтобы бот работал 24/7 —
переносим его на недорогой VPS-сервер и запускаем как системную службу
(systemd), которая сама перезапускает бота при сбое и при перезагрузке
сервера.

Подходит любой VPS-провайдер с Ubuntu/Debian (Timeweb Cloud, Selectel,
Hetzner, DigitalOcean и т.п.) — минимальной конфигурации (1 CPU, 1 ГБ RAM)
для этого бота более чем достаточно.

## 1. Арендовать VPS и подключиться

После создания сервера у провайдера вы получите IP-адрес и пароль (или
SSH-ключ). Подключаетесь с локального компьютера:

```bash
ssh root@ВАШ_IP_АДРЕС
```

(На Windows — через PowerShell тем же способом, или через PuTTY, если
удобнее.)

## 2. Установить зависимости на сервере

```bash
apt update && apt install -y python3 python3-venv python3-pip git
```

## 3. Скачать код бота на сервер

```bash
mkdir -p /opt/marketer-telegram-bot
cd /opt/marketer-telegram-bot
git clone --branch claude/marketer-assistant-claude-api-ca8n8s https://github.com/hehca42y1900/skill-creator.git tmp
mv tmp/marketer-telegram-bot/* .
mv tmp/marketer-telegram-bot/.gitignore . 2>/dev/null
rm -rf tmp
```

## 4. Настроить окружение

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 5. Создать `.env` на сервере

`.env` в git не хранится (там секреты), поэтому создаём заново прямо на
сервере:

```bash
nano .env
```

Вставляете (тот же токен и ключ, что использовали локально, либо можно
создать отдельные — так безопаснее, чтобы локальный тест и сервер не
делили один ключ):

```
TELEGRAM_BOT_TOKEN=ваш_токен
ANTHROPIC_API_KEY=ваш_ключ
```

Сохраняете (`Ctrl+O`, Enter, `Ctrl+X` в nano).

Проверка, что всё работает, до настройки автозапуска:

```bash
python bot.py
```

Если бот ответил в Telegram — жмите `Ctrl+C` и переходите к автозапуску.

## 6. Настроить автозапуск через systemd

Скопируйте шаблон и подставьте реальные пути/пользователя:

```bash
cp marketer-bot.service.example /etc/systemd/system/marketer-bot.service
nano /etc/systemd/system/marketer-bot.service
```

Проверьте/поправьте в файле:
- `WorkingDirectory` и пути в `ExecStart` — должны указывать на
  `/opt/marketer-telegram-bot` (или куда вы фактически скачали бота).
- `User` — под каким пользователем сервера запускать (не `root`, если есть
  отдельный пользователь; если работаете только под `root` — замените
  `User=deploy` на `User=root`).

Запускаем и включаем автозапуск при перезагрузке сервера:

```bash
systemctl daemon-reload
systemctl enable marketer-bot
systemctl start marketer-bot
```

## 7. Проверка и логи

```bash
systemctl status marketer-bot
```

Должно быть `active (running)`. Логи в реальном времени:

```bash
journalctl -u marketer-bot -f
```

(`Ctrl+C` — выйти из просмотра логов, сам бот при этом продолжит работать.)

## Обновление бота после изменений в коде

```bash
cd /opt/marketer-telegram-bot
git clone --branch claude/marketer-assistant-claude-api-ca8n8s https://github.com/hehca42y1900/skill-creator.git /tmp/mb-update
cp /tmp/mb-update/marketer-telegram-bot/bot.py /tmp/mb-update/marketer-telegram-bot/system.txt .
rm -rf /tmp/mb-update
systemctl restart marketer-bot
```

(`.env` и `marketer-bot.service` на сервере не трогаются — обновляется
только код.)
