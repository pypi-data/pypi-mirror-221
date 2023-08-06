import eikon


def before_scenario(context, scenario):
    context.exception = None
    context.response = None
    eikon.set_app_key("")


def after_scenario(context, scenario):
    print(f"Result of scenario '{scenario.name}': {scenario.status.name}")
