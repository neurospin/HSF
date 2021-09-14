from rich import print

from hsf import __version__


def welcome():
    print(rf"""

    Hippocampal                            Factory
__/\\\________/\\\_____/\\\\\\\\\\\____/\\\\\\\\\\\\\\\_        
 _\/\\\_______\/\\\___/\\\/////////\\\_\/\\\///////////__       
  _\/\\\_______\/\\\__\//\\\______\///__\/\\\_____________      
   _\/\\\\\\\\\\\\\\\___\////\\\_________\/\\\\\\\\\\\_____     
    _\/\\\/////////\\\______\////\\\______\/\\\///////______    
     _\/\\\_______\/\\\_________\////\\\___\/\\\_____________   
      _\/\\\_______\/\\\__/\\\______\//\\\__\/\\\_____________  
       _\/\\\_______\/\\\_\///\\\\\\\\\\\/___\/\\\_____________ 
        _\///________\///____\///////////_____\///______________
                             Segmentation

                  Copyright (c) 2021 POIRET Clément
                                v{__version__}
                             License: MIT

                *************************************
             NeuroSpin | UNIACT/InsermU1141 | CEA Saclay
                *************************************

        """)
