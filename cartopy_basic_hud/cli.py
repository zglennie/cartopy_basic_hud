import argparse

# argparse doesn't offer an elegant way of letting the user type a boolean value into the
# CLI, other than action='store_true'/'store_false', so I'm following this the suggestion here:
#  https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse/36031646

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
