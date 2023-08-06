def get_backup_settings(repository, env):
    restore_data_only = env.bool('RESTORE_DATA_ONLY', default=False)

    if restore_data_only:
        restore_options = ['data-only', 'disable-triggers', 'exit-on-error']
    else:
        restore_options = ['clean', 'create', 'exit-on-error']

    restore_options = env.list('RESTORE_OPTIONS', default=restore_options)

    connector_settings = {
        'SINGLE_TRANSACTION': False,
        'DROP': False,
        'RESTORE_SUFFIX': ' '.join([f'--{option}' for option in restore_options])
    }

    if 'create' in restore_options:
        connector_settings['NAME'] = 'postgres'

    return {
        'DBBACKUP_STORAGE': 'datamaker_backup.storage.BackupStorage',
        'DBBACKUP_STORAGE_OPTIONS': {
            'repository': repository,
            'environment': env('DEPLOYMENT_TARGET'),
            'enable_restore': env.bool('ENABLE_RESTORE', default=False),
            'enable_backup': env.bool('ENABLE_BACKUP', default=False),
        },
        'DBBACKUP_CONNECTORS': {
            'default': connector_settings
        },
        'DBBACKUP_CLEANUP_KEEP': env('DBBACKUP_CLEANUP_KEEP', default=30)
    }
