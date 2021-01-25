# Install Docker-CE and Docker-Compose
Installs Docker for Ubuntu (LTS releases) or Debian.

## Config
```python
node['foobar'] = {
    'metadata': {
        'docker': {
            'daemon_config': {
                'daemon_config': {
                    'registry-mirrors': [
                        'https://<your-mirror>'
                    ]
                },
            },
            'compose': {
                'version': '1.28.0',
                'checksum': '07a5e4104ac6495603454ada9c053a79ac554f65df3ffc28e833b571f6c3e6d1',
            },
        },
    }
}
```
The ``daemon_config``-dict is passed as json into ``/etc/docker/daemon.json``