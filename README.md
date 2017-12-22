# SINBIN
Pastebin Recon tool.


# Setup

     python3 setup.py
     put your pastebin api_dev_key, in the sinbin.py file.
     run python3 sinbin.py --help
     
     

# Example

    C:\paste-python>SinBin.py --help


                  ┈╭━━━━━━━━━━━╮┈
                  ┈┃╭━━━╮┊╭━━━╮┃┈
                  ╭┫┃┈▇┈┃┊┃┈▇┈┃┣╮
                  ┃┃╰━━━╯┊╰━━━╯┃┃
                  ╰┫╭━╮╰━━━╯╭━╮┣╯
                  ┈┃┃┣┳┳┳┳┳┳┳┫┃┃┈
                  ┈┃┃╰┻┻┻┻┻┻┻╯┃┃┈
                  ┈╰━━━━━━━━━━━╯┈
  
     ███████╗██╗███╗   ██╗      ██████╗ ██╗███╗   ██╗
     ██╔════╝██║████╗  ██║      ██╔══██╗██║████╗  ██║
     ███████╗██║██╔██╗ ██║█████╗██████╔╝██║██╔██╗ ██║
     ╚════██║██║██║╚██╗██║╚════╝██╔══██╗██║██║╚██╗██║
     ███████║██║██║ ╚████║      ██████╔╝██║██║ ╚████║
     ╚══════╝╚═╝╚═╝  ╚═══╝      ╚═════╝ ╚═╝╚═╝  ╚═══╝

     (Version:1.0)
     (Author:LukeBob)

     usage: SinBin.py --query --all                       List all Email:Password entries in database.
     usage: SinBin.py --query --email my@email.com        Query database for single email.
     usage: SinBin.py --stream --time 0.2                 Stream latest trending pastes.
     usage: SinBin.py --dump                              Scrape for Email:Password combinations, add them to database.
     usage: SinBin.py --drop                              Drop all entries from database.
     usage: SinBin.py --purge                             Drop all duplicate entries from databse.
     usage: SinBin.py --count                             Count all entries in database.
     usage: SinBin.py --backup                            Make a backup of database.

     Pastebin tool

     optional arguments:
       -h, --help            show this help message and exit
       -d, --dump            Scrape pastebin for Email:password dumps.
       -s, --stream          Stream trending pastebin content.
       -t TIME, --time TIME  intervals to print data in seconds default: 0.3
       -q, --query           Query database.
       -e EMAIL, --email EMAIL
                             Email to look for entries
       -a, --all             Dump(List) all entries stored in database
       -x, --drop            Drop(Delete) all Email:Password entries.
       -p, --purge           Drop(Delete) duplicate entries in database
       -c, --count           Count entries in database
       -b, --backup          Make a backup of database.
 

       MOTTO: WYO OR GTFO!

    C:\paste-python>

# Contributors

**LukeBob**


# License

**Copyright (c) 2017 LukeBob (MIT)**
