from pyinfra.api import deploy
from pyinfra.operations import dnf, files


@deploy("Deploy kind and k9s")
def deploy_kind():

    files.download(
        name="Download kind binary",
        src="https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64",
        dest="/usr/local/bin/kind",
        mode="755"
    )

    dnf.rpm(
        name="Add k9s",
        src="https://github.com/derailed/k9s/releases/download/v0.30.8/k9s_linux_amd64.rpm",
        present=True
    )
