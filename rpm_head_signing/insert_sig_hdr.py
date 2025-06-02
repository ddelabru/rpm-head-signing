import argparse
import sys

from .insertlib import insert_sig_hdr as insertlib_insert_sig_hdr


def insert_sig_hdr(rpm_path, sigh_path):
    """
    Insert raw signature header back into an RPM. Overwrites any existing
    signature header in the RPM.
    """

    return insertlib_insert_sig_hdr(rpm_path, sigh_path)


def _main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("rpm_path", help="RPM file path", type=str)
    parser.add_argument("sigh_path", help="Signature header path", type=str)
    args = parser.parse_args(argv[1:])
    insert_sig_hdr(args.rpm_path, args.sigh_path)


if __name__ == "__main__":
    _main(sys.argv)
