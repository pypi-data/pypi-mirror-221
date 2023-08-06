==========================
VCEE Payment App for oTree
==========================

Quick start
-----------


#. Install the package

   .. code-block:: console

     $ pip install otree-vcee-payment

#. Add the app to the end of your session config, e.g.:

   .. code-block:: python

      SESSION_CONFIGS = [
        dict(
            name="experiment",
            display_name="Some Experiment",
            num_demo_participants=1,
            app_sequence=["experiment", "result", "vceepayment"],
        ),
      ]

#. Download the payment file from the otree admin interface.

Options
-------

You can add the options to the session config, e.g.:

   .. code-block:: python

      SESSION_CONFIGS = [
        dict(
            name="experiment",
            display_name="Some Experiment",
            num_demo_participants=1,
            encrypt_payment_file=True,
            disable_waiting_for_others=True,
            app_sequence=["experiment", "result", "vceepayment"],
        ),
      ]

disable_waiting_for_others
^^^^^^^^^^^^^^^^^^^^^^^^^^

default: True

The default behavior is that participants are directly able to fill out their payment information as soon as they have completed everything else. Careful, this means only the amount earned up until that point in time is displayed and saved.
Setting disable_waiting_for_others to false forces every participant to wait for the last participant to complete everything before starting the payment app.
For more control of when a subject should be shown the payment app, set disable_waiting_for_others=True and add a WaitPage into the last app before vceepayment with the desired options.


encrypt_payment_file
^^^^^^^^^^^^^^^^^^^^

default: False

Encrypts the payment file. Only use this if you know what you are doing.

Remarks
-------
- Currently, the app requires a persistent file system to be run on. I.e., it does not work with an ephemeral filesystem (like Heroku).

- The payment file persists between sessions. This means you only need to download the payment file after the last session.
