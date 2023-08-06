
"""PyIono 
Ionosphere-related processing based on the data from space-geodetic techniques:

- Geodetic very-long-baseline-interferometry (VLBI): legacy VLBI system
- VLBI Global Observing System (VGOS): the next-generation VLBI system
- Global Navigation Satellite System (GNSS)

Usage:
------

    $ pyiono [options]

List ...:

    $ pyiono

Read ...:

    $ pyiono


Available options are:

    -h, --help         Show this help


Contact:
--------

- 

More information is available at:

- 
- 


Version:
--------

- pyiono v0.1.0
"""

# Standard library imports
import sys

def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [o for o in sys.argv[1:] if o.startswith("-")]
    # Show help message
    if "-h" in opts or "--help" in opts:
        print(__doc__)
        raise SystemExit()

if __name__ == "__main__":
	main()


