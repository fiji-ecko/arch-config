BASE_PACKAGES = [
    # main
    "plasma",
    "waybar",
    "yazi",
    "git",
    "fastfetch",
    "firefox",
    "libreoffice-fresh",
    "wofi",
    "hypridle",
    "hyprshot", 
    "hyprlock",
    "docker",

    # terminal
    "foot",  # Эмулятор терминала
    "wget",  # Получить файлы с использованием HTTP/S, FTP
    "fish",  # Shell для работы с терминалом
    "calcurse",  # Консольный календарь
    "sudo",  # Выполнение команд с правами root
    "tree",  # Отобразить дерево
    "openvpn",  # Поддержка протокола OpenVPN
    "networkmanager-openvpn"
   
    # monitoring
    "htop", "btop",  # Системные мониторы 
    "nvtop", # Позволяет посмотреть нагрузку на GPU в режиме терминала

    # media
    "grim", "slurp", "wl-clipboard",
    "ffmpeg",  # Утилита для работы с медиа
    "awww",
    "ncmpcpp", "mpd",  # Клиент для работы с медиа 
    "mpc", # Минималистичный интерфейс командной строки для MPD
    "mpv",  # Просмотр видео
    "pamixer",
    "audacity",  # Работа со звуком
    
    # audio
    "pipewire", "pipewire-pulse", "pipewire-alsa", "wireplumber",

    # reader / archives
    "zathura", "zat / mediahura-djvu", "zathura-pdf-mupdf",  # Просмотр PDF, DJVU, EPUB файлов
    "evince",  # Читалка PDF 
    "gzip", "p7zip", "unrar", "zip", "unzip", "xarchiver",  # Работа с архивами
    
    # drivers
    "mesa", "lib32-mesa", "xf86-video-nouveau", "xf86-video-intel", "vulkan-intel"  # Necessary drivers
    "intel-ucode",  # Микрокод для процессоров intel
    "brightnessctl",  # Используется для управления яркостью (bin/brightness)  
    "gvfs", "gvfs-mtp",  # Поддержка MTP протокола, монтирование Android через USB
    "networkmanager",
    
    # bluetooth
    "bluez", "bluez-utils",  # Пакеты для модуля блютуз
    "bluetuith",  # TUI менеджер управления bluetooth
    
    # system utils
    "npm",  # Зависимость для других компонентов
    "gparted",  # Работа с носителями в системе
    "gnu-netcat",  # Утилиты для работы с сетью
    "usbutils",  # Утилиты для работы с USB-устройствами
    "sshfs",  # Монтирование удаленных SSH каталогов локально
    "openssh",  # Набор программ для поддержки SSH
    
    # fonts
    "noto-fonts", "noto-fonts-emoji", "noto-fonts-cjk",
    "ttf-fira-code", "ttf-iosevka-nerd",  # Базовые шрифты
    "ttf-jetbrains-mono", "ttf-jetbrains-mono-nerd",  # Базовые шрифты
]

DEV_PACKAGES = [
    # Creation
    "krita",  # Софт для рисования
    "kdenlive",  # Монтаж видео
    "obs-studio",  # Запись видео и управление трансляциями
    "neovim",  # Консольный редактор кода
   
    # Git
    "lazygit",  # Удобный интерфейс для управления git
    "timeshift",  # Софт для бэкапов
    "filezilla",  # Работа с FTP из графической среды
    "veracrypt",  # Создание криптоконтейнеров

    # Web
    "wireshark-qt",  # Перехват и анализ сетевых пакетов
    "chromium",  # Дополнительный браузер
    "telegram-desktop",  # Мессенджер
    "qBittorrent",  # Торрент клиент
   
    # SQL 
    "sqlitebrowser",  # Работа с SQLite базами
    
    # Notes
    "obsidian",  # Работа с заметками
    "bitwardern-bin",  # Защищенный менеджер паролей
    
    # Python
    "python-pip",  # Система управления пакетами Python
]

AUR_PACKAGES = [
    "cava",  # Вывод спектра для музыки
    "anki",  # Программа для запоминания материала через карточки
]
