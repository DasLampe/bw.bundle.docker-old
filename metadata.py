defaults = {}

if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            "gnupg-agent": {'installed': True},
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
