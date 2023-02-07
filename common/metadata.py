from dataclasses import dataclass, asdict


@dataclass
class Contact:
    name: str = "steve.kim"
    url: str = "http://example/ocell"
    email: str = "steve.kim@kakaocorp.com"


@dataclass
class Licence_info:
    name: str = "Apache 2.0"
    url: str = "https://www.apache.org/licenses/LICENSE-2.0.html"


@dataclass
class Metadata:
    """
    Basic metadata and docs for fastapi app
    """

    description: str = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

    title: str = "FastAPI Skeleton"
    version: str = "0.0.1"
    terms_of_service: str = "http://example.com/terms/"
    contact: Contact = Contact()
    license_info: Licence_info = Licence_info()


def get_metadata():
    """
    Return metadata
    :return:
    """
    return asdict(Metadata())
