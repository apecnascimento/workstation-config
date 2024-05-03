from pyinfra.api import deploy
from pyinfra.operations import dnf, server


@deploy("Install Vagrant and KVM")
def deploy_vagrant():
    dnf.packages(
        name="Add vagrant and libvirt packages",
        packages=[
            "vagrant",
            "qemu-kvm",
            "virt-install",
            "gcc",
            "libvirt",
            "libvirt-devel",
            "libxml2-devel",
            "make",
            "ruby-devel",
            "ruby-devel"
        ],
        present=True
    )

    server.shell(
        name="Install pluguins",
        commands=[
            "vagrant plugin install vagrant-libvirt",
            "vagrant plugin install vagrant-mutate"
            ]
    )
