Update Handlers
===============

Handlers are used to instruct pyroblack about which kind of updates you'd like to handle with your callback functions.
For a much more convenient way of registering callback functions have a look at :doc:`Decorators <decorators>` instead.

.. code-block:: python

    from pyrogram import Client
    from pyrogram.handlers import MessageHandler

    app = Client("my_account")


    def dump(client, message):
        print(message)


    app.add_handler(MessageHandler(dump))

    app.run()

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

-----

.. currentmodule:: pyrogram.handlers

Index
-----

.. hlist::
    :columns: 3

    - :class:`MessageHandler`
    - :class:`EditedMessageHandler`
    - :class:`DeletedMessagesHandler`
    - :class:`CallbackQueryHandler`
    - :class:`MessageReactionUpdatedHandler`
    - :class:`MessageReactionCountUpdatedHandler`
    - :class:`InlineQueryHandler`
    - :class:`ChosenInlineResultHandler`
    - :class:`ChatMemberUpdatedHandler`
    - :class:`UserStatusHandler`
    - :class:`StoryHandler`
    - :class:`PollHandler`
    - :class:`DisconnectHandler`
    - :class:`RawUpdateHandler`

-----

Details
-------

.. Handlers
.. autoclass:: MessageHandler()
.. autoclass:: EditedMessageHandler()
.. autoclass:: DeletedMessagesHandler()
.. autoclass:: CallbackQueryHandler()
.. autoclass:: MessageReactionUpdatedHandler()
.. autoclass:: MessageReactionCountUpdatedHandler()
.. autoclass:: InlineQueryHandler()
.. autoclass:: ChosenInlineResultHandler()
.. autoclass:: ChatMemberUpdatedHandler()
.. autoclass:: UserStatusHandler()
.. autoclass:: StoryHandler()
.. autoclass:: PollHandler()
.. autoclass:: DisconnectHandler()
.. autoclass:: RawUpdateHandler()
