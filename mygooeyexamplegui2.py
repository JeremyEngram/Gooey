from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser(description="Software Installer")

    parser.add_argument(
        "software",
        metavar="Software Name",
        type=str,
        help="Enter the name of the software you want to install:"
    )

    parser.add_argument(
        "--version",
        metavar="Version",
        type=str,
        help="Specify the version of the software (optional):"
    )

    args = parser.parse_args()
    
    # Here, you would include code to install the specified software
    # For demonstration purposes, we'll print a message.
    if args.version:
        print(f"Installing {args.software} version {args.version}...")
    else:
        print(f"Installing {args.software}...")

if __name__ == "__main__":
    main()
