import json

def load_settings(config_file='config.json'):
    with open(config_file, 'r') as f:
        settings = json.load(f)
    return settings

def update_settings(settings, args):
    settings['general']['iterations'] = args.iterations
    settings['diffusion']['inference_steps'] = args.inference_steps
    settings['general']['output directory'] = args.outputdir
    return settings
