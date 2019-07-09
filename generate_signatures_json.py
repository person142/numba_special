import os
import json
import collections
import re

import scipy.special.cython_special as cysc

SIGNATURES_FILE = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'numba_special',
    'signatures.json'
)

SIGNATURE_REGEX = ' *([a-z \*]+) ([a-zA-Z0-9_]+)\((.*)\)'

SPECIAL_DOC_TO_CTYPES = {
    'double': 'c_double',
    'float': 'c_float',
    'long': 'c_long'
}

SPECIAL_DOC_TO_CYTHON_SPECIALIZATION = {
    'double': 'double',
    'float': 'float',
    'long': 'long'
}


def get_signatures():
    signatures = collections.defaultdict(dict)
    doc = cysc.__doc__.split('\n')
    for line in doc:
        match = re.match(SIGNATURE_REGEX, line)
        if match:
            return_type = match.group(1)
            name = match.group(2)
            arg_types = tuple(match.group(3).split(', '))
            signatures[name][arg_types] = return_type
    return signatures


def determine_fused_args(specializations):
    arg_types = collections.defaultdict(list)
    for args in specializations.keys():
        for i, arg in enumerate(args):
            arg_types[i].append(arg)
    # These args have fused types
    changing_args = {
        i: types for i, types in arg_types.items()
        if types[1:] != types[:-1]
    }
    fused_args = []
    seen_args = set()
    for i1, types1 in changing_args.items():
        if i1 in seen_args:
            continue
        seen_args.add(i1)

        cluster = {i1}
        for i2, types2 in changing_args.items():
            if types1 == types2:
                # These arugments always have the same types, so they
                # are the same fused type.
                cluster.add(i2)
                seen_args.add(i2)
        fused_args.append(cluster)

    # Return the first occurance of a fused arg for each fused type.
    return {min(cluster) for cluster in fused_args}


def convert_signature(specializations):
    signatures = {}
    fused_args = determine_fused_args(specializations)
    for args, return_type in specializations.items():
        try:
            ctypes_signature = [SPECIAL_DOC_TO_CTYPES[return_type]]
        except KeyError:
            continue
        try:
            ctypes_signature += [SPECIAL_DOC_TO_CTYPES[arg] for arg in args]
        except KeyError:
            continue

        cython_specialization = '|'.join([
            SPECIAL_DOC_TO_CYTHON_SPECIALIZATION[arg]
            for i, arg in enumerate(args)
            if i in fused_args
        ])
        signatures[cython_specialization] = ctypes_signature

    if signatures and not fused_args:
        signatures = {'': list(signatures.values())[0]}
    return signatures


def main():
    raw_signatures = get_signatures()
    signatures = {}
    for name, raw_specializations in raw_signatures.items():
        specializations = convert_signature(raw_specializations)
        if specializations:
            signatures[name] = specializations

    with open(SIGNATURES_FILE, 'w') as f:
        json.dump(signatures, f, indent=4)


if __name__ == '__main__':
    main()
