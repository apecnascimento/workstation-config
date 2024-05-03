from kitty import deploy_kitty
from docker import deploy_docker
from vagrant import deploy_vagrant
from kind import deploy_kind


deploy_docker(_sudo=True)
deploy_kind(_sudo=True)
deploy_kitty(_sudo=True)
deploy_vagrant(_sudo=True)
