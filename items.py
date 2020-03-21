pkg_apt = {
    "gnupg2": {},
    "software-properties-common": {},
    'docker-ce': {
        'needs': [
            'file:/etc/apt/sources.list.d/docker.list',
            'action:apt_update',
        ],
    },
    'docker-compose': { # Old version in Repo
        'installed': False,
    },
}

release_names = {
    'debian': {
        8: 'jessie',
        9: 'stretch',
        10: 'buster',
        11: 'bullseye',
        12: 'bookworm',
    }
}

release_name = release_names.get(node.os, {}).get(node.os_version[0], 'stretch')
config = node.metadata.get('docker', {})

downloads = {
    '/usr/local/bin/docker-compose': {
        'url': 'https://github.com/docker/compose/releases/download/' \
               '{}/docker-compose-Linux-x86_64'.format(
            config.get('compose', {}).get('version', '1.22.0')),
        'sha256': config.get('compose', {}).get('checksum',
                                                'f679a24b93f291c3bffaff340467494f388c0c251649d640e661d509db9d57e9'),
    },
}

files = {
    '/etc/apt/sources.list.d/docker.list': {
        'content': "deb [arch=amd64] https://download.docker.com/linux/{os} {release_name} stable".format(
            os=node.os, release_name=release_name),
        'needs': [
            'action:install_gpg',
        ],
        'triggers': [
            'action:apt_update',
        ],
    }
}

actions = {
    'chmod_docker-compose': {
        'command': 'chmod 0755 /usr/local/bin/docker-compose',
        'unless': 'test "`stat -c %a /usr/local/bin/docker-compose`" -eq "755"',
        'needs': [
            'download:/usr/local/bin/docker-compose',
        ],
    },
    'install_gpg': {
        'command': 'curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -',
        'unless': 'apt-key list | grep "Docker Release (CE deb) <docker@docker.com>"',
    },
    'apt_update': {
        'command': 'apt-get update',
        'triggered': True,
    },
}
