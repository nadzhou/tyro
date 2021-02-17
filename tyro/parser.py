import argparse as ap 


def parse_args(): 
    parser = ap.ArgumentParser(description="Tool to get Tyrosine sulfation in a set of sequences.")

    parser.add_argument("-in",
                        help="fasta input file",
                        dest="input", 
                        type=str, 
                        required=True
                        )

    parser.add_argument("-f",
                        help="input file format, fasta by default",
                        dest="format", 
                        type=str, 
                        default="fasta"
                        )

    return parser.parse_args()