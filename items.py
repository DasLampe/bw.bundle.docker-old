import json

pkg_apt = {
    'docker-ce': {
        'needs': [
            'file:/etc/apt/sources.list.d/docker.list',
            'action:apt_update',
        ],
    },
}

release_names = {
    'debian': {
        8: 'jessie',
        9: 'stretch',
        10: 'buster',
        11: 'bullseye',
        12: 'bookworm',
    },
    'ubuntu': {
        20: 'focal',
        18: 'bionic',
        16: 'xenial',
    }
}

release_name = release_names.get(node.os, {}).get(node.os_version[0], 'stretch')
config = node.metadata.get('docker', {})

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

downloads = {
    '/usr/local/bin/docker-compose': {
        'url': 'https://github.com/docker/compose/releases/download/'
               '{}/docker-compose-Linux-x86_64'.format(
                    config.get('compose', {}).get('version', '1.28.0')),
        'sha256': config.get('compose', {}).get('checksum',
                                                '07a5e4104ac6495603454ada9c053a79ac554f65df3ffc28e833b571f6c3e6d1'),
        'mode': '0755',
    },
}


actions = {
    'install_gpg': {
        'command': 'curl -fsSL https://download.docker.com/linux/{os}/gpg | apt-key add -'.format(os=node.os),
        'unless': 'apt-key list | grep "Docker Release (CE deb) <docker@docker.com>"',
    },
    'apt_update': {
        'command': 'apt-get update',
        'triggered': True,
    },
}

if node.metadata.get('docker', {}).get('daemon_config', {}):
    files['/etc/docker/daemon.json'] = {
        'content': json.dumps(node.metadata.get('docker', {}).get('daemon_config', {}), indent=4)
    }
