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
    APP_ID = config("APP_ID", "6951121")
    API_HASH = config("API_HASH", "10654d2aa0d67e2f8759ba6a1644fa65")
    BOT_TOKEN = config("BOT_TOKEN", "1908889255:AAE3AAwrqkcLcBDncj_Ippeg1Zyf5O0ScQk")
    DEV = 1482769753
    OWNER = config("OWNER", "1482769753")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset superfast -c:v libx265 -crf 28 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
