# Installation

## .env
.env 파일에 아래 환경변수를 적절히 활용

### ENABLE_RESTORE
`true`|`false`

`dbrestore`, `mediarestore` 사용 가능 여부. 주로 production 환경에서는 비활성화.

Default: `false`

### ENABLE_BACKUP
`true`|`false`

`dbbackup`, `mediabackup` 사용 가능 여부. 주로 development 환경에서는 비활성화.

Default: `false`

### RESTORE_DATA_ONLY
`true`|`false`

`dbrestore`시 schema는 그대로 두고 data만 복원할지 여부.

아직까지는 해당 옵션을 활성화 할 경우 복원할 db에 data가 모두 삭제된 상태로 두어야 함.

Default: `false`

### RESTORE_OPTIONS
comma separated list of pg_restore option names

Example:
`clean,create`

Default:
- `RESTORE_DATA_ONLY`가 `true`일 때에는 `data-only,disable-triggers,exit-on-error`
- `RESTORE_DATA_ONLY`가 `false`일 때에는 `clean,create,exit-on-error`

## settings.py

settings.py에 아래 내용 추가

```python
from datamaker_backup import get_backup_settings

...

INSTALLED_APPS = (
    ...
    'dbbackup',  # django-dbbackup
)

...


# datamaker-backup
# https://github.com/datamaker-kr/datamaker-backup

BACKUP_CONFIG = get_backup_settings('<repository-name>', env)
vars().update(BACKUP_CONFIG)
```
