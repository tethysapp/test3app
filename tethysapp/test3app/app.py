from tethys_sdk.base import TethysAppBase


class Test3App(TethysAppBase):
    """
    Tethys app class for Test3App.
    """

    name = 'Test3App'
    description = ''
    package = 'test3app'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'test3app'
    color = '#2f3640'
    tags = ''
    enable_feedback = False
    feedback_emails = []