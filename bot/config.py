#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", "8978848")
    API_HASH = config("API_HASH", "24ce3cff2d32cf529df1c0018e28d6cf")
    BOT_TOKEN = config("BOT_TOKEN", "6555212335:AAEwTlWK9oc4T7fyTwkfrs0KYuiiNy4lkDo")
    DEV = 1995886602
    OWNER = config("OWNER", "5178332815")
    FFMPEG = config("FFMPEG", "ffmpeg -i '''{}''' -preset faster -c:v libx265 -metadata title='[Nikhil_Enc]'  -metadata:s:v title='480p - HEVC - 8bit'  -metadata:s:a title='40k - Nikhil_Enc' -metadata:s:s title='Subtitle Nikhil_Enc]' -vf 'drawtext=fontfile=Aclonica.ttf:fontsize=27:fontcolor=white:bordercolor=black@0.50:x=w-tw-10:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text=Nikhil_Enc' -s 854x480 -crf 28 -map 0:v -c:a aac  -b:a 35k -map 0:a -c:s copy -map 0:s? '''{}''' -y")
    THUMB = config("THUMBNAIL", "https://telegra.ph/file/eb6b1f4fe1e5e4a013534.jpg")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
