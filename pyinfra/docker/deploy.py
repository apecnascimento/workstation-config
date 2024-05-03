from pyinfra import host
from pyinfra.api import deploy
from pyinfra.facts.server import User
from pyinfra.operations import yum, systemd, server


@deploy("Install and configure Docker")
def deploy_docker():

    yum.repo(
        name="Add docker-ce-stable to yum repo",
        baseurl="https://download.docker.com/linux/fedora/$releasever/$basearch/stable",
        gpgkey="https://download.docker.com/linux/fedora/gpg",
        gpgcheck=True
    )

    yum.packages(
        name="Ensure docker",
        packages=[
            "docker-ce",
            "docker-ce-cli",
            "containerd.io",
            "docker-buildx-plugin",
            "docker-compose-plugin"
        ],
        present=True,
        update=True
    )

    server.shell(
        name="Add user to Docker group",
        commands=f"usermod -aG docker {host.get_fact(User)}"
    )

    systemd.service(
        name="Enable docker service",
        service="docker",
        running=True,
        enabled=True
    )
