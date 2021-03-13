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
