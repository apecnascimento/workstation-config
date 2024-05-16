from pyinfra import host
from pyinfra.api import deploy
from pyinfra.facts.server import User
from pyinfra.operations import dnf, files


@deploy("Install Kitty teminal")
def deploy_kitty(_sudo=True):

    dnf.packages(
        name="Add kitty package",
	packages=["kitty"],
        present=True
    )

    files.directory(
        name="Ensure kitty config folder",
        path=f"/home/{host.get_fact(User)}/.config/kitty",
        user=host.get_fact(User),
        present=True
    )

    files.template(
        name="Add kitty tokio night theme",
        src="templates/kitty/nord.conf.j2",
        dest=f"/home/{host.get_fact(User)}/.config/kitty/nord.conf"
    )

    files.template(
        name="Add kitty tokio night theme",
        src="templates/kitty/kitty.conf.j2",
        dest=f"/home/{host.get_fact(User)}/.config/kitty/kitty.conf"
    )
