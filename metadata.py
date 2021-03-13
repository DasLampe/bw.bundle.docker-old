defaults = {}

@metadata_reactor
def add_apt_packages(metadata):
    if not node.has_bundle("apt"):
        raise DoNotRunAgain

    return {
        'apt': {
            'packages': {
                "gnupg-agent": {'installed': True},
                'gnupg2': {'installed': True},
                'apt-transport-https': {'installed': True},
                'ca-certificates': {'installed': True},
                'curl': {'installed': True},
                'software-properties-common': {'installed': True},
                # Uninstall old versions
                'docker': {
                    'installed': False
                },
                'docker-engine': {
                    'installed': False,
                },
                'docker.io': {
                    'installed': False,
                },
                'containerd': {
                    'installed': False,
                },
                'runc': {
                    'installed': False,
                }
            }
        }
    }

@metadata_reactor
def add_users_to_docker_group(metadata):
    if not node.has_bundle('users'):
        raise DoNotRunAgain

    processed_metadata = {
        'users': {}
    }

    for username, userdata in metadata.get('users').items():
        if userdata.get('sudo', False):
            processed_metadata['users'][username] = {
                'add_groups': ['docker']
            }

    return processed_metadata
