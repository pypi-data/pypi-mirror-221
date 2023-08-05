==========================
VCEE Payment App for oTree
==========================

Quick start
-----------


#. Install the package

   .. code-block:: console

     $ pip install vcee-payment-app

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


Options
-------

encrypt_payment_file
^^^^^^^^^^^^^^^^^^^^

default: False

disable_waiting_for_others
^^^^^^^^^^^^^^^^^^^^^^^^^^

default: False
