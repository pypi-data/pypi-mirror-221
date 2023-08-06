==============
uagents-twilio
==============

.. image:: https://img.shields.io/pypi/v/uagents-twilio.svg
    :target: https://pypi.org/project/uagents-twilio
    :alt: PyPI version


----

This `uagents <https://github.com/fetchai/uAgents>`_ utlity was generated with `Cookiecutter <https://github.com/cookiecutter/cookiecutter>`_.


Features
--------

* uagents protocols to send SMS or Whatsapp messages using twilio
* supports on_message and on_query methods to receive and send messages


Installation
------------

You can install "uagents-twilio" via `pip <https://pypi.org/project/pip/>`_ from `PyPI <https://pypi.org/project>`_::

    $ pip install uagents-twilio

You can install "uagents_twilio" via poetry::

    $ poetry add uagents-twilio

Usage
-----

* Create .env file in root folder of project::

    AGENT_ADDRESS=""
    ACCOUNT_SID=""
    AUTH_TOKEN=""
    FROM_NUMBER=""
    WP_FROM_NUMBER=""
    TO_NUMBER=""

* Create a uagents in your project

* Import uagents_twilio protocol::

    $ from uagents_twilio.protocols.messages import service_protocol

* Include protocol in uagent::

    $ service_agent.include(service_protocol)

* Use functions::

    from uagents_twilio.models import Message, MessageType

    @service_agent.on_interval(period=2.0)
    async def send_message(ctx: Context):
        await ctx.send(
            AGENT_ADDRESS,
            Message(receiver="<replace_your_number>", msg="hello there bob", type=MessageType.sms),
        )
