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
    BOT_TOKEN = config("BOT_TOKEN", "5562438875:AAHKfFy6PdRkrEBqlt6w2mqghtlOKB19kSo")
    DEV = 1995886602
    OWNER = config("OWNER", "1995886602 -1001816242004")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset superfast -c:v libx265 -crf 28 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/eb6b1f4fe1e5e4a013534.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
